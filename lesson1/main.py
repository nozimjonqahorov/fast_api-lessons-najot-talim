from fastapi import FastAPI
from products.router import router as product_router
from orders.router import router as order_router
from sellers.router import router as seller_router
from buyers.router import router as buyer_router
from customers.router import router as customer_router
from inventory.router import router as inventory_router
from payments.router import router as payment_router
from reviews.router import router as review_router
app = FastAPI()

app.include_router(product_router, prefix="/products")
app.include_router(order_router, prefix="/orders")
app.include_router(seller_router, prefix="/sellers")
app.include_router(buyer_router, prefix="/buyers")
app.include_router(customer_router, prefix="/customers")
app.include_router(inventory_router, prefix="/inventory")
app.include_router(payment_router, prefix="/payments")
app.include_router(review_router, prefix="/reviews")


@app.get("/")
def test():
    return {"message": "Hello, Nozim!"}

    