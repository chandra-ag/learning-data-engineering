import os
import pandas as pd 
from dotenv import load_dotenv
from sqlalchemy import create_engine
import requests


print("--- STEP 1: EXTRACT ---")
print("Extracting data from Open-Meteo API...")

# This URL specifically asks for the daily max temperature in London for the first 10 days of 2024
url = "https://archive-api.open-meteo.com/v1/archive?latitude=51.5085&longitude=-0.1257&start_date=2024-01-01&end_date=2024-01-10&daily=temperature_2m_max"

# 1. 'GET' the data from the URL
response = requests.get(url)

# 2. Always check if the request was successful! (Status Code 200 means OK)
if response.status_code == 200:
    print("[SUCCESS] Successfully downloaded data from the API!")
    
    # 3. Convert the raw text response into a Python dictionary (JSON)
    raw_data = response.json()
    
    # Let's look at exactly what the API handed us
    print("\n--- RAW JSON OUTPUT ---")
    print(raw_data['daily'])
    
else:
    print(f"[ERROR] Failed to get data. The API returned status code: {response.status_code}")

# --- STEP 2: TRANSFORM ---
print("\n--- STEP 2: TRANSFORM ---")
print("Converting JSON to Pandas DataFrame...")

# 1. Isolate the specific dictionary we care about from the API response
daily_data = raw_data['daily']

print(daily_data)

# 2. Convert the dictionary into a tabular Pandas DataFrame
df = pd.DataFrame(daily_data)

# 3. Rename columns to be database-friendly (standardizing names)
df = df.rename(columns={
    'time': 'weather_date',
    'temperature_2m_max': 'max_temp_celsius'
})

# 4. DE Best Practice: Enforce strict data types! 
# APIs return dates as text strings. We need to tell Pandas it's a real Date.
df['weather_date'] = pd.to_datetime(df['weather_date'])

# Let's inspect our clean, transformed data
print("\n[SUCCESS] Data Successfully Transformed!")
print(df.head()) # .head() prints just the first 5 rows
print("\nData Types:")
print(df.dtypes)

# --- STEP 3: LOAD ---
print("\n--- STEP 3: LOAD ---")
print("Loading data into PostgreSQL...")

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# 1. Load credentials from your hidden .env file
load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# 2. Create the SQLAlchemy Engine (The Bridge)
db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
engine = create_engine(db_url)

# 3. Write the DataFrame directly into a Postgres table
try:
    # Pandas handles the CREATE TABLE and INSERT statements automatically!
    df.to_sql(
        name='london_weather',  # The name of the table in your database
        con=engine,             # The connection bridge
        if_exists='replace',    # If the table exists, drop it and recreate it
        index=False             # Don't load the Pandas row numbers (0, 1, 2) as a column
    )
    print("[SUCCESS] Pipeline Complete! Data successfully loaded into the 'london_weather' table.")
except Exception as e:
    print("[ERROR] Failed to load data.")
    print(e)

import os
import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

print("--- STARTING INCREMENTAL PIPELINE ---")

# 1. Setup the Database Connection
load_dotenv()
db_url = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(db_url)

# --- STEP 1: THE LOOK-BACK ---
print("Checking database for latest records...")
try:
    # We use a simple SQL query to find the maximum date currently in the table
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(weather_date) FROM london_weather;")).scalar()
        
        if result:
            # If the table exists and has data, start pulling from the day AFTER the max date
            start_date = (result + timedelta(days=1)).strftime('%Y-%m-%d')
            print(f"Found existing data. Latest date is {result}. Fetching new data starting from {start_date}.")
        else:
            # Fallback: If the table is empty, do a historical load starting from Jan 1st
            start_date = "2024-01-01"
            print("Table is empty. Running historical load from 2024-01-01.")
except Exception as e:
    # Fallback: If the table doesn't exist yet at all
    start_date = "2024-01-01"
    print("Table does not exist yet. Running initial historical load from 2024-01-01.")

# We always want the end date to be today
end_date = datetime.today().strftime('%Y-%m-%d')

# Prevent the script from running if we are already fully up to date!
if start_date > end_date:
    print("Database is already up to date! Exiting pipeline.")
    exit()

# --- STEP 2: EXTRACT & TRANSFORM ---
print(f"Extracting API data from {start_date} to {end_date}...")
# Notice the 'f' string here. We are injecting our dynamic dates straight into the URL!
url = f"https://archive-api.open-meteo.com/v1/archive?latitude=51.5085&longitude=-0.1257&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max"

response = requests.get(url)
if response.status_code == 200:
    raw_data = response.json()
    
    # Transformation (Same as yesterday)
    df = pd.DataFrame(raw_data['daily'])
    df = df.rename(columns={'time': 'weather_date', 'temperature_2m_max': 'max_temp_celsius'})
    df['weather_date'] = pd.to_datetime(df['weather_date'])
    
    # Drop rows where temperature is null (just in case today's data isn't fully recorded yet)
    df = df.dropna(subset=['max_temp_celsius'])
    
    print(f"Successfully transformed {len(df)} new rows.")
else:
    print(f"API Failed. Status Code: {response.status_code}")
    exit()

# --- STEP 3: LOAD (APPEND) ---
print("Appending new data to PostgreSQL...")
try:
    # CRITICAL CHANGE: if_exists is now 'append' instead of 'replace'
    df.to_sql('london_weather', con=engine, if_exists='append', index=False)
    print("[SUCCESS] Incremental Load Complete!")
except Exception as e:
    print("[ERROR] Failed to append data.")
    print(e)