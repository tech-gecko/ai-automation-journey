import csv, json
from datetime import datetime
from store_module.utils import product_status, total_inventory_value, find_category, log

STORE_NAME = "TechGecko"
READER = []

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

try:
    inventory = [product1, product2, product3, product4, product5]
    with open("inventory.csv", "w") as file:
        fieldnames = ["name", "category", "price", "quantity"]
        writer =csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    in_stock_products, out_of_stock_products, low_stock_products = [], [], []
    item_sum = 0
    total_price = 0

    def store_summary():
        print("===== SUMMARY =====")
        print()
        print(f'In-stock products: {[product["name"] for product in in_stock_products]}')
        print(f'Out-of-stock products: {[product["name"] for product in out_of_stock_products]}')
        print(f'Low-stock products: {[product["name"] for product in low_stock_products]}')
        print()

        with open("inventory.csv", "r") as file:
            reader = csv.DictReader(file)
            for product in reader:
                READER.append(product)
                print(f'{product["name"]} -> {product["quantity"]}')
            
        print()
        print(f'Total items in stock: {item_sum}')
        print(f'Total expected revenue: {total_price:.2f}')
        print(f'Average revenue per item: {total_price / item_sum}')

    print(f'===== {STORE_NAME.upper()} INVENTORY REPORT =====')
    print()

    with open("inventory.json", "r") as file:
        json_inventory = json.load(file)

    for product in json_inventory:
        if product["quantity"] > 3:
            in_stock_products.append(product)
        elif product["quantity"] <= 0:
            out_of_stock_products.append(product)
        else:
            low_stock_products.append(product)

        print(f'Product: {product["name"]}')
        print(f'Category: {find_category(product)}')
        print(f'Price: {product["price"]}')
        print(f'Quantity: {product["quantity"]}')
        item_sum += product["quantity"]
        inventory_value = total_inventory_value(product["price"], product["quantity"])
        total_price += inventory_value
        print(f'Status: {product_status(product)}')
        print(f'Inventory Value: {inventory_value:.2f}')
        print()

    store_summary()

except KeyError as e:
    print(str(e))
    log(f"[{datetime.now()}] {str(e)}.")
except TypeError as e:
    print(str(e))
    log(f"[{datetime.now()}] {str(e)}.")
except ZeroDivisionError as e:
    print(f'Error encountered while dividing Total Revenue: {total_price} by Total Items in Stock: {item_sum}')
    print(str(e))
    log(f"[{datetime.now()}] {str(e)}.")
except Exception as e:
    print(str(e))
    log(f"[{datetime.now()}] {str(e)}.")
else:
    print()
    print("===== DATA EXPORT SUMMARY =====")
    print()
    print("CSV export: Successful")
    print("JSON export: Successful")
    print()
    print(f"CSV records loaded: {len(READER)}")
    print(f"JSON records loaded: {len(json_inventory)}")
    log(f"[{datetime.now()}] TechGecko inventory report generated successfully.")
finally:
    print()
    print("Program is no longer running.")
