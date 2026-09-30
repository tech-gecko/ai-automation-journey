import requests
from typing import Dict, Optional

def fetch(url: str, params: Optional[Dict[str, str]] = None) -> Dict:
    if params is not None:
        response = requests.get(url, params=params, timeout=10)
    else:
        response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    print("GET PRODUCT(S)")
    print(f'Status: {response.status_code}')
    return data

def create(url: str, payload: Dict, headers: Dict) -> None:
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    print("POST PRODUCT")
    print(f'Status: {response.status_code}')
    print(f'ID: {data["id"]}')
    print(f'Title: {data["title"]}')

def update(url: str, payload: Dict, headers: Dict) -> None:
    response = requests.put(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    print("PUT PRODUCT")
    print(f'Status: {response.status_code}')
    print(f'ID: {data["id"]}')
    print(f'Title: {data["title"]}')
    print(f'Price: {data["price"]}')

def delete(url: str) -> None:
    response = requests.delete(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    print("DELETE PRODUCT")
    print(f'Status: {response.status_code}')
    print(f'Deleted: {data["isDeleted"]}')

def login(url: str, credentials: Dict, headers: Dict) -> str:
    response = requests.post(url, json=credentials, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    return data["accessToken"]

def get_profile(url: str, headers: Dict) -> None:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    print("AUTHENTICATED USER")
    print(f'Status: {response.status_code}')
    print(f'Username: {data["username"]}')
    print(f'Email: {data["email"]}')
