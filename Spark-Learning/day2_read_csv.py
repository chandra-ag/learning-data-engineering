from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Day2ReadCSV") \
    .getOrCreate()
df = spark.read.csv("employees.csv", header=True, inferSchema=True)
df.show()
df.printSchema()
spark.stop()
