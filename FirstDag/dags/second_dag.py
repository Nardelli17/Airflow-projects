from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.utils.helpers import chain

def print_a():
    print("Task a")
    
def print_b():
    print("Task b")

def print_c():
    print("Task c")

def print_d():
    print("Task d")
    
def print_e():
    print("Task e")

with DAG(
    dag_id='second_dag',
    default_args={
        'owner': 'vitor',
        'retries': 1,
    },
    description='Other simple DAG example',
    tags=['examples'],
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False):
        
    task_a = PythonOperator(task_id='task_a', python_callable=print_a)
    task_b = PythonOperator(task_id='task_b', python_callable=print_b)
    task_c = PythonOperator(task_id='task_c', python_callable=print_c)
    task_d = PythonOperator(task_id='task_d', python_callable=print_d)
    task_e = PythonOperator(task_id='task_e', python_callable=print_e)
    
    chain (task_a , [task_b, task_c], [task_d, task_e])
