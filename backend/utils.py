import pytz
from datetime import datetime


def get_kst_today() -> str:
    kst = pytz.timezone('Asia/Seoul')
    kst_time = datetime.now(kst)

    return kst_time.strftime("%Y%m%d")

