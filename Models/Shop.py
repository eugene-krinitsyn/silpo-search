from dataclasses import dataclass
from Models.JSONModel import JSONModel


@dataclass
class Shop(JSONModel):
    id: int
    title: str | None
    city: str | None
    address: str | None
    pickup: bool | None
    delivery: bool | None
    businessId: int | None
    lat: float | None
    lon: float | None
