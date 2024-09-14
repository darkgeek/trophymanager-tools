import copy
from utils.TacticUtils import get_assist_possibility, get_player_detail_by_no, get_defend_possibility, get_finish_possibility, get_finish_style_possibility, get_required_duel_skills
from model.FinishStyle import FinishStyle
from model.AttackingStyle import AttackingStyle
from model.Lineup import Lineup
from model.Player import Player
from model.DuelReport import AttackingDuelReport, DuelPlayer, DuelSkill, FinishDuelStyle, GkDuelReport
from operator import attrgetter


class Direct:
    def load_data(self, my_lineup: Lineup, opponent_lineup: Lineup, my_attacking_style: AttackingStyle, opponent_attacking_style: AttackingStyle, my_players: [Player], opponent_players: [Player]):
        self.my_lineup = my_lineup
        self.opponent_lineup = opponent_lineup
        self.my_attacking_style = my_attacking_style
        self.opponent_attacking_style = opponent_attacking_style
        self.my_players = my_players
        self.opponent_players = opponent_players
        return self

    def build(self):
        assist_players = self.buildAssistPlayers()
        defend_players = self.buildDefendPlayers()
        finish_players = self.buildFinishPlayers()
        gk_duel_reports = self.buildGkDuelReports()
        return AttackingDuelReport(style=self.my_attacking_style, assist_players=assist_players, defend_players=defend_players, finish_players=finish_players, gk_duel_reports=gk_duel_reports)

    def buildAssistPlayers(self):
        assist_players = []
        for lineup_player in self.my_lineup.players:
            if lineup_player.position == "gk" or lineup_player.position.startswith("sub"):
                continue

            player = get_player_detail_by_no(self.my_players, lineup_player.no)
            possibility = get_assist_possibility(
                self.my_attacking_style, lineup_player.position)
            primary_skills = get_required_duel_skills(
                self.my_attacking_style, True, True, player)
            secondary_skills = get_required_duel_skills(
                self.my_attacking_style, True, False, player)
            assist_player = DuelPlayer(name=player.name, position=lineup_player.position,
                                       possibility=possibility, primary_skills=primary_skills, secondary_skills=secondary_skills)
            assist_players.append(assist_player)

        return assist_players

    def buildDefendPlayers(self):
        defend_players = []
        for lineup_player in self.opponent_lineup.players:
            if lineup_player.position == "gk" or lineup_player.position.startswith("sub"):
                continue

            player = get_player_detail_by_no(
                self.opponent_players, lineup_player.no)
            possibility = get_defend_possibility(lineup_player.position)
            primary_skills = get_required_duel_skills(
                self.my_attacking_style, False, True, player)
            secondary_skills = get_required_duel_skills(
                self.my_attacking_style, False, False, player)

            defend_player = DuelPlayer(name=player.name, position=lineup_player.position,
                                       possibility=possibility, primary_skills=primary_skills, secondary_skills=secondary_skills)
            defend_players.append(defend_player)

        return sorted(defend_players, key=attrgetter("possibility"), reverse=True)

    def buildFinishPlayers(self):
        finish_players = []
        for lineup_player in self.my_lineup.players:
            if lineup_player.position == "gk" or lineup_player.position.startswith("sub"):
                continue

            player = get_player_detail_by_no(self.my_players, lineup_player.no)
            possibility = get_finish_possibility(
                self.my_attacking_style, lineup_player.position)
            primary_skills = [DuelSkill(name="heading", value=player.heading, formation_bonus=0.0, routine_bonus=0.0), DuelSkill(name="technique", value=player.technique, formation_bonus=0.0, routine_bonus=0.0), DuelSkill(
                name="finishing", value=player.finishing, formation_bonus=0.0, routine_bonus=0.0), DuelSkill(name="longshots", value=player.longshots, formation_bonus=0.0, routine_bonus=0.0)]
            secondary_skills = [DuelSkill(
                name="setpieces", value=player.setpieces, formation_bonus=0.0, routine_bonus=0.0)]

            finish_player = DuelPlayer(name=player.name, position=lineup_player.position,
                                       possibility=possibility, primary_skills=primary_skills, secondary_skills=secondary_skills)
            finish_players.append(finish_player)

        return sorted(finish_players, key=attrgetter("possibility"), reverse=True)

    def buildGkDuelReports(self):
        gk_duel_reports = []
        for lineup_player in self.opponent_lineup.players:
            if lineup_player.position != "gk" or lineup_player.position.startswith("sub"):
                continue

            player = get_player_detail_by_no(self.my_players, lineup_player.no)
            for finish_style in FinishStyle:
                finish_duel_style = FinishDuelStyle(
                    style=finish_style, possibility=get_finish_style_possibility(self.my_attacking_style, finish_style))
                effeftive_gk_info = copy.deepcopy(player)

                report = GkDuelReport(
                    finish_duel_style=finish_duel_style, effeftive_gk_info=effeftive_gk_info)
                gk_duel_reports.append(report)

        return gk_duel_reports
