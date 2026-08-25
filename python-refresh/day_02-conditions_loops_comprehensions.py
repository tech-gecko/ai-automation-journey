store_name = "TechGecko"

product1 = {
    "name": "Earbuds",
    "category": "Phone accessories",
    "price": 10000,
    "quantity": 5
}

product2 = {
    "name": "Power Bank",
    "category": "Phone accessories",
    "price": 20000,
    "quantity": 4
}

product3 = {
    "name": "iPhone 17 Pro Max",
    "category": "Phones",
    "price": 1400000,
    "quantity": 2
}

product4 = {
    "name": "iTel Power Tank",
    "category": "Power stations",
    "price": 340000,
    "quantity": 0
}

product5 = {
    "name": "Dell Latitude 5420",
    "category": "Laptops",
    "price": 400000,
    "quantity": 1
}

inventory = [product1, product2, product3, product4, product5]
in_stock_products = [product for product in inventory if product["quantity"] > 3]
out_of_stock_products = [product for product in inventory if product["quantity"] <= 0]
low_stock_products = [product for product in inventory if product["quantity"] > 0 and product["quantity"] <= 3]


"""
def available(dic: dict):
    return "Yes" if dic.get("available") else "No"
"""

print(f'===== {store_name.upper()} INVENTORY REPORT =====')
print()

for product in inventory:
    print(f'Product: {product["name"]}')
    print(f'Category: {product["category"]}')
    print(f'Price: {product["price"]}')
    print(f'Quantity: {product["quantity"]}')
    print(f'Status: {"In Stock" if product in in_stock_products else "Out of Stock" if product in out_of_stock_products else "Low Stock"}')
    print()

print("===== SUMMARY =====")
print()
print(f'In-stock products: {[product["name"] for product in in_stock_products]}')
print(f'Out-of-stock products: {[product["name"] for product in out_of_stock_products]}')
print(f'Low-stock products: {[product["name"] for product in low_stock_products]}')
