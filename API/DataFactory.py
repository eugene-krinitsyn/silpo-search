from typing import List
from API.SilpoRESTAPI import SilpoRESTAPI
from API.SearchResult import SearchResult
from Models import Shop, Product, Branch


class DataFactory:
    api: SilpoRESTAPI

    def __init__(self, api: SilpoRESTAPI):
        self.api = api

    def get_search_results(self, query: str) -> List[Product]:
        return self.api.get_search_results(query=query)

    def get_cities(self) -> List[str] | None:
        return self.api.get_cities()

    def get_results(self, product_names: List[str], cities: List[str]) -> List[SearchResult]:
        results = []
        for city in cities:
            shops_list: [Shop] = self.api.get_shops_list(city)
            for shop in shops_list:
                branches: [Branch] = self.api.get_branches(shop_id=shop.id) if shop.id is not None else []
                for branch in branches:
                    for product_name in product_names:
                        product: Product = self.api.get_product(branch.branchId, product_name)
                        if product.stock is not None and product.stock > 0:
                            result = SearchResult(shop=shop, product=product)
                            results.append(result)
        return results
