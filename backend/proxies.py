import os
import const


WEBSHARE_ADDRESS = os.environ.get(const.PROXY_ADDRESS_KEY)
WEBSHARE_PORT = os.environ.get(const.PROXY_PORT_KEY)
WEBSHARE_USERNAME = os.environ.get(const.PROXY_USERNAME_KEY)
WEBSHARE_PASSWORD = os.environ.get(const.PROXY_PASSWORD_KEY)
