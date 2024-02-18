import json
from main.conftest import base_url
from main.endpoints import UsersEndpoints
import pytest
from main.api_client import APIClient


class TestUserOperations:
    USER_ID = None

    @pytest.fixture
    def api_client(self, base_url):
        return APIClient(url=base_url)

    @pytest.fixture
    def data_user(self):
        with open('../resources/data_user.json', 'r') as file:
            payload_user = json.load(file)
        with open('../resources/put_user.json', 'r') as file:
            data_put = json.load(file)
        return payload_user,data_put

    @pytest.fixture
    def username(self, api_client, data_user):
        payload_user,data_put = data_user
        if TestUserOperations.USER_ID is None:
            TestUserOperations.USER_ID = payload_user.get("username")
        yield TestUserOperations.USER_ID

    def test_post_user(self, api_client, data_user):
        payload_user,data_put = data_user
        api_client.post(f'{UsersEndpoints.CREATE_USER}', payload_user)

    def test_get_user(self, api_client, username):
        USER_ID = username
        api_client.get(f'{UsersEndpoints.GET_USER}{USER_ID}')

    def test_put_user(self, api_client, username,data_user):
        data_put, payload_user = data_user
        USER_ID = username
        if all(payload_user[key] == data_put[key] for key in payload_user):
            api_client.put(f'{UsersEndpoints.UPDATE_USER}{USER_ID}', data_put)
        else:
            for key in payload_user:
                if payload_user[key] != data_put[key]:
                    print(f"{key} is not equal to {payload_user[key]}")


    def test_delete_user(self, api_client, username):
        USER_ID = username
        api_client.delete(f'{UsersEndpoints.DELETE_USER}{USER_ID}')



















# def test_post_user(base_url):
#     with open('../resources\\data_user.json', 'r') as file:
#         new_data = json.load(file)
#
#     response = requests.post(f'{base_url}user', json=new_data)
#     print("\nPOST request successful")
#     assert response.status_code == 200
#     print(response.json())
#
#
# def test_get_user(base_url, username):
#     response = requests.get(f"{base_url}user/{username}")
#     assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
#     print(json.dumps(response.json(), indent=4))
#
#
# def test_put_user(base_url, username):
#     put_data = {
#         "username": "doggie",
#     }
#     url = f"{base_url}user/{username}"  # Replace with your actual API endpoint
#     response = requests.put(url, json=put_data)
#
#     assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
#     print(json.dumps(response.json(), indent=4))
#
#
# def test_delete_user(base_url, username):
#     response = requests.delete(f'{base_url}user/{username}')
#     if response.status_code == 200:
#         print("DELETE request successful")
#         print(json.dumps(response.json(), indent=4))
#
#     else:
#         print(f"DELETE request failed with status code: {response.status_code}")
#         return None
#
#
#
