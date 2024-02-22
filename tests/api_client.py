import pytest
import requests
import json
from main.conftest import validate_url, base_url


@pytest.fixture
def test_validate_baseurl(self):
    validate_url(self)


@pytest.fixture
def api_client(base_url):
    return APIClient(url=base_url)


class APIClient:
    def __init__(self, url, auth_token=None):
        self.file = None
        self.url = url
        self.auth_token = auth_token
        self.headers = {'Authorization': f'Bearer {auth_token}'} if auth_token else {}

    def _make_request(self, method, endpoint, data=None, file=None):
        try:
            url = f"{self.url}{endpoint}"
            response = requests.request(method, url, json=data, headers=self.headers, files=self.file)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            print(f"\n{method.upper()} request to {endpoint} successful")
            if response.text:
                print(json.dumps(response.json(), indent=4))
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error during {method.upper()} request to {endpoint}: {e}")
            return None

    def get(self, endpoint):
        return self._make_request('get', endpoint)

    def post(self, endpoint, data, files):
        return self._make_request('post', endpoint, data, files)

    def put(self, endpoint, data):
        return self._make_request('put', endpoint, data)

    def delete(self, endpoint):
        return self._make_request('delete', endpoint)
























# class APIClient:
#
#     def __init__(self, url, auth_token=None):
#         self.url = url
#
#     def get(self, endpoint):
#         try:
#             url = f"{self.url}{endpoint}"
#             response = requests.get(url)
#             if response.status_code == 200:
#                 print("\nGET request successful")
#                 print(json.dumps(response.json(), indent=4))
#                 return response
#             else:
#                 print(f"Error: {response.status_code}")
#                 return None
#         except requests.exceptions.RequestException as e:
#             print(f"Error during GET request: {e}")
#             return None
#
#     def post(self, endpoint, data):
#         url = f"{self.url}{endpoint}"
#         response = requests.post(url, json=data)
#         return response
#
#
#     def put(self, endpoint, data):
#         url = f"{self.url}{endpoint}"
#         response = requests.put(url, json=data)
#         return response
#
#
#     def delete(self, endpoint):
#         url = f"{self.url}{endpoint}"
#         response = requests.delete(url)
#         if response.status_code == 200:
#             print("\nDELETE request successful")
#             print(json.dumps(response.json(), indent=4))
#
#         else:
#             print(f"DELETE request failed with status code: {response.status_code}")
#             return None
#         return response ::::: optiimize this code
te