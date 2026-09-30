from api_client.api import create, fetch, update, delete, login, get_profile
import requests

url1 = "https://dummyjson.com/products/1"
url2 = "https://dummyjson.com/products"
url3 = "https://dummyjson.com/products/add"
url4 = "https://dummyjson.com/auth/login"
url5 = "https://dummyjson.com/auth/me"

try:
    data = fetch(url1)

    print(f'Title: {data["title"]}')
    print(f'Price: {data["price"]}')
    print(f'Stock: {data["stock"]}')

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print("API request failed: ", str(e))
except Exception as e:
    print("API request failed: ", str(e))

try:
    params = {
        "select": ["title", "price", "stock"],
        "sortBy": "price",
        "order": "desc"
    }
    print()
    data = fetch(url2, params=params)

    for product in data["products"]:
        print(f'- {product["title"]}:\n    Price: ${product["price"]} ({product["stock"]} left).')

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print("API request failed: ", str(e))
except Exception as e:
    print("API request failed: ", str(e))

try:
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "title": "TechGecko Power Bank",
        "price": 25000,
        "stock": 10,
        "category": "phone-accessories"
    }
    print()
    create(url3, payload, headers)

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print("API request failed: ", str(e))
except Exception as e:
    print("API request failed: ", str(e))

try:
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "title": "TechGecko Power Tank",
        "price": 350000,
    }
    print()
    update(url1, payload, headers)

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print("API request failed: ", str(e))
except Exception as e:
    print("API request failed: ", str(e))

try:
    print()
    delete(url1)

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print("API request failed: ", str(e))
except Exception as e:
    print("API request failed: ", str(e))

try:
    credentials = {
        "username": "emilys",
        "password": "emilyspass"
    }
    headers = {"Content-Type": "application/json"}

    token = login(url4, credentials=credentials, headers=headers)

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print("API request failed: ", str(e))
except Exception as e:
    print("API request failed: ", str(e))

try:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    print()
    get_profile(url5, headers=headers)

except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print("API request failed: ", str(e))
except Exception as e:
    print("API request failed: ", str(e))
