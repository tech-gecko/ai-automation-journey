from datetime import datetime
import requests
from product_report.utils import log

def fetch(url: str) -> requests.Response:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response
    except requests.exceptions.Timeout:
        print("Request timed out.")
        log(f"[{datetime.now()}] Request timed out.")
        raise
    except requests.exceptions.RequestException as e:
        print("API request failed: ", str(e))
        log(f"[{datetime.now()}] API request failed: {str(e)}.")
        raise
    except Exception as e:
        print("Error: ", str(e))
        log(f"[{datetime.now()}] {str(e)}.")
        raise
