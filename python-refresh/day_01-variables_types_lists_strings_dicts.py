store_name = "TechGecko"

product1 = {
    "name": "Earbuds",
    "category": "Phone accessories",
    "price": 10000,
    "quantity": 5,
    "available": True
}

product2 = {
    "name": "Power Bank",
    "category": "Phone accessories",
    "price": 20000,
    "quantity": 3,
    "available": True
}

product3 = {
    "name": "iPhone 17 Pro Max",
    "category": "Phones",
    "price": 1400000,
    "quantity": 0,
    "available": False
}

inventory = [product1, product2, product3]

"""
def available(dic: dict):
    return "Yes" if dic.get("available") else "No"
"""

print(f'Store: {store_name}')
print()

print(f'Product: {product1["name"]}')
print(f'Category: {product1["category"]}')
print(f'Price: {product1["price"]}')
print(f'Quantity: {product1["quantity"]}')
print(f'Available: {"Yes" if product1["available"] else "No"}')
print()

print(f'Product: {product2["name"]}')
print(f'Category: {product2["category"]}')
print(f'Price: {product2["price"]}')
print(f'Quantity: {product2["quantity"]}')
print(f'Available: {"Yes" if product2["available"] else "No"}')
print()

print(f'Product: {product3["name"]}')
print(f'Category: {product3["category"]}')
print(f'Price: {product3["price"]}')
print(f'Quantity: {product3["quantity"]}')
print(f'Available: {"Yes" if product3["available"] else "No"}')
