from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[*]").appName("HelloWorld").getOrCreate()
    kolumny = ["Spark Version", "Scala Version", "Date"]
    dane = [
        ("3.1.2", "2.12", "May, 2021"),
        ("3.1.1", "2.12", "Mar, 2021"),
        ("3.1.0", "2.12", "Jan 2021"),
    ]
    dfFromData2 = spark.createDataFrame(dane).toDF(*kolumny)
    dfFromData2.show()

