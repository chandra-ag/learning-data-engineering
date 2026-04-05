from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType,IntegerType
from pyspark.sql.functions import col,expr,sum,avg,max
spark = SparkSession.builder \
    .appName("Day3") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
schema = StructType([
    StructField("id",IntegerType(),True),
    StructField("name",StringType(),True),
    StructField("department",StringType(),True),
    StructField("salary",IntegerType(),True)
])
df =spark.read.csv("employees.csv",header=True,schema=schema)
df.show()
df.printSchema()
df.groupBy("department").count().show()
df.groupBy("department").agg(sum("salary").alias("total_salary")).show()
df.groupBy().agg(sum("salary").alias("total_salary_all")).show()
df.groupBy("department").agg(sum("salary").alias("total_salary"),
     avg("salary").alias("average_salary"),
     max("salary").alias("max_salary")).show()
    
spark.stop()
