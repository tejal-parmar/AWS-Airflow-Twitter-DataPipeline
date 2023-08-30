# AWS-Airflow-Twitter-DataPipeline
End-to-end Data Engineering project
  - Task1 - Extract data from Twitter API using tweepy
  - Task2 - Transform data using Python pandas
  - Task3 - Deploy the code on Airflow/EC2
  - Task4 - Save data in AWS S3 bucket

## Workflow
![DataPipeline](https://github.com/tejal-parmar/AWS-Airflow-Twitter-DataPipeline/assets/111147531/8c7d5641-dddf-423e-a26d-3449c2c83408)

Extracting data from Twitter
  - API credentials from Twitter Development platform

Python libraries
  - Tweepy: An easy-to-use Python library for accessing the Twitter API.
  - Pandas: to work with the data and transform the data

Apache Airflow
  - Deploy the code onto airflow,
  - An open source workflow management platform for data engineering pipelines.
  - It is  workflow orchestration tool to build, schedule, monitor data pipelines.
  - Workflow is sequence of every task, in Airflow it is defined as Directed Cyclic Graph (DAG).(sequence of operations is called DAG).
  - Airflow contains multiple DAGs, and each DAG can contain multiple tasks, task is the unit of operation.
  - Different tasks can be built using operators, operators are predefined template used to creat task.
  - Airflow has many different operators, i.e.,
     - airflow.operators.bash-> to run bash commands,
     - airflow.operators.python-> to run python code,
     - custom operators can be created as well.
