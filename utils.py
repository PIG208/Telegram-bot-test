from json import load

credentials = load(open('token.json'))


def get_token():
    return credentials['token']