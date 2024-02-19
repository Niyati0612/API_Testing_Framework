import pytest
from main.api_client import *
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
        return data_post, data_put

    @pytest.fixture
    def post_fixture(self, api_client, data_pet, request):
        data_post, data_put = data_pet
        if TestPetOperations.PET_ID is None:
            response = api_client.post(PetEndpoints.CREATE_PET, data_post)
            # TestPet3Operations.PET_ID = response.json()['id']
            TestPetOperations.PET_ID = response.json().get("id")
        yield TestPetOperations.PET_ID

    def test_get_pet(self, api_client, post_fixture):
        PET_ID = post_fixture
        api_client.get(f"{PetEndpoints.GET_PET}{PET_ID}")

    def test_put_pet(self, api_client, data_pet, post_fixture):
        data_post, data_put = data_pet
        PET_ID = post_fixture
        # data_put = readData
        # myDict = dict(data_put)
        # print(myDict)
        # api_client.put(f"{PetEndpoints.UPDATE_PET}", myDict)
        assert data_put['name'] == 'cat'
        if all(data_post[key] == data_put[key] for key in data_post):
            api_client.put(f"{PetEndpoints.UPDATE_PET}{PET_ID}", data_put)
        else:
            for key in data_post:
                if data_post[key] != data_put[key]:
                    print(f"{key} is not equal to {data_post[key]}")

    def test_delete_pet(self, api_client, post_fixture):
        PET_ID = post_fixture
        api_client.delete(f'{PetEndpoints.DELETE_PET}{PET_ID}')

        # df = pd.read_excel('../resources/convert1.xlsx')
        # data= df.iloc[0].to_dict()
        # data_post = json.dumps(data)
