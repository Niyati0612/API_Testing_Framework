import pytest
from tests.api_client import APIClient
from main.endpoints import StoreEndpoints
import json
from main.conftest import base_url

class TestStoreOperations:
    STORE_ID =None
    @pytest.fixture
    def api_client(self, base_url):
        return APIClient(url=base_url)

    @pytest.fixture
    def data_store(self):
        with open('../main/Data/data_store.json', 'r') as file:
            data_post = json.load(file)
        return data_post

    @pytest.fixture
    def post_fixture(self, api_client, data_store):
        data_post= data_store
        if TestStoreOperations.STORE_ID is None:
            response = api_client.post(f'{StoreEndpoints.CREATE_STORE}', data_post,files=None)
            TestStoreOperations.STORE_ID= response.json().get("id")
        yield TestStoreOperations.STORE_ID

    def test_get_store(self, api_client, post_fixture):
        STORE_ID = post_fixture
        api_client.get(f"{StoreEndpoints.GET_STORE}{STORE_ID}")

    def test_get_store_invetory(self,api_client, post_fixture):
        STORE_ID = post_fixture
        api_client.get(f"{StoreEndpoints.GET_INVENTORY}")
        print("\nInventory details")

    def test_delete_store(self, api_client, post_fixture):
        STORE_ID = post_fixture
        api_client.delete(f'{StoreEndpoints.DELETE_STORE}{STORE_ID}')
