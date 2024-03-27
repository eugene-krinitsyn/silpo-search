from dataclasses import dataclass
from Models import Shop, Product


@dataclass
class SearchResult:
    shop: Shop
    product: Product
    googleMapsLink: str

    def __init__(self, shop: Shop, product: Product):
        self.shop = shop
        self.product = product
        self.googleMapsLink = f"https://www.google.com/maps/search/?api=1&query={shop.lat},{shop.lon}"
