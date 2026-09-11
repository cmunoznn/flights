###V1.  Flight extraction and processing DAG for Airflow

import sys
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator


sys.path.insert(0, "/opt/airflow/flights")


def flights_extraction() -> None:

    #Pipeline execution function for Airflow DAG

    from src.main import execute_pipeline
    execute_pipeline()


with DAG(
    dag_id="flights_api_pipeline",
    start_date=pendulum.datetime(2026, 1, 1, 19, tz="America/Santiago"),
    schedule="0 1,7,13,19 * * *",
    catchup=False,
    tags=["flights", "api"],
) as dag:
    GetSCLJFKFlights = PythonOperator(
        task_id="GetSCLJFKFlights",
        python_callable=flights_extraction,
    )
