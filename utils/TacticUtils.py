from model.AttackingStyle import AttackingStyle
from model.Player import Player

TACTIC_POS_TO_ASSIST_POSSIBILITY_DICT = {
    "DIRECT-DR": 0.1,
    "DIRECT-DL": 0.1,
    "DIRECT-DC": 0.04,
    "DIRECT-DMR": 0.13,
    "DIRECT-DML": 0.13,
    "DIRECT-DMC": 0.13,
    "DIRECT-MR": 0.11,
    "DIRECT-ML": 0.11,
    "DIRECT-MC": 0.17,
    "DIRECT-OMR": 0.09,
    "DIRECT-OML": 0.09,
    "DIRECT-OMC": 0.11,
    "DIRECT-FC": 0.11
}

TACTIC_POS_TO_FINISH_POSSIBILITY_DICT = {
    "DIRECT-DR": 0.0,
    "DIRECT-DL": 0.0,
    "DIRECT-DC": 0.0,
    "DIRECT-DMR": 0.063,
    "DIRECT-DML": 0.063,
    "DIRECT-DMC": 0.063,
    "DIRECT-MR": 0.125,
    "DIRECT-ML": 0.125,
    "DIRECT-MC": 0.125,
    "DIRECT-OMR": 0.188,
    "DIRECT-OML": 0.188,
    "DIRECT-OMC": 0.188,
    "DIRECT-FC": 0.25
}

TACTIC_STYLE_TO_POSSIBILITY_DICT = {
    "DIRECT-HEADER": 0.32,
    "DIRECT-NORMAL": 0.33,
    "DIRECT-LONGSHOT": 0.35
}

POS_TO_POSSIBILITY_DICT = {
    "DL": 0.205,
    "DR": 0.205,
    "DC": 0.308,
    "DMR": 0.135,
    "DML": 0.135,
    "DMC": 0.173,
    "MR": 0.058,
    "ML": 0.058,
    "MC": 0.064,
    "OMR": 0.026,
    "OML": 0.026,
    "OMC": 0.032,
    "FC": 0
}


def get_assist_possibility(style: AttackingStyle, position: str) -> float:
    return TACTIC_POS_TO_ASSIST_POSSIBILITY_DICT[style.name + "-" + position.upper()]


def get_player_detail_by_no(all_players: [Player], no: int) -> Player:
    for player in all_players:
        if player.no == no:
            return player

    return None


def get_defend_possibility(position: str) -> float:
    return POS_TO_POSSIBILITY_DICT[position.upper()]


def get_finish_possibility(style: AttackingStyle, position: str) -> float:
    return TACTIC_POS_TO_FINISH_POSSIBILITY_DICT[style.name + "-" + position.upper()]


def get_finish_style_possibility(style: AttackingStyle, finish_style: FinishStyle):
    return TACTIC_STYLE_TO_POSSIBILITY_DICT[style.name + "-" + finish_style.name]
