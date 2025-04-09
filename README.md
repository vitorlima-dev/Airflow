# Airflow with Docker Compose

This repository sets up a complete environment for **Apache Airflow**, using **PostgreSQL** as the backend database and **MinIO** for data storage. With Docker Compose, this setup makes it easy to configure and run Airflow in an isolated and practical way.

## Components

- **PostgreSQL**: Used as the backend database to store task states and DAGs in Airflow.
- **Airflow**: The main application for orchestrating workflows (DAGs).
- **MinIO**: An object storage solution compatible with S3, used to store data and files in Airflow.

## Prerequisites

- **Docker** and **Docker Compose** installed on your machine.
  - [Install Docker](https://docs.docker.com/get-docker/)
  - [Install Docker Compose](https://docs.docker.com/compose/install/)

## How to Use

1. **Clone the repository**:

    ```bash
    git clone https://github.com/vitorlima-dev/Airflow.git
    cd Airflow
    ```

2. **Create the containers and start the services**:

    Run the following command to start all Docker containers defined in the `docker-compose.yml` file:

    ```bash
    docker-compose up -d
    ```

    This command will:

    - Download the necessary Docker images (PostgreSQL, Airflow, MinIO).
    - Create the containers and configure them to run in the background.

3. **Accessing the Airflow interface**:

    After the containers are initialized, you can access the Airflow web interface at [http://localhost:8080](http://localhost:8080) in your browser.

    - **Default username**: `airflow`
    - **Default password**: `airflow`

4. **Accessing MinIO**:

    You can access the MinIO web interface at [http://localhost:9001](http://localhost:9001) with the following credentials:

    - **Username**: `minio`
    - **Password**: `minio`

5. **Stopping the containers**:

    To stop all containers, run:

    ```bash
    docker-compose down
    ```

## Project Structure

- `airflow-setup/`: Contains Airflow configuration, including the `Dockerfile` and the `airflow.cfg` configuration file.
- `dags/`: Directory where the Airflow DAG files will be stored.
- `docker-compose.yml`: Docker Compose configuration file that defines all required services.

## Volumes

This setup uses volumes for data persistence:

- **postgres-db-volume**: Stores the PostgreSQL database data.
- **minio-storage-volume**: Stores MinIO data.

## Customizations

- If you need to customize Airflow, you can edit the `airflow.cfg` file located in the `./airflow-setup/` directory.
- DAGs can be added directly to the `./dags/` directory.

## Considerations

- Airflow is configured to run in isolation with a PostgreSQL database and MinIO for file storage.
- The initial database setup for Airflow will be done automatically using the `_AIRFLOW_DB_UPGRADE: 'true'` environment variable.
