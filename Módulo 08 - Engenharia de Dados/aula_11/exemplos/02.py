from pyspark.sql import SparkSession, DataFrame, Row

spark = (
    SparkSession.builder.config("spark.driver.host", "127.0.0.1")
    .appName("SparkSQL")
    .getOrCreate()
)

df = spark.createDataFrame([
    Row(nome="João", idade=25, cidade="São Paulo"),
    Row(nome="Maria", idade=30, cidade="Rio de Janeiro"),
    Row(nome="Pedro", idade=35, cidade="Belo Horizonte"),
])

df.show()

df.write.mode("overwrite").csv("data02.py")
