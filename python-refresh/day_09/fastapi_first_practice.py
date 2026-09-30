from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from typing import List, Dict

app = FastAPI()

class Cart(BaseModel):
    products: List[Dict]
    total: int
    discountedTotal: int
    userId: int
    totalProducts: int
    totalQuantity: int  

carts = requests.get("https://dummyjson.com/carts").json()
cart_list = {cart["id"]: cart["products"] for cart in carts["carts"]}

@app.get("/carts")
def get_all_carts():
    return cart_list

@app.get("/carts/{cart_id}")
def get_cart_by_id(cart_id: int):
    if cart_id not in cart_list:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart_list[cart_id]

@app.post("/carts")
def create_cart(cart: Cart):
    cart_list[len(cart_list) + 1] = cart.products
    return {"message": "Cart created", "cart": cart}
