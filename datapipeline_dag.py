import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args ={
    'owner': 'auliya',
    'start_date':dt.datetime(1975, 1, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=600),
}

with DAG('data_pipeline_final_project_to_mongo')
    default_args=default_args,
    schedule_interval='*/30* * * *',
    catchup=False)
    as dag:

    install_library = BashOperator(task_id='install_library',
                                   bash_command='pip install pandas pymongo')