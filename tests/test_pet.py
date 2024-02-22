from tests.api_client import *
from main.endpoints import PetEndpoints
import json
from main.conftest import base_url

class TestPetOperations:
    PET_ID = None

    @pytest.fixture
    def data_pet(self):
        with open('../main/Data/data_pet.json', 'r') as file:

            data_post = json.load(file)
        with open('../main/Data/put_pet.json', 'r') as file:
            data_put = json.load(file)
        return data_post, data_put

    @pytest.fixture
    def pet_id(self, api_client, data_pet):
        if TestPetOperations.PET_ID is None:
            response = api_client.post(f'{PetEndpoints.CREATE_PET}', data_pet[0], files=None)
            TestPetOperations.PET_ID = response.json().get("id")
        return TestPetOperations.PET_ID

    def test_post_pet(self, api_client, data_pet):
        data_post, data_put = data_pet
        api_client.post(f'{PetEndpoints.CREATE_PET}', data_post, files=None)

    # def test_post_pet_image(self, api_client, pet_id):
    #     PET_ID = pet_id
    #     files = {'file': ('image.jpg', open('image.png', 'rb'), 'image/jpeg')}
    #     api_client.post(f'{PetEndpoints.CREATE_PET}{PET_ID}', files=files,data=None)

    def test_get_pet(self, api_client, pet_id):
        PET_ID = pet_id
        api_client.get(f"{PetEndpoints.GET_PET}{PET_ID}")

    def test_get_pet_status(self, api_client):
        PET_ID = "findByStatus?status=available"
        api_client.get(f"{PetEndpoints.GET_PET}{PET_ID}")

    def test_put_pet(self, api_client, data_pet, pet_id):
        data_post, data_put = data_pet
        PET_ID = pet_id
        if all(data_post[key] == data_put[key] for key in data_post):
            api_client.put(f"{PetEndpoints.UPDATE_PET}{PET_ID}", data_put)
        else:
            for key in data_post:
                if data_post[key] != data_put[key]:
                    print(f"{key} is not equal to {data_post[key]}")

    def test_delete_pet(self, api_client, pet_id):
        PET_ID = pet_id
        api_client.delete(f'{PetEndpoints.DELETE_PET}{PET_ID}')





























# import pandas as pd
# from Execution.test_readexcel import readData
# df = pd.read_excel('../Execution/convert1.xlsx')
# data= df.iloc[0].to_dict()

# data_post = json.dumps(data)
# data_put = readData
# myDict = dict(data_put)
# print(myDict)
# api_client.put(f"{PetEndpoints.UPDATE_PET}", myDict)
#         response_dict = response.json()
#
#         # Create a DataFrame from the response data
#         df = pd.DataFrame([response_dict])
#
#         # Save the DataFrame to an Excel file with the 'id' column formatted as a string
#         df.to_excel('response.xlsx', index=False, float_format='%0.f')
#
#         # Store the PET_ID from the response for future use
# df = pd.DataFrame(data)
#
# # Fetch the value at row index 2 and column index 1 (0-based indexing)
# value = df.iloc[2, 1]
