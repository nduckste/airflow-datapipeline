import sys
sys.path.append("..")
sys.path.append("/home/centos/airflow-datapipeline/core/")
sys.path.append("/home/centos/airflow-datapipeline/config/")
sys.path.append("/home/centos/airflow-datapipeline/Movie/")
sys.path.append("/home/centos/airflow-datapipeline/utils/")
sys.path.append("/home/centos/airflow-datapipeline/")

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from utils.db import create_connection_object
from ..core.execute import core_aggregation, core_db_insert_to_db, core_get_data



SCHEDULE_INTERVAL = '@hourly'

DB_CONN = create_connection_object('postgres_default')

default_args = {
    'owner': 'Business Intelligence',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 16),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

DAG_VERSION = 'MovieRatings.0'

dag = DAG(DAG_VERSION
          ,  default_args=default_args
          ,  schedule_interval=SCHEDULE_INTERVAL
          ,  concurrency=1
          ,  max_active_runs=1)


get_data = PythonOperator(
    task_id='get_data',
    python_callable=core_get_data,
    retries=0,
    provide_context=True,
    dag=dag
)


aggregation = PythonOperator(
    task_id='aggregation',
    python_callable=core_aggregation,
    retries=0,
    provide_context=True,
    dag=dag
)


db_insert_to_db = PythonOperator(
    task_id='db_insert_to_db',
    python_callable=core_db_insert_to_db,
    op_args=[DB_CONN],
    retries=0,
    provide_context=True,
    dag=dag
)

get_data >> aggregation >> db_insert_to_db