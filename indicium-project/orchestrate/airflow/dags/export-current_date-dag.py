from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

default_args = {
    'owner': 'madruga',
    'retries': '5',
    'retry_delay': timedelta(minutes=2)

}

with DAG(
    dag_id='step_2',
    description='runs bash command to export current_time from local system',
    start_date=datetime.now(),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='export_current_date',
        bash_command="export CURRENT_DATE=$(date +'%Y-%m-%d')"
    )
    task2 = TriggerDagRunOperator (
        task_id = 'trigger_dag',
        trigger_dag_id = 'meltano_step_2_dag_step-2-exec-write-db'
    )