from enum import Enum


class Week(Enum):
    SUNDAY = '0'
    MONDAY = '1'
    TUESDAY = '2'
    WEDNESDAY = '3'
    THURSDAY = '4'
    FRIDAY = '5'
    SATURDAY = '6'

    def get_kr_name(self) -> str:
        if self == Week.SUNDAY:
            return '일'
        elif self == Week.MONDAY:
            return '월'
        elif self == Week.TUESDAY:
            return '화'
        elif self == Week.WEDNESDAY:
            return '수'
        elif self == Week.THURSDAY:
            return '목'
        elif self == Week.FRIDAY:
            return '금'
        elif self == Week.SATURDAY:
            return '토'
