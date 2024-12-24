import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

# Simulate or use an actual API endpoint for fetching real-time market prices
api_url = "https://marsapi.ams.usda.gov/services/v1.2/reports/1095"

response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})
print(response.status_code)

# Process response data (simulate response if no actual API)
if response.status_code == 200:
    price_data = response.json()  # Extract price information
    print(price_data)
