class UsersEndpoints:
    USER_ID = None
    GET_USER = "v2/user/"
    CREATE_USER = "v2/user/"
    UPDATE_USER = "v2/user/"
    DELETE_USER = "v2/user/"


class PetEndpoints:
    PET_ID = None
    GET_PET = "v2/pet/"
    CREATE_PET = "v2/pet/"
    UPDATE_PET = "v2/pet"
    DELETE_PET = "v2/pet/"


class StoreEndpoints:
    STORE_ID = None
    GET_STORE = "v2/store/order/"
    CREATE_STORE = "v2/store/order/"
    GET_INVENTORY = "v2/store/inventory/"
    DELETE_STORE = "v2/store/order/"










# def end_point_request(data, key):
#     global end_point
#     for i in data.keys():
#         if i == key:
#             end_point = data.get(i)
#             break
#     return end_point
