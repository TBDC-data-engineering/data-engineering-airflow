# file sensor
# checks the existense of a file
# external task sensor, https sensor etc
# why sensor
# for check a condition and not fail the complete dag

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

report_dag = DAG(
    dag_id = 'execute_report',
    schedule_interval = "0 0 * * *"
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2024,1,20),
    mode='poke',
    dag=report_dag
)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2024,1,20),
    dag=report_dag
)

precheck >> generate_report_task
