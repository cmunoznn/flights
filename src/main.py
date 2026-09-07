
"""Santiago - NewYork Flight activity"""

import os
import requests
from dotenv import load_dotenv
import pandas as pd

def execute_pipeline():

    load_dotenv()

    try:

        """getting the API URL and token from the environment variables"""

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

        print(f"Código HTTP: {response.status_code}")
        response.raise_for_status()
        result = response.json()
        print(f"Resultado: {result}")

        """Taking the data from the API response and creating a DataFrame"""
            
        df = pd.DataFrame(result["data"])

        if len(df) == 0:
            raise RuntimeError("No results found in the API response")

        print(df.iloc[0,1])  # Print the first row of the DataFrame

        for columns in df.columns:
            for rows in df.index:
                print(f"{columns}: {df.at[rows, columns]}")


    except Exception as e:
        print(f"*******ERROR*******: {e}")   


if __name__ == "__main__":
    execute_pipeline()