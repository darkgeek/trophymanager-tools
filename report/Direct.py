from report.AbstractAttackingStyle import AbstractAttackingStyle
from utils.TacticUtils import get_assist_possibility, get_player_detail_by_no
from model.FinishStyle import FinishStyle


class Direct(AbstractAttckingStyle):
    def load_data(self, my_lineup: Lineup, opponent_lineup: Lineup, my_attacking_style: AttackingStyle, opponent_attacking_style: AttackingStyle, my_players: [Player], opponent_players: [Player]) -> AbstractAttckingStyleReport:
        self.my_lineup = my_lineup
        self.opponent_lineup = opponent_lineup
        self.my_attacking_style = my_attacking_style
        self.opponent_attacking_style = opponent_attacking_style
        self.my_players = my_players
        self.opponent_players = opponent_players

    def build():
        assist_players = buildAssistPlayers()
        defend_players = buildDefendPlayers()
        finish_players = buildFinishPlayers()
        gk_duel_reports = buildGkDuelReports()

        return AttackingDuelReport(style=my_attacking_style, assist_players=assist_players, defend_players=defend_players, finish_players=finish_players, gk_duel_reports=gk_duel_reports)

    def buildAssistPlayers():
        assist_players = []
        for lineup_player in my_lineup.players:
            player = get_player_detail_by_no(my_players, lineup_player.no)
            possibility = get_assist_possibility(
                my_attacking_style, lineup_player.position)
            primary_skills = [DuelSkill(name="pace", value=player.pace, formation_bonus=0.0, routine_bonus=0.0),
                              DuelSkill(name="technique", value=player.technique, formation_bonus=0.0, routine_bonus=0.0)]
            secondary_skills = [DuelSkill(name="passing", value=player.passing, formation_bonus=0.0, routine_bonus=0.0),
                                DuelSkill(name="workrate", value=player.workrate,
                                          formation_bonus=0.0, routine_bonus=0.0),
                                DuelSkill(name="positioning", value=player.positioning, formation_bonus=0.0, routine_bonus=0.0)]

            assist_player = DuelPlayer(name=player.name, position=lineup_player.position,
                                       possibility=possibility, primary_skills=primary_skills, secondary_skills=secondary_skills)
            assist_players.append(assist_player)

        return assist_players

    def buildDefendPlayers():
        defend_players = []
        for lineup_player in opponent_lineup.players:
            player = get_player_detail_by_no(
                opponent_players, lineup_player.no)
            possibility = get_defend_possibility(lineup_player.position)
            primary_skills = [DuelSkill(name="marking", value=player.marking, formation_bonus=0.0, routine_bonus=0.0), DuelSkill(
                name="workrate", value=player.workrate, formation_bonus=0.0, routine_bonus=0.0)]
            secondary_skills = [DuelSkill(name="positioning", value=player.positioning, formation_bonus=0.0, routine_bonus=0.0), DuelSkill(
                name="pace", value=player.pace, formation_bonus=0.0, routine_bonus=0.0), DuelSkill(name="tackling", value=player.tackling, formation_bonus=0.0, routine_bonus=0.0)]

            defend_player = DuelPlayer(name=player.name, position=lineup_player.position,
                                       possibility=possibility, primary_skills=primary_skills, secondary_skills=secondary_skills)
            defend_players.append(defend_player)

        return defend_players

    def buildFinishPlayers():
        finish_players = []
        for lineup_player in my_lineup.players:
            player = get_player_detail_by_no(my_players, lineup_player.no)
            possibility = get_finish_possibility(
                my_attacking_style, lineup_player.position)
            primary_skills = [DuelSkill(name="heading", value=player.heading, formation_bonus=0.0, routine_bonus=0.0), DuelSkill(name="technique", value=player.technique, formation_bonus=0.0, routine_bonus=0.0), DuelSkill(
                name="finishing", value=player.finishing, formation_bonus=0.0, routine_bonus=0.0), DuelSkill(name="longshots", value=player.longshots, formation_bonus=0.0, routine_bonus=0.0)]
            secondary_skills = [DuelSkill(
                name="setpieces", value=player.setpieces, formation_bonus=0.0, routine_bonus=0.0)]

            finish_player = DuelPlayer(name=player.name, position=lineup_player.position,
                                       possibility=possibility, primary_skills=primary_skills, secondary_skills=secondary_skills)
            finish_players.append(finish_player)

        return finish_players

    def buildGkDuelReports():
        gk_duel_reports = []
        for lineup_player in opponent_lineup.players:
            if lineup_player.position != "gk":
                continue

            player = get_player_detail_by_no(my_players, lineup_player.no)
            for finish_style in FinishStyle:
                finish_duel_style = FinishDuelStyle(
                    style=finish_style, possibility=get_finish_style_possibility(my_attacking_style, finish_style))
                effeftive_gk_info = player

                report = GkDuelReport(
                    finish_duel_style=finish_duel_style, effeftive_gk_info=effeftive_gk_info)
                gk_duel_reports.append(report)

        return gk_duel_reports
