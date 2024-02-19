import requests
import json
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


# import requests, pytest
# import logging
# from endpoints import end_point_request
# logger = logging.getLogger()
#
# # e_response = {"key": "value"}
# @pytest.mark.post
# def post(base_url, endpoint, data, key):
#     try:
#         global e_response
#         response_post = requests.post(f'{base_url}{endpoint}', json=data)
#         e_response = response_post.json()
#         print("\n\nPOST request successful.\nResponse:", e_response)
#         print("Print ID:", end_point_request(data, key, e_response))
#         return e_response
#
#     except requests.exceptions.RequestException as e:
#         # raise Exception (f"\nPOST request failed. Error: {e}")
#         logger.error(f"\n\nPOST request failed. Error: {e}")
#         return False
#
# @pytest.mark.get
# def get(base_url, endpoint, data, key):
#     try:
#         global e_response
#         response = requests.get(f'{base_url}{endpoint}{end_point_request(data, key, e_response)}', json=data)
#         response.raise_for_status()
#         print("\n\nGET request successful.\nResponse:", response.json())
#         return response
#
#     except requests.exceptions.RequestException as e:
#         logger.error(f"\n\nGET request failed. Error: {e}")
#         return False
#
# @pytest.mark.put
# def put(base_url, endpoint, data, udata):
#     try:
#         response = requests.put(f'{base_url}{endpoint}', json=udata)
#         response.raise_for_status()
#         print("\n\nPUT request successful.\nResponse:", response.json())
#         for key in data:
#             if data[key] != udata[key]:
#                 print(f"{key} FAIL {data[key]}")
#             else:
#                 print(f"{key} PASS {data[key]}")
#                 # sys.exit()
#         return response
#
#     except requests.exceptions.RequestException as e:
#         logger.error(f"\n\nPUT request failed. Error: {e}")
#         return False
#
# @pytest.mark.put_specification
# def put_with_specification(base_url, endpoint, data, udata, key):
#     try:
#         global e_response
#         print(e_response)
#         response = requests.put(f'{base_url}{endpoint}{end_point_request(data, key, e_response)}', json=udata)
#         print("\n\nPUT request successful.\nResponse:", response.json())
#         for key in data:
#             if data[key] != udata[key]:
#                 print(f"{key} FAIL {data[key]}")
#             else:
#                 print(f"{key} PASS {data[key]}")
#                 # sys.exit()
#         return response
#
#     except requests.exceptions.RequestException as e:
#         logger.error(f"\n\nPUT request failed. Error: {e}")
#         return False
#
# @pytest.mark.delete
# def delete(base_url, endpoint, data, key):
#     try:
#         response = requests.delete(f'{base_url}{endpoint}{end_point_request(data, key, e_response)}', json=data)
#         print("\n\nDELETE request successful.\nResponse:", response.json())
#         response.raise_for_status()
#         return response
#
#     except requests.exceptions.RequestException as e:
#         logger.error(f"\n\nDELETE request failed. Error: {e}")
#         return False
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


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
