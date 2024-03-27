import urllib.parse
import urllib.request
import json
from Network.ParameterType import ParameterType


class NetworkRequest:
    def __init__(
            self,
            url: str,
            method='GET',
            headers: dict = None,
            parameters: dict = None,
            parameters_type: ParameterType = None
    ):
        self.url = url
        self.method = method.upper()  # Convert method to uppercase
        self.headers = headers
        self.parameters_type = parameters_type
        self.parameters_dict = parameters

        match parameters_type:
            case ParameterType.QUERY:
                if method.upper() != 'GET':
                    raise ValueError("ParameterType.QUERY only makes sense with GET method")
            case ParameterType.BODY:
                if method.upper() == 'GET':
                    raise ValueError("ParameterType.BODY does not make sense with GET method")
            case _:
                pass  # No specific action needed for other cases

    @property
    def urllib_request(self) -> urllib.request.Request:
        url = self.url
        data = None

        match self.parameters_type:
            case ParameterType.QUERY:
                query_params = self.parameters_dict if self.parameters_dict else {}
                url = self.url + '?' + urllib.parse.urlencode(query_params)
            case ParameterType.BODY:
                body_params = self.parameters_dict if self.parameters_dict else {}
                data = json.dumps(body_params).encode('utf-8')

        request = urllib.request.Request(url, data=data, headers=self.headers, method=self.method)
        return request
