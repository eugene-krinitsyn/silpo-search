from urllib.error import URLError, HTTPError
from Network.NetworkSession import NetworkSession
from API.SilpoRESTAPI import SilpoRESTAPI
from API.DataFactory import DataFactory
from API.SearchResult import SearchResult
from IO.OutputHelper import OutputHelper
from IO.InputHelper import InputHelper
from typing import List
from Models import Product


def runner():
    network_session = NetworkSession()
    api = SilpoRESTAPI(network_session)
    data_factory = DataFactory(api)

    search_query: str = InputHelper.get_valid_input(prompt="Enter search query: ")
    search_results: List[Product] = data_factory.get_search_results(query=search_query)
    OutputHelper.show_search_results(products=search_results)
    
    product_names: List[str] = InputHelper.get_products_input()
    show_discounts_only: bool = InputHelper.get_boolean_input("Search discounts only?")

    cities: List[str] | None = data_factory.get_cities()
    selected_cities: [str] = InputHelper.pick_from_list(cities) if cities is not None else []
    if selected_cities is None or not selected_cities:
        raise Exception("Failed to receive cities")

    print(f'Searching for: \'{product_names}\', please wait...')

    results: List[SearchResult] = data_factory.get_results(product_names=product_names, cities=selected_cities)

    if results:
        print(f"Found {len(results)} results:")
        for result in results:
            if show_discounts_only:
                if (result.product.price is not None and
                        result.product.oldPrice is not None and
                        result.product.price < result.product.oldPrice):
                    OutputHelper.show_result(result)
            else:
                OutputHelper.show_result(result)
    else:
        print("No results found")


def main():
    try:
        runner()
    except HTTPError as e:
        print(f"Error: {e.reason}")
        return None
    except URLError as e:
        print(f"Error: {e.reason}")
        return None


if __name__ == "__main__":
    # This block will be executed only if the script is run directly, not if it's imported as a module.
    main()
