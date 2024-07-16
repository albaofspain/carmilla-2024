import json
import requests

from backend.const import schedule as const
from backend.dto.schedule import ScheduleDTO, ScheduleDTOBuilder
from backend.proxy_fetcher import fetch_proxy_from_webshare

"""
: raise requests.HTTPError: if the HTTP request returned an unsuccessful status code
: raise requests.RequestException: if the request failed for any reason
"""


def fetch_schedule_from_interpark(start_date: str) -> list[ScheduleDTO]:
    api_response = _fetch_schedule_with_proxies(start_date)

    return _parse_schedule(api_response)


def _fetch_schedule_with_proxies(start_date: str) -> requests.Response:
    proxies = fetch_proxy_from_webshare()

    for proxy in proxies:
        proxy_credential = {
            "http": f"http://{proxy.user_name}:{proxy.password}@{proxy.proxy_address}:{proxy.port}",
            "https": f"http://{proxy.user_name}:{proxy.password}@{proxy.proxy_address}:{proxy.port}"
        }

        url = const.REQUEST_URL + start_date

        api_response = requests.get(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0',
            },
            proxies=proxy_credential,
        )

        if api_response.status_code == 200:
            return api_response

    raise requests.RequestException('All proxies are not working')


"""
: raise IOError: if an I/O operation fails (e.g. file not exists)
"""


def write_schedule_in_json(schedules: list[ScheduleDTO]) -> None:
    json_data = {
        const.FIELD_CASTINGS: []
    }

    for schedule in schedules:
        json_data[const.FIELD_CASTINGS].append(schedule.to_dict())

    with open(const.SCHEDULE_JSON_FILE, 'w') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)


"""
: raise KeyError: if the key is not found in the dictionary
: raise JsonDecodeError: if the JSON data is not valid
"""


def _parse_schedule(api_response: requests.Response) -> list[ScheduleDTO]:
    raw_data = api_response.json()
    raw_schedules = raw_data['data']['dataList']
    schedules = []

    for raw_schedule in raw_schedules:
        schedules.append(ScheduleDTOBuilder.build(raw_schedule))

    return schedules
