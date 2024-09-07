from dataclasses import dataclass
from model.AttackingStyle import AttackingStyle
from model.FinishStyle import FinishStyle
from model.Player import Player


@dataclass
class DuelSkill:
    name: str
    value: int
    formation_bonus: float
    routine_bonus: float


@dataclass
class DuelPlayer:
    name: str
    position: str
    possibility: float
    primary_skills: [DuelSkill]
    secondary_skills: [DuelSkill]


@dataclass
class FinishDuelStyle:
    style: FinishStyle
    possibility: float


@dataclass
class GkDuelReport:
    finish_duel_style: FinishDuelStyle
    effeftive_gk_info: Player


@dataclass
class AttackingDuelReport:
    style: AttackingStyle
    assist_players: [DuelPlayer]
    defend_players: [DuelPlayer]
    finish_players: [DuelPlayer]
    gk_duel_reports: [GkDuelReport]
