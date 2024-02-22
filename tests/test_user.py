from tests.api_client import *
from main.endpoints import UsersEndpoints
import pytest


class TestUserOperations:
    USER_ID = None

    @pytest.fixture
    def data_user(self):
        with open('../main/Data/data_user.json', 'r') as file:
            payload_user = json.load(file)
        with open('../main/Data/put_user.json', 'r') as file:
            data_put = json.load(file)
        return payload_user, data_put

    @pytest.fixture
    def username(self, data_user):
        payload_user, data_put = data_user
        if TestUserOperations.USER_ID is None:
            TestUserOperations.USER_ID = payload_user.get("username")
        yield TestUserOperations.USER_ID

    def test_post_user(self, api_client, data_user):
        payload_user, data_put = data_user
        api_client.post(f'{UsersEndpoints.CREATE_USER}', payload_user,files=None)

    # def test_post_user_list(self, api_client, data_user):
    #     payload_user, data_put = data_user
    #     api_client.post(f'{UsersEndpoints.CREATE_USER}createWithList', payload_user)
    #
    # def test_post_user_array(self, api_client, data_user):
    #     payload_user, data_put = data_user
    #     api_client.post(f'{UsersEndpoints.CREATE_USER}createWithArray', payload_user)

    def test_put_user(self, api_client, username, data_user):
        data_put, payload_user = data_user
        USER_ID = username
        if all(payload_user[key] == data_put[key] for key in payload_user):
            api_client.put(f'{UsersEndpoints.UPDATE_USER}{USER_ID}', data_put)
        else:
            for key in payload_user:
                if payload_user[key] != data_put[key]:
                    print(f"{key} is not equal to {payload_user[key]}")

    def test_get_user(self, api_client, username):
        USER_ID = username
        api_client.get(f'{UsersEndpoints.GET_USER}{USER_ID}')

    def test_get_user_login(self, api_client, username):
        api_client.get(f'{UsersEndpoints.GET_USER}login?username=string&password=123')

    def test_get_user_logout(self, api_client, username):
        api_client.get(f'{UsersEndpoints.GET_USER}logout')

    def test_delete_user(self, api_client, username):
        USER_ID = username
        api_client.delete(f'{UsersEndpoints.DELETE_USER}{USER_ID}')
