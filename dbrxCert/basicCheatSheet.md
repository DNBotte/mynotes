# MY CHEATSHEET FOR STUDYING FOR THE DATABRICKS CERT

# SPARK

* Write raw text to DBFS

```pyth
dbutils.fs.put("FileStore/filename.tsv", raw, overwrite = True)

df = (spark.read
	.option("header", "true")
	.option("sep", "\t")
	.option("inferSchema", "true")
	.csv("/FileStore/filename.tsv")
	)

display(df)
```

* Pandas -> Spark

```python
import pandas as pd
from io import StringIO

raw = """Carname\tColor\tAge\tSpeed\tAutoPass
BMW\tred\t5\t99\tY
Volvo\tblack\t7\t86\tY
VW\tgray\t8\t87\tN
VW\twhite\t7\t88\tY
Ford\twhite\t2\t111\tY
VW\twhite\t17\t86\tY
Tesla\tred\t2\t103\tY
BMW\tblack\t9\t87\tY
Volvo\tgray\t4\t94\tN
Ford\twhite\t11\t78\tN
Toyota\tgray\t12\t77\tN
VW\twhite\t9\t85\tN
Toyota\tblue\t6\t86\tY"""


pdf = pd.read_csv(StringIO(raw), sep = "\t")

df = spark.createDataFRame(pdf)
```

* Display methods

```python
print(f"Rows: {df.count()}, Cols: {len(df.columns)}")

df.printSchema()
```
#### equivalent to df.describe()

```python
dispaly(df.describe())
```

## Write to catalog as a permanent table

```python
df.write.format("delta").mode("overwrite").saveAsTable(Iimp.car_color_bronze")

# Test is out:

result = spark.sql("SELECT Carname, AVG(Speed) as avg_speed FROM imp.car_color_bronze GROUP BY Carname ORDER BY avg_speed DESC")
display(result)
```
#### Confirm table registered in catalog:
```python
display(spark.sql("SHOW TABLES IN imp"))
```
