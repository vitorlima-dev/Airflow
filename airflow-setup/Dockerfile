FROM apache/airflow:2.9.2

COPY requirements.txt /
COPY airflow.cfg /opt/airflow/airflow.cfg
RUN pip install --no-cache-dir -r /requirements.txt

USER airflow