import requests


def get_photo_url(url, client_id, query):
    response = requests.get(url.format(query, client_id)).json()
    return response['urls']['full']
