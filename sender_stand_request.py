import configuration
import requests
import data

# Solicitud GET crear un usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = body,
                         headers = data.headers)

# Solicitud POST para crear Kit
def post_new_client_kit(kit_body,auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         headers={"Authorization" : f"Bearer {auth_token}"},
                         json = kit_body)
