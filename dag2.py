from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

default_args={
    'email': ['airflowalerts@datacamp.com', 'airflowadmin@datacamp.com'],
    'email_on_failure': True,
    'email_on_success': True
}

report_dag = DAG(
    dag_id = 'execute_report',
    schedule_interval = "0 0 * * *",
    default_args=default_args
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2023,2,20),
    mode='reschedule',
    dag=report_dag)

generate_report_task = BashOperator(
    task_id='generate_report',
    bash_command='generate_report.sh',
    start_date=datetime(2023,2,20),
    dag=report_dag
)

precheck >> generate_report_task