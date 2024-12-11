# Airflow com Docker Compose

Este repositório configura um ambiente completo para o **Apache Airflow**, com **PostgreSQL** como banco de dados backend e **MinIO** para armazenamento de dados. Utilizando o Docker Compose, este setup facilita a configuração e a execução do Airflow de forma isolada e prática.

## Componentes

- **PostgreSQL**: Usado como banco de dados backend para armazenar o estado das tarefas e DAGs no Airflow.
- **Airflow**: A aplicação principal para orquestração de fluxos de trabalho (DAGs).
- **MinIO**: Solução de armazenamento de objetos compatível com o S3, usada para armazenar dados e arquivos no Airflow.

## Pré-requisitos

- **Docker** e **Docker Compose** instalados na sua máquina.

    - [Instalar Docker](https://docs.docker.com/get-docker/)
    - [Instalar Docker Compose](https://docs.docker.com/compose/install/)

## Como usar

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/vitorlima-dev/Airflow.git
    cd Airflow
    ```

2. **Crie os containers e inicie os serviços**:

    Execute o comando abaixo para iniciar todos os containers do Docker definidos no arquivo `docker-compose.yml`:

    ```bash
    docker-compose up -d
    ```

    O comando irá:

    - Baixar as imagens do Docker necessárias (PostgreSQL, Airflow, MinIO).
    - Criar os containers e configurá-los para rodar em segundo plano.

3. **Acessando a interface do Airflow**:

    Após os containers serem inicializados, você pode acessar a interface web do Airflow em [http://localhost:8080](http://localhost:8080) no seu navegador.

    - **Usuário padrão**: `airflow`
    - **Senha padrão**: `airflow`

4. **Acessando o MinIO**:

    Você pode acessar a interface do MinIO em [http://localhost:9001](http://localhost:9001) com as credenciais:

    - **Usuário**: `minio`
    - **Senha**: `minio`

5. **Parar os containers**:

    Para parar todos os containers, execute:

    ```bash
    docker-compose down
    ```

## Estrutura do projeto

- `airflow-setup/`: Contém a configuração do Airflow, incluindo o arquivo `Dockerfile` e o arquivo de configuração `airflow.cfg`.
- `dags/`: Diretório onde os arquivos DAGs do Airflow serão armazenados.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose que define todos os serviços necessários.

## Volumes

Este setup utiliza volumes para persistência de dados:

- **postgres-db-volume**: Armazena os dados do banco de dados PostgreSQL.
- **minio-storage-volume**: Armazena os dados do MinIO.

## Customizações

- Se precisar de customizações no Airflow, você pode editar o arquivo `airflow.cfg` localizado no diretório `./airflow-setup/`.
- Os DAGs podem ser adicionados diretamente no diretório `./dags/`.

## Considerações

- O Airflow é configurado para rodar de forma isolada com uma base de dados PostgreSQL e MinIO para armazenar arquivos.
- A configuração inicial do banco de dados Airflow será feita automaticamente com a variável `_AIRFLOW_DB_UPGRADE: 'true'`.
