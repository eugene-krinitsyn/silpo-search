from typing import List
from Models import Product
from API import SearchResult


class OutputHelper:
    @staticmethod
    def show_search_results(products: List[Product]):
        for product in products:
            print("----------------------------------------------")
            print(f"Product:        {product.title}")
            print(f"ID:             {product.slug}")
            print(f'Stock:          {product.stock}')
            print(f'Discount Price: {product.price}')
            print(f'Full Price:     {product.oldPrice}')

    @staticmethod
    def show_result(result: SearchResult):
        print("----------------------------------------------")
        print(f"Product:        {result.product.title}")
        print(f'Address:        {result.shop.city}, {result.shop.address}')
        print(f'Stock:          {result.product.stock}')
        print(f'Discount Price: {result.product.price}')
        print(f'Full Price:     {result.product.oldPrice}')
        print(f'Google Maps:    {result.googleMapsLink}')
