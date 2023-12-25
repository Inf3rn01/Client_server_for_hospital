import requests
import json
import settings

server_url: str = f'http://{settings.SERVER_HOST}:{settings.SERVER_PORT}'


def server_available(func):
    def need_it(*args, **kwargs):
        try:
            requests.get(url=server_url)
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            return {'error': 'Server not available'}

    return need_it


@server_available
def check_connection():
    return True


@server_available
def register(fullname: str, login_str: str, password: str) -> bool:
    new_user_data = {'id': 0, 'fullname': fullname, 'balance': 1000, 'regular': False}

    new_user_answer = requests.post(
        url=f'{server_url}/user/create',
        data=json.dumps(new_user_data)
    )

    new_auth_data = {'id': 0, 'login': login_str, 'password': password, 'user_id': new_user_answer.json()['id']}

    new_auth_answer = requests.post(
        url=f'{server_url}/auth_data/create',
        data=json.dumps(new_auth_data)
    )

    return True


@server_available
def login(login_str: str, password: str) -> int:
    data = {"login": login_str, "password": password}

    answer = requests.post(
        url=f'{server_url}/auth_data/login',
        data=json.dumps(data)
    )

    return answer.json()


@server_available
def get_user_by_id(id: int) -> dict:
    return requests.get(
        url=f'{server_url}/user/get/{id}'
    ).json()
