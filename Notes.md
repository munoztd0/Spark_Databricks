# Master Databricks and Apache Spark

Ressources: https://github.com/bcafferky/shared/tree/master/MasterDatabricksAndSpark

## Table of Contents
1. [Introduction](#lesson-1-introduction)


## Lesson 1: Introduction
- Combining the big 3 : AI, Big Data, and Cloud Computing
- What is Apache Spark? Open source big data platform for Data Science and Engineering
- Raw, not ide, not notebook, not a database, no collaboration, no version control
- Not optimized for cloud
- Databricks: Commercial version of Apache Spark, complementary services, optimized for cloud, ideal for data science team collaboration, version control, and more

### What is special about Databricks?
Scale up reached a cap ... Databricks can scale out ! What is scale out? It is the ability to add more resources to a system to increase its capacity. Databricks can scale out to handle more data and more users. Same as vertical scaling, vs horizontal scaling. *horizontal scaling is like scaling out, adding more nodes to a cluster.*

### First came Hadoop
Was first open-source big data platform, but it was slow and complex. Spark was created to be faster and easier to use. Spark is 100x faster than Hadoop.

### The Apache Haddop Ecosystem
![alt text](image-1.png)
- HDFS: Hadoop Distributed File System, partioning data across multiple nodes
- Zookeeper: Distributed coordination service, meaning it helps manage a cluster of machines
- YARN: Yet Another Resource Negotiator, manages resources in a Hadoop cluster
- Spark: In-memory *real-time* data processing engine, faster than Hadoop
- Kafka: Distributed streaming platform, used for building real-time data pipelines and streaming apps


### Spark Components

Spark is a replacement of MapReduce because everybody that work with data knows that reading and writing in disk gonna slow everything down, so Spark is in-memory, meaning it reads and writes data in memory, which is faster than reading and writing to disk.

Spark has 4 main components:
- Spark SQL: SQL interface for Spark, allows you to run SQL queries on Spark data (80% of data science work)
- Spark Streaming: Real-time data processing, like Kafka
- MLlib: Machine learning library, built on top of Spark
- GraphX: Graph processing library, built on top of Spark

### General Spark Cluster Architecture

![alt text](image-2.png)

- Driver runs the user main function
- Data sources(HDFS, SQL, NoSQl. DataLake) all fancy names that emulates HDFS behavior but with more or less features or efficient way to be faster.
- Spark is not for storage, it is for processing. It is not a database, it is a processing engine.
- Spark core: The core of Spark, the engine that runs the code 
- Spark SQL: *SQL interface for Spark, even if it's not stored in a SQL database, you can still run SQL queries on it*

### Azure Databricks
Has notebooks like Jupyter, but with more features. It is a collaborative environment for data science and engineering teams. It is optimized for cloud, and it has a job scheduler, a cluster manager, and a workspace for collaboration. It is integrated with Azure, so you can use Azure services like Azure Data Lake, Azure Blob Storage, and Azure SQL Data Warehouse. It is also integrated with Azure Active Directory, so you can use your Azure AD credentials to log in.


### Lesson 2: Create a Databricks Workspace
- Runtime is special version of Spark, optimized for Databricks

%fs commande for databricks file system
also %sh for shell commands
%sql SHOW TABLES oR DESCRIBE TABLE tablename

### Lesson 3: Demo - Introduction to Databricks

### Lesson 4: Create a Spark Cluster from the Azure Portal
- HDinsight is a managed Hadoop service in Azure to run Spark, Hadoop, and other big data frameworks
- PASS: Platform as a Service, like Azure Databricks for Spark
- Then use Zeppelin or Jupyter notebooks to run Spark code

### Lesson 5: Using the Data Science Process 
- Framework the structure of your work
-- Business understanding: identify the problem, define the goal and the data required
-- Data Collection
-- Data Exploration: understand the data, clean the data, visualize the data
-- Feature Engineering: create new features from the data
-- Modeling: build a model to predict the target variable
-- Evaluation: evaluate the model, tune the model
-- Deployment: deploy the model to production

#### Business Understanding/ Analysis
- Document the problem, the goal, and the data required
- Cost Constraints: how much money can you spend on the project?
- Assumptions: what assumptions are you making about the data?
- Identify Data Sources: where is the data coming from?

#### Data Engineering
- Pull data from data sources
- Clean the data
- EDA: Exploratory Data Analysis, visualize the data, understand the data
- Find pareto principle: 80% of the results come from 20% of the causes
- Evaluate and identify problems with the data
- Feature Engineering: transform the data into model features

#### Modeling
- Split the data into training and testing sets
- Data resampling: oversample the minority class, undersample the majority class
- Select the best model: use cross-validation to select the best model
- Model deployment: deploy the model to production
- Post Deployment: monitor the model, retrain the model, visualize 

### Lesson 6: Understanding Spark SQL

What is Spark SQL?
- Distributed dataframe at scale
Even if you are doing R or Python, you are still using Spark SQL under the hood which is being optimized by Spark SQL engine.

Schema on read: advantagous because you dont have to replicate, ingest or anything, just query it
Data is not in an RDBMS, it is in a file, so you have to define the schema when you read the data
External File is Described Structurally
Does NOT have a database catalog and NO stored procedures or functions
Does not support referential integrity ! i.e. no foreign keys
Limited security features, no user roles, no row-level security

![alt text](<Screenshot from 2024-11-25 14-17-19.png>)

#### Delta Lake
 Delta lake is Databricks responses to Redshift, DataFactory and Snowflake datawarehouses.
 - Delta lake delivers more RDBMS like functionality, but with the scale and flexibility
- Use parquet which is very fast and efficient, and it is columnar storage, so it is faster than row storage 
RDBMS running on clusters, with ACID transactions, schema enforcement, and data versioning
- ACID: Atomicity (all or nothing), Consistency (data is consistent), Isolation (transactions are isolated), Durability (data is durable)

Spark is trying to bring OLTP.
- OLTP: Online Transaction Processing, like a bank transaction

![alt text](image-3.png)

Delta lake is moving towards a datawarehouse.


### Lesson 7: Using Spark SQL  Data Definition Language (DDL)

What are SQL DDL ?
- Create, Alter, Drop, Truncate, Rename, Comment, Describe Database Objects
- Create, Drop or change Partitions (so you can contorl how your data is save)

- SHOW FUNCTIONS 
- SHOW CREATE TABLE ( give you the schema of the table that  you can copy and paste and chnange !)
- USE mydatabase (to switch to a database / the context)
- Database are like folders/namespace, they are not like databases in SQL
- Properties are spark specific, they are not SQL standard, they allow you to set value pairs
- You want to save you data in a partionned way, so you can query it faster like for example zipcode, date, etc

### Lesson 9: Creating a Database and Tables in Spark SQL: Databricks
The AdventureWorks Project Use Case : get business insights from the data
Then create a ML model to predict the sales of a product
Star schema is the best schema for data warehousing, the idea is that your fact table only holds metrics
Metrics are actually the measures that you want to analyze, like sales, revenue, etc
The dimension tables are the tables that hold the attributes of the metrics, like the product, the customer, the date, etc
dimensions don't join to each other, they only join to the fact table, if they do join to each other, then they are not dimensions, they are fact tables or it's a snowflake schema
- Redundancy is good in data warehousing, because it makes the queries faster

### Lesson 10: Creating a Database and Tables in Spark SQL: Raw Spark
- Permanent storage VS Temporary storage on the cluster: You have to make sure that 
you enable container storage on the cluster, so that the data is not lost when the cluster is terminated !
- Using stuff like count(*) is gonna be optimized by Spark.


### Lesson 11 & 12:  SQL
- CREATE OR REPLACE TABLE: if the table exists, it will replace it, important because in databricks sometimes you can't create if the metadata already exists you have to replace it
- CASE statement: like if else statement
- Common Table Expressions (CTE): like a subquery, but you can reference it multiple times
- WHERE <> 'NA' for when you want everything except


### Lesson 13: Joins
- Inner Join: only the rows that match in both tables
- Left Join: all the rows in the left table, and the rows that match in the right table
- Full Outer Join: all the rows in both tables
- Left Semi Join: all the rows in the left table that match in the right table (only for subsetting)
- Cross Join: all the rows in the left table with all the rows in the right table (useless)
- Anti Join: all the rows in the left table that do not match in the right table (only for subsetting)

### Lesson 14: Using set operators
union, intersect, except
union all will keep duplicates, union will remove duplicates !
Table on the fly you can use VALUES

### Lesson 15: SQL
- Scalar functions: executes for each row, like UPPER, LOWER, LENGTH: can add serious overheard but faster than using any other language
- Aggregate functions: like SUM, AVG, COUNT, MIN, MAX: executes on a group of rows, BUT grouping can cause a partition shuffle, so it can be slow (GROUP BY 1 means group by the first column)
- to_json: converts a struct to a JSON string   i.e. named_struct('DateShipped', ShipDate) as json
- If you want to name a column with a space just use backticks like `column name`
- Different aggregate functions: COUNT, MIN, MAX, STDDEV, AVG, SUM, VARIANCE, SKEWNESS, KURTOSIS, SLOPE, INTERCEPT, CORR
- HAVING is like WHERE but for aggregate functions

### Lesson 16: Window functions
Windows functions operate a set of row and return a single value 
- Similar to an aggregate but not consolidate the results
- The window function is able to access more than just the current row of the query result
- OVER — Identifies the start of a window function block of code. 
- PARTITION – The data grouping.  The window function works within each partition. In the old days, we called this a control-break.
- ORDER BY — Sorts the rows by the specified colmumn which is critical for things like running totals.

```sql
SELECT SalesYear, SalesMonth, TotalSales, Sum(TotalSales) 
  OVER ( PARTITION BY (SalesYear) ORDER BY SalesMonth ROWS BETWEEN unbounded preceding AND CURRENT ROW ) cumsum
FROM v_salessummary
WHERE SalesYear > 2010
```

![alt text](image-5.png)
window framing -> rolling average

UNBOUNDED PRECEDING: from the beginning of the partition
N PRECEDING: N rows before the current row
CURRENT ROW: the current row
UNBOUNDED FOLLOWING: to the end of the partition
N FOLLOWING: N rows after the current row

DEFAULT are ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

Window functions: RANK, DENSE_RANK, ROW_NUMBER, NTILE
```sql
SELECT
  Category,
  Product,
  SalesAmount,
  rank
FROM (
  SELECT
    Category,
    Product,
    SalesAmount,
    dense_rank() OVER (PARTITION BY Category ORDER BY SalesAmount DESC) as rank
  FROM v_productcatalog)
WHERE
  rank <= 2
```
Explaining the query: dense_rank() is a window function that assigns a rank to each row within a partition of a result set, with no gaps in the ranking values. The rank of a specific row is one plus the number of distinct rank values that are less than the rank value of the row itself. 
In this case, we are ranking the products by sales amount within each category. The query returns the top two products in each category.


- NTILE: divides the result set into a specified number of groups, assigning a bucket number to each row (like quartiles) but you can specify the number of buckets

CASTING: CAST(StandardCost as DECIMAL(10,2))

### Lesson 19: PySpark
- PySpark is the Python API for Spark
 ![alt text](image-6.png)
-  RDD to DataFrame , originally RDD was the only way to interact with Spark, but now we have DataFrames, RDD are black box wether DataFrames are more structured and optimized

### Lesson 20: PySpark with RDD
- RDD: Resilient Distributed Dataset, the original way to interact with Spark
- Fault-tolerant, distributed collection of objects
- Immutable, partitioned, and parallel
- Lazy evaluation: transformations are not executed until an action is called
- Actions: collect, count, first, take, reduce, saveAsTextFile