import pytest
from main.api_client import APIClient
from main.endpoints import PetEndpoints
import json
from main.conftest import base_url
import pandas as pd
from resources.test_readexcel import readData

class TestPetOperations:
    PET_ID = None

    @pytest.fixture
    def api_client(self, base_url):
        return APIClient(url=base_url)

    @pytest.fixture
    def data_pet(self):
        with open('../resources/data_pet.json', 'r') as file:
            data_post = json.load(file)
        with open('../resources/put_pet.json', 'r') as file:
            data_put = json.load(file)
        # df = pd.read_excel('../resources/convert1.xlsx')
        # data= df.iloc[0].to_dict()
        # data_post = json.dumps(data)
        return data_post,data_put

    @pytest.fixture
    def post_fixture(self, api_client, data_pet, request):
        data_post,data_put = data_pet
        if TestPetOperations.PET_ID is None:
            response = api_client.post(PetEndpoints.CREATE_PET, data_post)
            # TestPetOperations.PET_ID = response.json()['id']
            TestPetOperations.PET_ID = response.json().get("id")
        yield TestPetOperations.PET_ID

    def test_get_pet(self, api_client, post_fixture):
        PET_ID = post_fixture
        api_client.get(f"{PetEndpoints.GET_PET}{PET_ID}")

    def test_put_pet(self, api_client, post_fixture, readData):
        PET_ID = post_fixture
        data_put = readData
        myDict = dict(data_put)
        print(myDict)
        api_client.put(f"{PetEndpoints.UPDATE_PET}", myDict)

        # assert data_put['name']=='cat'
        # if all(data_post[key] == data_put[key] for key in data_post):
        #     api_client.put(f"{PetEndpoints.UPDATE_PET}{PET_ID}", data_put)
        # else:
        #     for key in data_post:
        #         if data_post[key] != data_put[key]:
        #             print(f"{key} is not equal to {data_post[key]}")

    def test_delete_pet(self, api_client, post_fixture):
        PET_ID = post_fixture
        api_client.delete(f'{PetEndpoints.DELETE_PET}{PET_ID}')



















# @pytest.fixture
# def post_fixture(base_url):
#     with open('..\\resources\\data_pet.json', 'r') as file:
#         new_data = json.load(file)
#
#     response = requests.post(f'{base_url}{PetEndpoints.CREATE_PET}', json=new_data)
#     PET_ID = response.json().get("id")
#     if PetEndpoints.PET_ID is None:
#         PetEndpoints.PET_ID = PET_ID
#         print("POST request successful")
#         print(f"User ID from POST request: {PET_ID}")
#         print(json.dumps(response.json(), indent=4))
#
#     return PET_ID
#
#
# def test_get_pet(base_url, post_fixture):
#     PET_ID = post_fixture
#     response = requests.get(f"{base_url}{PetEndpoints.GET_PET.format(pet_id=PET_ID)}")
#     PET_ID = response.json().get("id")
#     if PetEndpoints.PET_ID is None:
#         PetEndpoints.PET_ID = PET_ID
#     print("\nGET request successful")
#     print(f"User ID from GET request: {PET_ID}")
#     print(json.dumps(response.json(), indent=4))
#
#
# def test_put_pet(base_url, post_fixture):
#     PET_ID = post_fixture
#     put_data = {
#
#         "name": "doggie",
#         "status": "available"
#
#
#     }
#     response = requests.put(f"{base_url}{PetEndpoints.UPDATE_PET.format(pet_id=PET_ID)}", json=put_data)
#     if response.status_code == 200:
#         print("PUT request successful!")
#         print(json.dumps(response.json(), indent=4))
#
#     else:
#         print(f"PUT request failed with status code: {response.status_code}")
#         return None
#     resp = response.json()
#     for key in put_data.keys():
#         if put_data[key] != resp[key]:
#             print(f"{key} fail")
#
#
# def test_delete_pet(post_fixture, base_url):
#     PET_ID = post_fixture
#     response = requests.delete(f'{base_url}{PetEndpoints.DELETE_PET.format(pet_id=PET_ID)}')
#     if response.status_code == 200:
#         print("\nDELETE request successful")
#         print(f"User ID from DELETE request: {PET_ID}")
#         print(json.dumps(response.json(), indent=4))
#
#     else:
#         print(f"DELETE request failed with status code: {response.status_code}")
#         return None
