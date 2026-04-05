from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Day1") \
    .getOrCreate()

df = spark.range(10)
df.show()

spark.stop()