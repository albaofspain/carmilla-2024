import re

from week import Week


def convert_date_format(date_str):
    # 정규식을 사용하여 연도 부분(앞의 4자리 숫자)을 제거하고 나머지 부분을 '/'로 구분합니다.
    converted_date = re.sub(r'^(\d{4})(\d{2})(\d{2})$', r'\2/\3', date_str)
    return converted_date

# 예시 사용
date_str = '20240704'
formatted_date = convert_date_format(date_str)
print(formatted_date)  # 출력: 07/04


rr = "fine"

a = "0"

aa = Week(a)
print(aa.get_kr_name())
