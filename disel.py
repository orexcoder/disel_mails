import requests
from anti_useragent import UserAgent as ua
from loguru import logger

import config

def get_headers(): return config.HEADERS.copy()

def setup_session(proxy: str):
    session = requests.Session()
    headers = get_headers()
    headers["User-Agent"] = ua().random
    session.headers = headers
    session.proxies.update({'https': 'http://' + proxy})
    return session

def subscribe_disel(email: str, proxy: str):

    session = setup_session(proxy)

    data = {
        "action": "register",
        "email": email
    }

    resp = session.post(
        "https://hape.diesel.com/api.php",
        data
    )

    if resp.status_code == 200:
        logger.success(f" {email} successfully registered!")
    else:
        logger.error(f" {email} - {resp.status_code}")


