from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("Day2ReadCSV") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
df = spark.range(50)
df.show()
df.filter(df.id % 2 == 0).show()
df.filter(df.id > 10 and df.id < 30).show()
spark.stop()