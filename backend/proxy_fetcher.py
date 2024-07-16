import requests

from backend.const import proxy as const
from backend.dto.proxy import ProxyDTO, ProxyDTOBuilder


def fetch_proxy_from_webshare() -> list[ProxyDTO]:
    url = const.PROXIES_URL

    api_response = requests.get(
        url,
        headers={
            'Authorization': f'Token {const.WEBSHARE_TOKEN}',
        },
    )

    api_response.raise_for_status()

    return _parse_proxy(api_response)


"""
: raise KeyError: if the key is not found in the dictionary
: raise JsonDecodeError: if the JSON data is not valid
"""


def _parse_proxy(api_response: requests.Response) -> list[ProxyDTO]:
    raw_data = api_response.json()
    raw_proxies = raw_data[const.FIELD_RESULTS]
    proxies = []

    for raw_proxy in raw_proxies:
        proxies.append(ProxyDTOBuilder.build(raw_proxy))

    return proxies
