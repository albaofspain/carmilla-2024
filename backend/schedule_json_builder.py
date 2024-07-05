import json
import time
from datetime import datetime, timedelta

from requests import Response

import requests
import const

import proxies
from backend.schedule import ScheduleDTO, ScheduleDTOBuilder

proxy_credential = {
    "http": f"http://{proxies.WEBSHARE_USERNAME}:{proxies.WEBSHARE_PASSWORD}@{proxies.WEBSHARE_ADDRESS}:{proxies.WEBSHARE_PORT}",
    "https": f"http://{proxies.WEBSHARE_USERNAME}:{proxies.WEBSHARE_PASSWORD}@{proxies.WEBSHARE_ADDRESS}:{proxies.WEBSHARE_PORT}"
}


def fetch_kst_datetime() -> str:

    machine_timezone = time.tzname[time.localtime().tm_isdst]
    today = datetime.now()

    if machine_timezone != "KST":
        today = today + timedelta(hours=9)

    return today.strftime("%Y%m%d")


"""
: raise requests.HTTPError: if the HTTP request returned an unsuccessful status code
: raise requests.RequestException: if the request failed for any reason
"""


def fetch_schedule_from_interpark(start_date: str) -> Response:
    url = const.REQUEST_URL + start_date

    api_response = requests.get(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0',
        },
        proxies=proxy_credential,
    )
    api_response.raise_for_status()

    return api_response


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


def parse_schedule(api_response: Response) -> list[ScheduleDTO]:
    raw_data = api_response.json()
    raw_schedules = raw_data['data']['dataList']
    schedules = []

    for raw_schedule in raw_schedules:
        schedules.append(ScheduleDTOBuilder.build(raw_schedule))

    return schedules
