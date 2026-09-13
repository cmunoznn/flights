# Flight Data Pipeline

Hello!!, in this data engineering project I'm playing around with flights.  I have several ideas to continue but for now let me show you what's done so far:

1) I'm interested in knowing more about a specific flight route, considering those flights departing from Santiago (SCL) to New York (JFK). So I'm getting the live info through the flightradar24 API.
   
2) I read the API every 1 hour using an Airflow DAG.  The response data is recorded in a Postgres table in my bronze medallion for further review.

3) To be continued.... (feel free to suggest any idea!)  --> Contact me at cmunoznn@gmail.com

## Technical Overview

I'm locally using Airflow/Postgres containers, VSC as editor, GitH Copilot, and some well known python libraries.


## Tech Stack

- Python
- Pandas
- SQL
- PostgreSQL
- Apache Airflow
- Docker
- SQLAlchemy
- Flightradar24 API

## Project Structure

```text
flights/
├── airflow/
│   └── dags/
│       └── flights_dag.py
├── data/
│   ├── raw/
│   └── processed/
├── data_scripts/
│   └── 01-TableCreation.sql
├── src/
│   └── main.py
├── tests/
├── requirements.txt
└── .env
```

## Configuration

The project use the ".env" configuration file containing the followings variables:

```env
FLIGHTRADAR_API_URL=https://fr24api.flightradar24.com/api/live/flight-positions/full?routes=SCL-JFK&categories=P
FLIGHTRADAR_API_TOKEN=Your_token (you can get a sandbox token from https://fr24api.flightradar24.com using the basic pricing plan)

POSTGRES_USER=airflow
POSTGRES_PASSWORD=tu_password
POSTGRES_HOST=localhost (Used when you execute the code directly from VSC)
POSTGRES_PORT=5432
POSTGRES_DB=flights
```

```env
POSTGRES_HOST=postgres (Used when the code runs inside Docker and Airflow & PostgreSQL belong to the same compose)
```

## Local Installation

Create and activate a virtual environment:

python -m venv .venv

On Windows:

.venv\Scripts\Activate.ps1

## Install the dependencies:

pip install -r requirements.txt
Manual Execution

Run the pipeline with:

python src/main.py

## The process:

- Queries the Flightradar24 API.
- Converts the response into a DataFrame.
- Adds the recorded_at column.
- Inserts the records into PostgreSQL.
- Stores the data in the bronze schema, in the flights table.
- Execution with Airflow

## Start the containers:

cd airflow
docker compose up -d

The DAG is located at:

airflow/dags/flights_dag.py

It currently runs every hour:

schedule="0 * * * *"

The Airflow web interface is available at:

http://localhost:8080

## Database

The table used by the pipeline is:

bronze.flights

The initial table structure can be found in:

data_scripts/01-TableCreation.sql

## "Very Simple" Query Example showing the table:

SELECT *
FROM bronze.flights
ORDER BY recorded_at DESC;

## Considerations

- A valid Flightradar24 token is required.
- PostgreSQL must be available before running the pipeline.
- Credentials should be kept outside the repository (.env)
- The DAG schedule uses the time zone configured in Airflow.

## Project Status

Open to new ideas regarding the following topics or others:

- API consumption.
- Data processing with Pandas.
- Data persistence in PostgreSQL.
- Orchestration with Apache Airflow.
- Containerization with Docker.
- SQL Aggregation, CTEs
- Etc.
