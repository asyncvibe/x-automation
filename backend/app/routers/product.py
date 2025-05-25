from fastapi import APIRouter
from app.models.product import Product

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
async def get_products():
    return await Product.find_all().to_list()

@router.post("/")
async def create_product(product: Product):
    await product.insert()
    return product
