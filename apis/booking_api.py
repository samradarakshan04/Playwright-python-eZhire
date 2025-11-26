import requests

BASE_URL = "https://api.ezhire.me"

def get_latest_booking():
    response = requests.get(f"{BASE_URL}/bookings/latest")
    response.raise_for_status()
    return response.json()

def create_booking(data):
    response = requests.post(f"{BASE_URL}/bookings", json=data)
    response.raise_for_status()
    return response.json()
