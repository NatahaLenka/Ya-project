import requests
import configuration
import data


#api


def get_docs():
    url = configuration.URL_SERVICE + configuration.DOC_PATH
    return requests.get(url)


#new_client


def post_new_user():
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    return requests.post(url,
                         json=data.user_body,
                         headers=data.headers)


#create_kits


def post_new_client_kit(authToken, kit_name):
    url = configuration.URL_SERVICE + configuration.KITS_PATH
    body = {
        "name": kit_name
    }
    new_headers = data.headers.copy()
    new_headers['Authorization'] = "Bearer " + authToken
    return requests.post(url, json=body, headers=new_headers)
