from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="demo",
    catchup=False,
    start_date=datetime(2022, 1, 1),
    schedule="0 0 * * *"  # Executa todos os dias à meia-noite
) as dag:

    # Tarefas representadas por operadores
    hello = BashOperator(task_id="hello", bash_command="echo hello")
    airflow = BashOperator(task_id="airflow", bash_command="echo airflow")

    # Definindo dependências entre as tarefas
    hello >> airflow  # A tarefa 'airflow' será executada após a 'hello'