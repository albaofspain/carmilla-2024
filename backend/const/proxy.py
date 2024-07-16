import os

WEBSHARE_TOKEN = os.environ.get('WEBSHARE_TOKEN')

FIELD_RESULTS = 'results'
FIELD_USERNAME = 'username'
FIELD_PASSWORD = 'password'
FIELD_PROXY_ADDRESS = 'proxy_address'
FIELD_PORT = 'port'

PROXIES_URL = 'https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25'
