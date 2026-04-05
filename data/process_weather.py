from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# 1. Initialize the Session with the Postgres Connector
spark = SparkSession.builder \
    .appName("WeatherBatchIngestion") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.5.0") \
    .getOrCreate()

# 2. Create some dummy data (Replace this with a CSV read later)
# data = [("Chennai", 32, "Sunny"), ("Bangalore", 24, "Cloudy"), ("Mumbai", 28, "Rainy")]
# columns = ["city", "temp_celsius", "condition"]
# df = spark.createDataFrame(data, columns)
df = spark.read.csv("/opt/airflow/data/weather_data.csv", header=True, inferSchema=True)

# 3. A Simple Transformation (Tester logic!)
# Convert Celsius to Fahrenheit: (C * 9/5) + 32
df_transformed = df.withColumn("temp_fahrenheit", (col("temp_celsius") * 9/5) + 32)

print("--- Transformed Data ---")
df_transformed.show()

# 4. Write to Postgres
# Note: 'de-postgres' is the container name in your Docker network
try:
    df_transformed.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://de-postgres:5432/weather_db") \
        .option("dbtable", "city_weather") \
        .option("user", "spark_user") \
        .option("password", "spark_pass") \
        .option("driver", "org.postgresql.Driver") \
        .mode("overwrite") \
        .save()
    print("Successfully saved to Postgres!")
except Exception as e:
    print(f"Postgres Write Failed: {e}")

spark.stop()