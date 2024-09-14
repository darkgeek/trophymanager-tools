from utils.DataLoaders import load_players, load_lineup_data, load_lineup_json
from model.Lineup import LineupParty, Lineup, LineupPlayer
from report.TacticDuelReport import TacticDuelReport
from model.AttackingStyle import AttackingStyle
from model.DuelReport import DuelPlayer, GkDuelReport

def printDuelPlayers(players: [DuelPlayer]):
    for player in players:
        print(f"{player.name}: {player.position},{player.possibility}")
        print("Primary skills:")
        for skill in player.primary_skills:
            print(f"    {skill.name}:{skill.value}", end=', ')

        print("\nSecondary skills:")
        for skill in player.secondary_skills:
            print(f"    {skill.name}:{skill.value}", end=', ')

        print("\n")


def printGkDuelReports(reports: [GkDuelReport]):
    for report in reports:
        print(f"{report.finish_duel_style.style.name}: {report.finish_duel_style.possibility}")
        print(report.effeftive_gk_info)


print("Loading data...")
my_players = load_players("my_players.json")
opponent_players = load_players("opponent_players.json")
opponent_lineup = load_lineup_json("opponent_lineup.json", LineupParty.AWAY)
my_lineup = load_lineup_data("my_lineup.data")
print("Done.")

print("Building report...")
directReport = TacticDuelReport().load_data(my_lineup, opponent_lineup, AttackingStyle.DIRECT,
                                            AttackingStyle.DIRECT, my_players, opponent_players).build()
print("Done.")

print("====== Attacking Report ======")
print(f"style: Direct")

print("# Assist Phase:")
print("## My assist players:")
printDuelPlayers(directReport.assist_players)

print("## Opponent defend players:")
printDuelPlayers(directReport.defend_players)

print("# Finish Phase:")
print("## My finish players:")
printDuelPlayers(directReport.finish_players)

print("## Opponent GK player:")
printGkDuelReports(directReport.gk_duel_reports)
