class UsersEndpoints:
    GET_USER = "v2/user/"
    CREATE_USER = "v2/user/"
    UPDATE_USER = "v2/user/"
    DELETE_USER = "v2/user/"


class PetEndpoints:
    GET_PET = "v2/pet/"
    CREATE_PET = "v2/pet/"
    UPDATE_PET = "v2/pet"
    DELETE_PET = "v2/pet/"


class StoreEndpoints:
    GET_STORE = "v2/store/order/"
    CREATE_STORE = "v2/store/order/"
    GET_INVENTORY = "v2/store/inventory/"
    DELETE_STORE = "v2/store/order/"


# end_point_pet = "/v2/pet/"
# end_point_user = "/v2/user/"
# end_point_store = "/v2/store/order/"
#
# end_point = 0
# def end_point_request(data, key, response):
#     global end_point
#     if key == "id":
#         for i in data.keys():
#             if i == key:
#                 end_point = response.get(i)
#                 break
#         return end_point
#     else:
#         for i in data.keys():
#             if i == key:
#                 end_point = data.get(i)
#                 break
#         return end_point