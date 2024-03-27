import json
import urllib.parse
import urllib.request
import Network.NetworkRequest


class NetworkSession:

    def execute_request(self, req: Network.NetworkRequest.NetworkRequest, x_path: str | None = None):
        with urllib.request.urlopen(req.urllib_request) as response:
            response_data = response.read().decode('utf-8')
            result = json.loads(response_data)
            if not result:
                raise ValueError("Invalid or empty JSON data")
            if isinstance(x_path, str):
                return result[x_path]
            else:
                return result
