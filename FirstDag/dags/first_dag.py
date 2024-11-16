from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def process_data():
    print("Processing data...")

with DAG(
    dag_id='simple_dag',
    default_args={
        'owner': 'vitor',
        'retries': 1,
    },
    description='A simple DAG example',
    schedule='@daily',  # Updated to `schedule`
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    start = EmptyOperator(task_id='start')
    process = PythonOperator(task_id='process', python_callable=process_data)
    end = EmptyOperator(task_id='end')

    start >> process >> end
