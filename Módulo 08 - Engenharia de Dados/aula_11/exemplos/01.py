from pyspark.sql import SparkSession, DataFrame

spark = (
    SparkSession.builder.config("spark.driver.host", "127.0.0.1")
    .appName("SparkSQL")
    .getOrCreate()
)

df = spark.read.csv("data01.csv", header=True)

df.show()