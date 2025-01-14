import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHIP24_API_KEY = os.getenv("SHIP24_API_KEY")

headers = {
    'Authorization': SHIP24_API_KEY,
    'Content-Type': 'application/json; charset=utf-8'
}


def create_tracker(tracking_id: str) -> dict:
    """
    Creates a tracker for the specified tracking number.
    Returns tracker data or an error if the creation fails.

    Args:
        tracking_id (str): The tracking number to create a tracker for.

    Returns:
        dict: A dictionary containing either the tracker data or an error.
    """
    url = "https://api.ship24.com/public/v1/trackers"
    payload = {"trackingNumber": tracking_id}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        tracking_data = response.json()
        return {"success": True, "data": tracking_data}
    else:
        return {
            "success": False,
            "status_code": response.status_code,
            "error": response.json(),
        }


def track_package(tracking_id: str) -> dict:
    """
    Tracks a package using the specified tracking number.
    Returns package tracking data or an error if tracking fails.

    Args:
        tracking_id (str): The tracking number to fetch tracking details for.

    Returns:
        dict: A dictionary containing either the tracking data or an error.
    """
    url = f"https://api.ship24.com/public/v1/trackers/search/{tracking_id}/results"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tracking_data = response.json()
        return {"success": True, "data": tracking_data}
    elif response.status_code == 404:
        return {
            "success": False,
            "status_code": response.status_code,
            "error": response.json(),
        }
    else:
        return {
            "success": False,
            "status_code": response.status_code,
            "error": response.json(),
        }
