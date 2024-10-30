from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/id/{product}")
def displayProduct(product: int):
    return f"product {product}"