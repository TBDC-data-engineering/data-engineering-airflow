# data-engineering-airflow


DAG - Directed Acyclic Graph

DAG composed of Tasks

Testing a task in Airflow

## Airflow Operatos

Operator - represent a single task in a workflow

run independently 
not change info among them (operators)

airflow contain many

## Tasks

Tasks are instances of operators, usually assigned to a variable in Python

Tasks dependencies define a given order of task completion


``` bash
 
airflow tasks test etl_pipeline download_file 2023-01-08
```