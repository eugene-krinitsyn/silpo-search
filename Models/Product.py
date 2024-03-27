from dataclasses import dataclass
from Models.JSONModel import JSONModel


@dataclass
class Product(JSONModel):
    id: str
    title: str
    price: float
    oldPrice: float
    companyId: str | None
    branchId: str | None
    externalProductId: str | None
    slug: str
    stock: int
