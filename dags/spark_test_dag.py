from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

with DAG(
    dag_id='weather_spark_pipeline',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    # One task to rule them all: Memory limits + Postgres Driver
    run_weather_job = SparkSubmitOperator(
        task_id='run_weather_transform',
        application='/opt/airflow/data/process_weather.py',
        conn_id='spark_default',
        # Combine all your configurations here
        conf={
            "spark.driver.bindAddress": "0.0.0.0",
            "spark.executor.memory": "512m",
            "spark.driver.memory": "512m",
            "spark.executor.cores": "1",
            "spark.jars.packages": "org.postgresql:postgresql:42.5.0" # Driver included!
        },
        # Using 'packages' directly is also a safe backup
        packages="org.postgresql:postgresql:42.5.0", 
        verbose=True
    )