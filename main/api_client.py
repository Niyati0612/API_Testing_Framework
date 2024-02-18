import requests
import json
import pytest

class APIClient:
    def __init__(self, url, auth_token=None):
        self.url = url
        self.auth_token = auth_token
        self.headers = {'Authorization': f'Bearer {auth_token}'} if auth_token else {}

    def _make_request(self, method, endpoint, data=None):
        try:
            url = f"{self.url}{endpoint}"
            response = requests.request(method, url, json=data, headers=self.headers)
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

    def post(self, endpoint, data):
        return self._make_request('post', endpoint, data)

    def put(self, endpoint, data):
        return self._make_request('put', endpoint, data)

    def delete(self, endpoint):
        return self._make_request('delete', endpoint)

# class TestApiOperations:
#     OBJECT_ID = None
#
#     @pytest.fixture
#     def api_client(self, base_url):
#         return APIClient(url=base_url)
#
#     @pytest.fixture
#     def data_objects(self, object_type):
#         with open(f'../resources/data_{object_type}.json', 'r') as file:
#             data_post = json.load(file)
#         with open(f'../resources/put_{object_type}.json', 'r') as file:
#             data_put = json.load(file)
#         return data_post, data_put
#
#     @pytest.fixture
#     def post_fixture(self, api_client, data_objects, request, object_type):
#         data_post, data_put = data_objects
#         if TestApiOperations.OBJECT_ID is None:
#             response = api_client.post(f"/{object_type}", data_post)
#             TestApiOperations.OBJECT_ID = response.json().get("id")
#         yield TestApiOperations.OBJECT_ID
#
#     def test_get_object(self, api_client, post_fixture, object_type):
#         OBJECT_ID = post_fixture
#         api_client.get(f"/{object_type}/{OBJECT_ID}")
#
#     def test_put_object(self, api_client, post_fixture, data_objects, object_type):
#         OBJECT_ID = post_fixture
#         data_post, data_put = data_objects
#         assert data_put['name'] == 'cat'
#         if all(data_post[key] == data_put[key] for key in data_post):
#             api_client.put(f"/{object_type}/{OBJECT_ID}", data_put)
#         else:
#             for key in data_post:
#                 if data_post[key] != data_put[key]:
#                     print(f"{key} is not equal to {data_post[key]}")
#
#     def test_delete_object(self, api_client, post_fixture, object_type):
#         OBJECT_ID = post_fixture
#         api_client.delete(f'/{object_type}/{OBJECT_ID}')














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
