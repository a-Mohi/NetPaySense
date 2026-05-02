import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENCELL_API_KEY")
lat, lon = 12.9716, 77.5946 # Bengaluru

def create_bounding_box(lat, lon, radius_km):
    delta_lat = radius_km / 111
    delta_lon = radius_km / (111 * 0.97) # rough cos(lat)
    return f"{lat - delta_lat},{lon - delta_lon},{lat + delta_lat},{lon + delta_lon}"

params = {
    "key": api_key,
    "BBOX": create_bounding_box(lat, lon, 2),
    "format": "json"
}

print(f"Testing API with key: {api_key}")
try:
    res = requests.get("https://opencellid.org/cell/getInArea", params=params)
    print(f"Status: {res.status_code}")
    print(f"Body: {res.text}")
except Exception as e:
    print(f"Error: {e}")
