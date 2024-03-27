from Network.NetworkSession import NetworkSession
from Network.NetworkRequest import NetworkRequest
from Network.ParameterType import ParameterType
from typing import List
from Models.Product import Product
from Models.Shop import Shop
from Models.Branch import Branch


class SilpoRESTAPI:
    network_session: NetworkSession

    def __init__(self, network_session: NetworkSession):
        self.network_session = network_session

    common_headers = {
        'Accept': 'application/json',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json'
    }

    def get_search_results(self, query: str) -> List[Product]:
        params = {
            "limit": "47",
            "offset": "0",
            "deliveryType": "DeliveryHome",
            "includeChildCategories": "true",
            "sortBy": "productsList",
            "sortDirection": "desc",
            "inStock": "true",
            "search": query
        }
        request = NetworkRequest(
            url='https://sf-ecom-api.silpo.ua/v1/uk/branches/00000000-0000-0000-0000-000000000000/products',
            headers=SilpoRESTAPI.common_headers,
            parameters=params,
            parameters_type=ParameterType.QUERY
        )
        json_data = self.network_session.execute_request(request, x_path='items')
        parsed_array = list(map(lambda x: Product.from_json(x), json_data if json_data is not None else []))
        return parsed_array

    def get_cities(self) -> List[str] | None:
        params = {
            "method": "GetPickupCities",
            "data": {
                "merchantId": 1,
                "basketGuid": "",
                "city": "",
                "businessId": 1
            }
        }
        request = NetworkRequest(
            url='https://api.catalog.ecom.silpo.ua/api/2.0/exec/EcomCatalogGlobal',
            method='POST',
            headers=SilpoRESTAPI.common_headers,
            parameters=params,
            parameters_type=ParameterType.BODY
        )
        data = self.network_session.execute_request(request, x_path='items')
        return data

    def get_shops_list(self, city: str) -> List[Shop]:
        params = {
            'method': 'GetPickupFilials',
            'data': {
                'merchantId': 1,
                'businessId': 1,
                'city': city
            }
        }
        request = NetworkRequest(
            url='https://api.catalog.ecom.silpo.ua/api/2.0/exec/EcomCatalogGlobal',
            method='POST',
            headers=SilpoRESTAPI.common_headers,
            parameters=params,
            parameters_type=ParameterType.BODY
        )
        data = self.network_session.execute_request(request, x_path='items')
        parsed_array = list(map(lambda x: Shop.from_json(x), data if data is not None else []))
        return parsed_array

    def get_branches(self, shop_id: int) -> List[Branch]:
        params = {'filialIds[]': shop_id}
        request = NetworkRequest(
            url='https://sf-ecom-api.silpo.ua/v1/branches/by-filial-ids',
            headers=SilpoRESTAPI.common_headers,
            parameters=params,
            parameters_type=ParameterType.QUERY
        )
        data = self.network_session.execute_request(request, x_path='items')
        parsed_array = list(map(lambda x: Branch.from_json(x), data if data is not None else []))
        return parsed_array

    def get_product(self, branch_id: str, product_name: str) -> Product:
        params = {'deliveryType': 'SelfPickup'}
        request = NetworkRequest(
            url=f"https://sf-ecom-api.silpo.ua/v1/uk/branches/{branch_id}/products/{product_name}",
            headers=SilpoRESTAPI.common_headers,
            parameters=params,
            parameters_type=ParameterType.QUERY
        )
        data = self.network_session.execute_request(request)
        parsed = Product.from_json(data)
        return parsed
