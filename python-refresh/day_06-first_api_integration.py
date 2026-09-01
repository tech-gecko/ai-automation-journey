from datetime import datetime
import requests

url1 = "https://dummyjson.com/products/1"
url2 = "https://dummyjson.com/products"
url3 = "https://dummyjson.com/products/add"
params = {
    "select": ["title", "price"],
    "sortBy": "price",
    "order": "desc"
}
payload = {
    "title": "Essence Mascara Lash Princess",
    "description": "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.",
    "category": "beauty",
    "price": 9.99,
    "discountPercentage": 7.17,
    "rating": 4.94,
    "stock": 5
}
headers = {
    "Content-Type": "application/json"
}

try:
    response1 = requests.get(url1)
    print(response1.status_code)
    response1.raise_for_status()
    product1 = response1.json()
    print()
    print(f'Product: {product1["title"]}')
    print(f'Price: ${product1["price"]}')
    print(f'Category: {product1["category"]}')
    print()

    response2 = requests.get(url2, params=params)
    print(response2.status_code)
    response2.raise_for_status()
    product_list = response2.json()["products"]
    for product2 in product_list:
        print(f'{product2["title"]}: ${product2["price"]}')
    print()

    response3 = requests.post(url3, json=payload)
    print(response3.status_code)
    response3.raise_for_status()
    product3 = response3.json()
    for key, value in product3.items():
        print(f'{key}: {value}')
    print()

    url4 = f'https://dummyjson.com/products/1'
    response4 = requests.delete(url4, headers=headers)
    print(response4.status_code)
    response4.raise_for_status()
    product4 = response4.json()
    if product4["isDeleted"]:
        iso_deleted_time = product4["deletedOn"].replace("Z", "+00:00")
        print("Deleted successfully on ", datetime.fromisoformat(iso_deleted_time).strftime("%B %d, %Y at %I:%M %p"))
except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.RequestException as e:
    print("API request failed: ", str(e))
except Exception as e:
    print("Error: ", str(e))
else:
    print()
    print("API processing completed.")
