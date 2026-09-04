import os

import requests
from dotenv import load_dotenv


load_dotenv()

api_url = os.getenv("FLIGHTRADAR_API_URL")
api_token = os.getenv("FLIGHTRADAR_API_TOKEN")

if not api_url or not api_token:
    raise RuntimeError("Faltan FLIGHTRADAR_API_URL o FLIGHTRADAR_API_TOKEN en .env")

headers = {
    "Authorization": f"Bearer {api_token}",
    "Accept": "application/json",
    "Accept-Version": "v1"
}

response = requests.get(api_url, headers=headers, timeout=30)

print(f"Código HTTP: {response.status_code}")
print(response.text)