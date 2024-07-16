import re

import const
from backend.const.week import Week


class ScheduleDTO:
    def __init__(self, play_date: str, week: Week, play_time: str, carmilla: str, laura: str, nick: str, spielsdorf: str):
        self.play_date = play_date
        self.week = week
        self.play_time = play_time
        self.carmilla = carmilla
        self.laura = laura
        self.nick = nick
        self.spielsdorf = spielsdorf

    def to_dict(self) -> dict:
        return {
            const.FIELD_PLAYDATE: self.build_playdate(),
            const.FIELD_PLAYTIME: self.build_playtime(),
            const.EN_CARMILLA: self.carmilla,
            const.EN_LAURA: self.laura,
            const.EN_NICK: self.nick,
            const.EN_SPIELSDORF: self.spielsdorf
        }

    def build_playtime(self) -> str:
        converted_time = re.sub(r'(\d{2})(\d{2})', r'\1:\2', self.play_time)
        return converted_time

    def build_playdate(self) -> str:
        converted_date = re.sub(r'^(\d{4})(\d{2})(\d{2})$', r'\2/\3', self.play_date)
        return f'{converted_date}({self.week.get_kr_name()})'
        pass


# TODO: builder pattern refactoring
class ScheduleDTOBuilder:
    @staticmethod
    def build(data: dict) -> ScheduleDTO:

        castings = data[const.FIELD_CASTINGS]

        carmilla = castings[0][const.FIELD_ACTOR]
        laura = castings[1][const.FIELD_ACTOR]
        nick = castings[2][const.FIELD_ACTOR]
        spielsdorf = castings[3][const.FIELD_ACTOR]

        return ScheduleDTO(
            data[const.FIELD_PLAYDATE],
            Week(data[const.FIELD_WEEK]),
            data[const.FIELD_PLAYTIME],
            carmilla,
            laura,
            nick,
            spielsdorf
        )
