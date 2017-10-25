

import requests

def get_users():
    url = 'http://127.0.0.1:8000/users/'
    r = requests.get(url)
    books = r.json()

    return books
