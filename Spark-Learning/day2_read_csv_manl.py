from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col
spark = SparkSession.builder \
    .appName("Day2ReadCSV") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("department", StringType(), True),
    StructField("salary", IntegerType(), True)
])
df = spark.read.csv("employees.csv", header=True, schema=schema)
df.show()
df.printSchema()
df.select("name", "salary").show()
df.filter(df.salary > 50000).show()
df2 = df.withColumn("salary_after_tax", col("salary") * 0.7)
df3 = df.filter(col("department") == "IT")\
    .filter(col("salary") > 60000)\
    .withColumn("bonus", col("salary") * 0.20)
df2.show()
df3.show()
spark.stop()