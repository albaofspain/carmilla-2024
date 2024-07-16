import time
from datetime import datetime, timedelta


def fetch_kst_datetime() -> str:
    machine_timezone = time.tzname[time.localtime().tm_isdst]
    today = datetime.now()

    if machine_timezone != "KST":
        today = today + timedelta(hours=9)

    return today.strftime("%Y%m%d")
