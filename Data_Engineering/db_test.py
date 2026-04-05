import pandas as pd
from sqlalchemy import create_engine

# 1. Define the connection string to your Docker Postgres container
# Format: postgresql+driver://username:password@host:port/database_name
db_url = "postgresql+psycopg2://postgres:admin@localhost:5432/postgres"

try:
    # 2. Create the engine (the bridge to the database)
    engine = create_engine(db_url)
    
    # 3. Write a simple SQL query to test the connection
    query = "SELECT COUNT(*) AS total_rows FROM index_fund_history;"
    
    # 4. Use Pandas to run the query and store the result in a DataFrame
    df = pd.read_sql(query, engine)
    
    print("✅ Connection Successful!")
    print(f"Your database currently has {df.iloc[0]['total_rows']} rows in the index_fund_history table.")

except Exception as e:
    print("❌ Connection Failed. Check your Docker container and credentials.")
    print(e)