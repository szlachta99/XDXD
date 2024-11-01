from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/id/{product}")
def displayProduct(product: int):
    return f"product {product}"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
