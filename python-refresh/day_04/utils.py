def product_status(product):
    if product["quantity"] > 3:
        return "In Stock"
    elif product["quantity"] <= 0:
        return "Out of Stock"
    else:
        return "Low Stock"

def total_inventory_value(unit_price, product_quantity):
    return unit_price * product_quantity

def find_category(product):
    return product.get("category")
