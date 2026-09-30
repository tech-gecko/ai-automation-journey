import csv, json
from datetime import datetime
from product_report.utils import log
from requests import Response
from typing import Dict, List, Literal, TypedDict

class ProductDict(TypedDict):
    """Structure of a processed product."""

    title: str
    category: str
    price: float
    stock: int
    rating: float
    stock_status: str
    priority: str

class InventoryResult(TypedDict):
    """Structure of the complete inventory processing result."""

    data: List[ProductDict]
    product_count: int
    in_stock_count: int
    low_stock_count: int
    out_of_stock_count: int
    total_rating: float
    needs_attention: int
    inventory_value: float

def process_json(response: Response) -> InventoryResult:
    data = []
    product_count = 0
    in_stock_count = 0
    low_stock_count = 0
    out_of_stock_count = 0
    total_rating = 0
    needs_attention = 0
    inventory_value = 0

    try:
        product_list = response.json()["products"]

        for product in product_list:
            if product["stock"] > 5:
                in_stock_count += 1
            elif product["stock"] <= 0:
                out_of_stock_count += 1
            else:
                low_stock_count += 1
            
            if product["stock"] <= 5 and product["rating"] >= 4.5:
                needs_attention += 1

            product_dict = {
                "title": product["title"],
                "category": product["category"],
                "price": product["price"],
                "stock": product["stock"],
                "rating": product["rating"],
                "stock_status": "In Stock" if product["stock"] > 5 else "Out of Stock" if product["stock"] <= 0 else "Low Stock",
                "priority": "Needs ATTENTION" if product["stock"] <= 5 and product["rating"] >= 4.5 else "Normal"
            }
            data.append(product_dict)
            product_count += 1
            total_rating += product["rating"]
            inventory_value += product["stock"] * product["price"]

        return {
            "data": data,
            "product_count": product_count,
            "in_stock_count": in_stock_count,
            "low_stock_count": low_stock_count,
            "out_of_stock_count": out_of_stock_count,
            "total_rating": total_rating,
            "needs_attention": needs_attention,
            "inventory_value": inventory_value
        }
    except Exception as e:
        print("ERROR: ", str(e))
        log(f"[{datetime.now()}] {str(e)}.")
        raise

def generate_report(data: List[ProductDict], file_format: Literal["csv", "json"]):
    if file_format == "csv":
        with open("product_report.csv", "w") as file:
            fieldnames = ["title", "category", "price", "stock", "rating", "stock_status", "priority"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    elif file_format == "json":
        with open("product_report.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        raise ValueError("Invalid format: must be 'csv' or 'json'")
