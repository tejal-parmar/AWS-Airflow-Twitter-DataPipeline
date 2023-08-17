# twitter-airflow-aws-datapipeline
End-to-end Data Engineering project to extract data using Twitter API, transform data using Python, deploy the code on Airflow/EC2 and save final result on Amazon S3.

Extracting data from Twitter
API credentials from Twitter Development platform
Tweepy - An easy-to-use Python library for accessing the Twitter API.

Pandas - to work with the data and transform the data

Apache Airflow - deploy the code onto airflow, an open source workflow management platform for data engineering pipelines. It is  workflow orchestration tool to build, schedule, monitor data pipelines. Workflow is sequence of every task, in Airflow it is defined as Directed Cyclic Graph (DAG).(sequence of operations is called DAG). 
Airflow contains multiple DAGs, and each DAG can contain multiple tasks, task is the unit of operation.
Different tasks can be built using operators, operators are predefined template used to creat task.
Airflow has many different operators 
i.e., 
airflow.operators.bash - to run bash command
airflow.operators.python - to run python code
custom operators can be created as well.
Task 1 - Extract data from API
Task 2 - Transform data
Task 3 - Store data




