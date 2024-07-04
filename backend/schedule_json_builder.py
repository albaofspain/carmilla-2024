import json
import sys

import const
import requests
from datetime import datetime
from backend.schedule import ScheduleDTO, ScheduleDTOBuilder


def fetch_schedule_from_interpark(start_date: str) -> dict:
    try:
        url = const.REQUEST_URL + start_date
        print(url)
        response = requests.get(url)
        print(response)
        response.raise_for_status()
        raw_schedules = response.json()
        print(raw_schedules)
    # except requests.exceptions.RequestException as e:
    #     print(f'Failed to fetch schedule from interpark: {e.response}')
    #     raw_schedules = {}
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e.response}")

    return {}


def write_schedule_in_json(schedules: list[ScheduleDTO]) -> None:
    json_data = {
        const.FIELD_CASTINGS: []
    }

    for schedule in schedules:
        json_data[const.FIELD_CASTINGS].append(schedule.to_dict())

    try:
        with open(const.SCHEDULE_JSON_FILE, 'w') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"IO error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def parse_schedule(raw_data: dict) -> list[ScheduleDTO]:
    raw_schedules = raw_data['data']['dataList']
    schedules = []

    for raw_schedule in raw_schedules:
        schedules.append(ScheduleDTOBuilder.build(raw_schedule))

    return schedules


today = datetime.now().strftime("%Y%m%d")
interpark_schedules = fetch_schedule_from_interpark(today)

if not interpark_schedules:
    sys.exit()

my_schedules = parse_schedule(interpark_schedules)
write_schedule_in_json(my_schedules)
