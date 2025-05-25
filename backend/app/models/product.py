from beanie import Document
from pydantic import BaseModel
from typing import Optional

class Product(Document):
    name: str
    price: float
    description: Optional[str]

    class Settings:
        name = "products"  # MongoDB collection name