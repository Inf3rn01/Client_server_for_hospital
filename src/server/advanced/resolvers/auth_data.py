from src.server.database.models import AuthData


def login(login_str, password):
    auth_data: AuthData = AuthData.get_or_none(
        AuthData.login == login_str,
        AuthData.password == password
    )

    return {'error': 'Incorrect login or password'} if auth_data is None else auth_data.user_id.id


