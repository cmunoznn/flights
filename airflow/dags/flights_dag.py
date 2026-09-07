"""Flight extraction and processing DAG for Airflow"""

import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


sys.path.insert(0, "/opt/airflow/flights")


def flights_extraction() -> None:
    """Pipeline execution function for Airflow DAG"""
    from src.main import execute_pipeline
    execute_pipeline()


with DAG(
    dag_id="flights_api_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="*/5 * * * *",
    catchup=False,
    tags=["flights", "api"],
) as dag:
    GetSCL-JFK-Flights = PythonOperator(
        task_id="Get and Process SCL-JFK Flights",
        python_callable=flights_extraction,
    )
