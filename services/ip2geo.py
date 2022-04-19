import requests


def get_geo(ip='127.0.0.1'):
    try:
        if ip == '127.0.0.1':
            raise Exception('[✖] IP expected Localhost received')
        return requests.get(url=f'http://ip-api.com/json/{ip}').json()
    except requests.exceptions.ConnectionError:
        return '[✖] Please check your connection!'


if __name__ == '__main__':
    from pif import get_public_ip
    from pprint import pprint

    pprint(get_geo(get_public_ip()))
