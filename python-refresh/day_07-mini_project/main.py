from datetime import datetime
from product_report.api import fetch
from product_report.processor import process_json, generate_report
from product_report.utils import log

URL = "https://dummyjson.com/products"
response = fetch(URL)
result = process_json(response)

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("   TECHGECKO PRODUCT REPORT   ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()

print(f'Products analyzed:          {result["product_count"]}')
print(f'Units in stock:             {result["in_stock_count"] + result["low_stock_count"]}')
print(f'Inventory value:    ${result["inventory_value"]:.2f}')
print(f'Average rating:           {(result["total_rating"] / result["product_count"]):.2f}')
print()

print("STOCK STATUS")
print(f'✓ In Stock:                 {result["in_stock_count"]}')
print(f'⚠ Low Stock:                 {result["low_stock_count"]}')
print(f'✕ Out of Stock:              {result["out_of_stock_count"]}')
print()

print(f'⚠ PRODUCTS NEEDING ATTENTION: {result["needs_attention"]}')

try:
    generate_report(result["data"], "csv")
    generate_report(result["data"], "json")
except Exception as e:
    print("ERROR: ", str(e))
    log(f"[{datetime.now()}] {str(e)}.")
else:
    print()
    print("Reports generated:")
    print("✓ product_report.csv")
    print("✓ product_report.json")
    print("✓ product_report.log")
    log(f"[{datetime.now()}] TechGecko product report generated successfully.")
