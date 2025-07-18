from fastapi import FastAPI
from product import Product
from json_db import JsonDB  


app = FastAPI()

productsDB = JsonDB(path='./data/products.json')

@app.get("/products")
def get_products():
    products = productsDB.read()
    return{"products": products}

@app.post("/products")
def create_products(product: Product):

    print("new product", product)
    return{"status": "inserted"}

