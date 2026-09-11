
###V1. Register Santiago - NewYork Flight activity ###

import os
import requests
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def save_flights(df: pd.DataFrame) -> None:

    #Getting the database connection parameters from the environment variables

    required_database_values = [
        os.getenv("POSTGRES_USER"),
        os.getenv("POSTGRES_PASSWORD"),
        os.getenv("POSTGRES_DB"),
    ]
    if all(required_database_values):
        
        database_url = URL.create(
            "postgresql+psycopg2",
            username=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=int(os.getenv("POSTGRES_PORT", "5432")),
            database=os.getenv("POSTGRES_DB"),
        )
    else:
        raise RuntimeError(
            "Define POSTGRES_USER, POSTGRES_PASSWORD and POSTGRES_DB in .env"
        )

    #adding a timestamp to the DataFrame to record when the data was retrieved (Santiago timezone)

    df["recorded_at"] = pd.Timestamp.now(tz="America/Santiago")

    engine = create_engine(database_url)

    try:
        #append the records to the flights table in the bronze schema of the PostgreSQL database
        df.to_sql(
            "flights",
            engine,
            schema="bronze",
            if_exists="append",
            index=False,
            method="multi",
        )

    finally:
        engine.dispose()

def execute_pipeline(): 

    load_dotenv()

    try:

        #Getting the API URL and token from the environment variables

        api_url = os.getenv("FLIGHTRADAR_API_URL")
        api_token = os.getenv("FLIGHTRADAR_API_TOKEN")

        if not api_url or not api_token:
            raise RuntimeError("Missing FLIGHTRADAR_API_URL or FLIGHTRADAR_API_TOKEN in .env")

        headers = {
            "Authorization": f"Bearer {api_token}",
            "Accept": "application/json",
            "Accept-Version": "v1"
        }

        response = requests.get(api_url, headers=headers, timeout=30)

        #For logging purposes, printing the HTTP status code and the API response

        print(f"Código HTTP: {response.status_code}")
        response.raise_for_status()
        result = response.json()
        print(f"Resultado: {result}")

        #Taking the data from the API response and creating a DataFrame
            
        df = pd.DataFrame(result["data"])

        if len(df) == 0:
            raise RuntimeError("No results found in the API response")

        #Append the API records to the PostgreSQL flights table.

        save_flights(df)
         
    except Exception as e:
        print(f"*******ERROR*******: {e}")   


if __name__ == "__main__":
    execute_pipeline()