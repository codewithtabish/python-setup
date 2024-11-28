import requests

API_KEY = "3c78e1e183eb5fe132da9af9e1d267f0"
BASE_URL = "http://api.exchangeratesapi.io/v1/latest"

def get_conversion_rate_utils():
    url = f"{BASE_URL}?access_key={API_KEY}&format=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
