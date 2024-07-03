import const


class ScheduleDTO:
    def __init__(self, play_date, play_time, carmilla, laura, nick, spielsdorf):
        self.play_date = play_date
        self.play_time = play_time
        self.carmilla = carmilla
        self.laura = laura
        self.nick = nick
        self.spielsdorf = spielsdorf

    def to_dict(self) -> dict:
        return {
            const.FIELD_PLAYDATE: self.play_date,
            const.FIELD_PLAYTIME: self.play_time,
            const.EN_CARMILLA: self.carmilla,
            const.EN_LAURA: self.laura,
            const.EN_NICK: self.nick,
            const.EN_SPIELSDORF: self.spielsdorf
        }


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
            data[const.FIELD_PLAYTIME],
            carmilla,
            laura,
            nick,
            spielsdorf
        )
