import requests


def api_login():
    payload = {
        'username': '0302226873',
        'password': '0302226873',
    }
    headers = {'Authorization': 'Token 18c895c9139fba860a352a32aa4232986d8f3743'}
    r = requests.post('http://127.0.0.1:8000/api/login/', data=payload, headers=headers)
    if r.status_code == 200:
        items = r.json()
        print(items)
    else:
        print(r.text)


api_login()
