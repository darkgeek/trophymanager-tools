from model.AttackingStyle import AttackingStyle
from model.Player import Player
from model.FinishStyle import FinishStyle
from model.DuelReport import DuelSkill

TACTIC_POS_TO_ASSIST_POSSIBILITY_DICT = {
    "DIRECT-RB": 0.1,
    "DIRECT-LB": 0.1,
    "DIRECT-CB": 0.04,
    "DIRECT-DMR": 0.13,
    "DIRECT-DML": 0.13,
    "DIRECT-DMC": 0.13,
    "DIRECT-RM": 0.11,
    "DIRECT-LM": 0.11,
    "DIRECT-CM": 0.17,
    "DIRECT-OMR": 0.09,
    "DIRECT-OML": 0.09,
    "DIRECT-OMC": 0.11,
    "DIRECT-FW": 0.11,
    "WINGS-RB": 0.26,
    "WINGS-LB": 0.26,
    "WINGS-CB": 0.0,
    "WINGS-DMR": 0.21,
    "WINGS-DML": 0.21,
    "WINGS-DMC": 0.0,
    "WINGS-RM": 0.26,
    "WINGS-LM": 0.26,
    "WINGS-CM": 0.0,
    "WINGS-OMR": 0.27,
    "WINGS-OML": 0.27,
    "WINGS-OMC": 0.0,
    "WINGS-FW": 0.0,
    "SHORTPASSING-RB": 0.0,
    "SHORTPASSING-LB": 0.0,
    "SHORTPASSING-CB": 0.09,
    "SHORTPASSING-DMR": 0.09,
    "SHORTPASSING-DML": 0.09,
    "SHORTPASSING-DMC": 0.18,
    "SHORTPASSING-RM": 0.05,
    "SHORTPASSING-LM": 0.05,
    "SHORTPASSING-CM": 0.17,
    "SHORTPASSING-OMR": 0.08,
    "SHORTPASSING-OML": 0.08,
    "SHORTPASSING-OMC": 0.17,
    "SHORTPASSING-FW": 0.17,
    "LONGBALLS-RB": 0.19,
    "LONGBALLS-LB": 0.19,
    "LONGBALLS-CB": 0.34,
    "LONGBALLS-DMR": 0.11,
    "LONGBALLS-DML": 0.11,
    "LONGBALLS-DMC": 0.17,
    "LONGBALLS-RM": 0.08,
    "LONGBALLS-LM": 0.08,
    "LONGBALLS-CM": 0.11,
    "LONGBALLS-OMR": 0.0,
    "LONGBALLS-OML": 0.0,
    "LONGBALLS-OMC": 0.0,
    "LONGBALLS-FW": 0.0,
    "THROUGHBALLS-RB": 0.10,
    "THROUGHBALLS-LB": 0.10,
    "THROUGHBALLS-CB": 0.12,
    "THROUGHBALLS-DMR": 0.06,
    "THROUGHBALLS-DML": 0.06,
    "THROUGHBALLS-DMC": 0.07,
    "THROUGHBALLS-RM": 0.09,
    "THROUGHBALLS-LM": 0.09,
    "THROUGHBALLS-CM": 0.09,
    "THROUGHBALLS-OMR": 0.09,
    "THROUGHBALLS-OML": 0.09,
    "THROUGHBALLS-OMC": 0.19,
    "THROUGHBALLS-FW": 0.19
}

TACTIC_POS_TO_FINISH_POSSIBILITY_DICT = {
    "DIRECT-RB": 0.0,
    "DIRECT-LB": 0.0,
    "DIRECT-CB": 0.0,
    "DIRECT-DMR": 0.063,
    "DIRECT-DML": 0.063,
    "DIRECT-DMC": 0.063,
    "DIRECT-RM": 0.125,
    "DIRECT-LM": 0.125,
    "DIRECT-CM": 0.125,
    "DIRECT-OMR": 0.188,
    "DIRECT-OML": 0.188,
    "DIRECT-OMC": 0.188,
    "DIRECT-FW": 0.25,
    "WINGS-RB": 0.0,
    "WINGS-LB": 0.0,
    "WINGS-CB": 0.0,
    "WINGS-DMR": 0.063,
    "WINGS-DML": 0.063,
    "WINGS-DMC": 0.063,
    "WINGS-RM": 0.125,
    "WINGS-LM": 0.125,
    "WINGS-CM": 0.125,
    "WINGS-OMR": 0.188,
    "WINGS-OML": 0.188,
    "WINGS-OMC": 0.188,
    "WINGS-FW": 0.25,
    "SHORTPASSING-RB": 0.0,
    "SHORTPASSING-LB": 0.0,
    "SHORTPASSING-CB": 0.0,
    "SHORTPASSING-DMR": 0.063,
    "SHORTPASSING-DML": 0.063,
    "SHORTPASSING-DMC": 0.063,
    "SHORTPASSING-RM": 0.125,
    "SHORTPASSING-LM": 0.125,
    "SHORTPASSING-CM": 0.125,
    "SHORTPASSING-OMR": 0.188,
    "SHORTPASSING-OML": 0.188,
    "SHORTPASSING-OMC": 0.188,
    "SHORTPASSING-FW": 0.25,
    "LONGBALLS-RB": 0.0,
    "LONGBALLS-LB": 0.0,
    "LONGBALLS-CB": 0.0,
    "LONGBALLS-DMR": 0.097,
    "LONGBALLS-DML": 0.097,
    "LONGBALLS-DMC": 0.032,
    "LONGBALLS-RM": 0.097,
    "LONGBALLS-LM": 0.097,
    "LONGBALLS-CM": 0.097,
    "LONGBALLS-OMR": 0.194,
    "LONGBALLS-OML": 0.194,
    "LONGBALLS-OMC": 0.194,
    "LONGBALLS-FW": 0.29,
    "THROUGHBALLS-RB": 0.0,
    "THROUGHBALLS-LB": 0.0,
    "THROUGHBALLS-CB": 0.0,
    "THROUGHBALLS-DMR": 0.097,
    "THROUGHBALLS-DML": 0.097,
    "THROUGHBALLS-DMC": 0.032,
    "THROUGHBALLS-RM": 0.097,
    "THROUGHBALLS-LM": 0.097,
    "THROUGHBALLS-CM": 0.097,
    "THROUGHBALLS-OMR": 0.194,
    "THROUGHBALLS-OML": 0.194,
    "THROUGHBALLS-OMC": 0.194,
    "THROUGHBALLS-FW": 0.29
}

TACTIC_STYLE_TO_POSSIBILITY_DICT = {
    "DIRECT-HEADER": 0.32,
    "DIRECT-NORMAL": 0.33,
    "DIRECT-LONGSHOT": 0.35,
    "WINGS-HEADER": 0.65,
    "WINGS-NORMAL": 0.30,
    "WINGS-LONGSHOT": 0.5,
    "SHORTPASSING-HEADER": 0.12,
    "SHORTPASSING-NORMAL": 0.53,
    "SHORTPASSING-LONGSHOT": 0.35,
    "LONGBALLS-HEADER": 0.65,
    "LONGBALLS-NORMAL": 0.30,
    "LONGBALLS-LONGSHOT": 0.05,
    "THROUGHBALLS-HEADER": 0.15,
    "THROUGHBALLS-NORMAL": 0.70,
    "THROUGHBALLS-LONGSHOT": 0.15,
}

POS_TO_POSSIBILITY_DICT = {
    "DL": 0.205,
    "DR": 0.205,
    "DC": 0.308,
    "DCR": 0.308,
    "DCL": 0.308,
    "DMR": 0.135,
    "DML": 0.135,
    "DMC": 0.173,
    "DMCL": 0.173,
    "DMCR": 0.173,
    "MR": 0.058,
    "ML": 0.058,
    "MC": 0.064,
    "MCL": 0.064,
    "MCR": 0.064,
    "OMR": 0.026,
    "OML": 0.026,
    "OMC": 0.032,
    "OMCL": 0.032,
    "OMCR": 0.032,
    "FC": 0,
    "FCL": 0,
    "FCR": 0,
}

FINISH_STYLE_TO_GK_BACKS_RATIO_DICT = {
    "HEADER": [0.0, 0.0, 0.05, 0.14, 0.07, 0.0, 0.02, 0.02],
    "NORMAL": [0.11, 0.07, 0.04, 0.0, 0.03, 0.0, 0.03, 0.02],
    "LONGSHOT": [0.06, 0.12, 0.06, 0.0, 0.02, 0.0, 0.02, 0.02]
}

ATTACKING_STYLE_TO_ASSIST_PRIMARY_SKILLS_DICT = {
    "DIRECT": ["pace", "technique"],
    "WINGS": ["pace", "crossing", "technique"],
    "SHORTPASSING": ["passing", "technique"],
    "LONGBALLS": ["passing", "crossing", "technique", "workrate", "positioning"],
    "THROUGHBALLS": ["passing", "technique", "crossing", "workrate", "positioning"]
}

ATTACKING_STYLE_TO_ASSIST_SECONDARY_SKILLS_DICT = {
    "DIRECT": ["passing", "workrate", "positioning"],
    "WINGS": ["workrate", "strength"],
    "SHORTPASSING": ["workrate", "pace", "positioning"],
    "LONGBALLS": ["heading", "strength"],
    "THROUGHBALLS": ["pace"]
}

ATTACKING_STYLE_TO_DEFEND_PRIMARY_SKILLS_DICT = {
    "DIRECT": ["marking", "workrate"],
    "WINGS": ["pace", "tackling", "marking"],
    "SHORTPASSING": ["positioning", "tackling"],
    "LONGBALLS": ["heading"],
    "THROUGHBALLS": ["pace"]
}

ATTACKING_STYLE_TO_DEFEND_SECONDARY_SKILLS_DICT = {
    "DIRECT": ["positioning", "pace", "tackling"],
    "WINGS": ["positioning", "workrate", "strength"],
    "SHORTPASSING": ["marking", "workrate"],
    "LONGBALLS": ["marking", "tackling"],
    "THROUGHBALLS": ["positioning"]
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


def get_required_skills(style: AttackingStyle, is_assist_player: bool, is_primary_skills: bool) -> [str]:
    if (is_assist_player and is_primary_skills):
        return ATTACKING_STYLE_TO_ASSIST_PRIMARY_SKILLS_DICT[style.name]

    if (is_assist_player and not is_primary_skills):
        return ATTACKING_STYLE_TO_ASSIST_SECONDARY_SKILLS_DICT[style.name]

    if (not is_assist_player and is_primary_skills):
        return ATTACKING_STYLE_TO_DEFEND_PRIMARY_SKILLS_DICT[style.name]

    if (not is_assist_player and not is_primary_skills):
        return ATTACKING_STYLE_TO_DEFEND_SECONDARY_SKILLS_DICT[style.name]


def get_required_duel_skills(style: AttackingStyle, is_assist_player: bool, is_primary_skills: bool, player: Player) -> [DuelSkill]:
    skills = get_required_skills(style, is_assist_player, is_primary_skills)

    duel_skills = []
    for skill in skills:
        duel_skills.append(DuelSkill(name=skill, value=getattr(
            player, skill), formation_bonus=0.0, routine_bonus=0.0))

    return duel_skills


def calculate_effective_value_for_gk(ori_value: int, back_players: [Player], finish_style: FinishStyle) -> int:
    gk_backs_ratio = FINISH_STYLE_TO_GK_BACKS_RATIO_DICT[finish_style.name]

    value_from_backs = 0.0
    for player in back_players:
        value_from_backs = value_from_backs + player.marking * gk_backs_ratio[0] + player.tackling * gk_backs_ratio[1] + player.positioning * gk_backs_ratio[2] + player.heading * \
            gk_backs_ratio[3] + player.strength * gk_backs_ratio[4] + player.stamina * \
            gk_backs_ratio[5] + player.pace * gk_backs_ratio[6] + \
            player.workrate * gk_backs_ratio[7]

    effeftive_value = float(ori_value) * 0.7 + \
        value_from_backs / len(back_players)

    return int(effeftive_value)


def populate_effective_values_for_gk(gk_player: Player, back_players: [Player], finish_style: FinishStyle):
    gk_player.strength = calculate_effective_value_for_gk(
        gk_player.strength, back_players, finish_style)
    gk_player.stamina = calculate_effective_value_for_gk(
        gk_player.stamina, back_players, finish_style)
    gk_player.pace = calculate_effective_value_for_gk(
        gk_player.pace, back_players, finish_style)
    gk_player.handling = calculate_effective_value_for_gk(
        gk_player.handling, back_players, finish_style)
    gk_player.oneonones = calculate_effective_value_for_gk(
        gk_player.oneonones, back_players, finish_style)
    gk_player.reflexes = calculate_effective_value_for_gk(
        gk_player.reflexes, back_players, finish_style)
    gk_player.arialability = calculate_effective_value_for_gk(
        gk_player.arialability, back_players, finish_style)
    gk_player.jumping = calculate_effective_value_for_gk(
        gk_player.jumping, back_players, finish_style)
    gk_player.communication = calculate_effective_value_for_gk(
        gk_player.communication, back_players, finish_style)
    gk_player.kicking = calculate_effective_value_for_gk(
        gk_player.kicking, back_players, finish_style)
    gk_player.throwing = calculate_effective_value_for_gk(
        gk_player.throwing, back_players, finish_style)
