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


def find_by_postition(players: [DuelPlayer], positions: [str]) -> [DuelPlayer]:
    candidates = []
    for player in players:
        if player.position in positions:
            candidates.append(player)

    return candidates


def printDuelPlayersReport(attack_players: [DuelPlayer], defend_players: [DuelPlayer]):
    # Duel for left
    left_attackers = find_by_postition(
        attack_players, ['oml', 'lom', 'ml', 'lm', 'dml', 'ldm', 'lb', 'dl'])
    right_defenders = find_by_postition(
        defend_players, ['rb',  'dr', 'dmr', 'rdm', 'mr', 'rm'])
    print("> Left attackers:")
    printDuelPlayers(left_attackers)
    print("vs Right defenders:")
    printDuelPlayers(right_defenders)

    # Duel for right
    right_attackers = find_by_postition(
        attack_players, ['omr', 'rom', 'rm', 'mr', 'dmr', 'rdm', 'rb', 'dr'])
    left_defenders = find_by_postition(
        defend_players, ['lb', 'dl', 'dml', 'ldm', 'lm', 'ml'])
    print("> Right attackers:")
    printDuelPlayers(right_attackers)
    print("vs Left defenders:")
    printDuelPlayers(left_defenders)

    # Duel for center
    center_attackers = find_by_postition(
        attack_players, ['omc', 'omcl', 'omcr', 'mc', 'cm', 'mcl', 'cml', 'mcr', 'cmr', 'dmc',  'cdm', 'dmcl', 'dmcr', 'cb', 'cbl', 'cbr', 'dc', 'dcl', 'dcr'])
    center_defenders = find_by_postition(defend_players, [
                                         'cb',  'cbl',  'cbr', 'dc', 'dcl', 'dcr', 'dmc', 'dmcl', 'dmcr', 'mc', 'mcl', 'mcr', 'cm', 'cml', 'cmr'])
    print("> Center attackers:")
    printDuelPlayers(center_attackers)
    print("vs Center defenders:")
    printDuelPlayers(center_defenders)


def printGkDuelReports(reports: [GkDuelReport]):
    for report in reports:
        print(
            f"{report.finish_duel_style.style.name}: {report.finish_duel_style.possibility}")
        print(report.effeftive_gk_info)


print("Loading data...")
my_players = load_players("my_players.json")
opponent_players = load_players("opponent_players.json")
opponent_lineup = load_lineup_json("opponent_lineup.json", LineupParty.AWAY)
my_lineup = load_lineup_data("my_lineup.data")
print("Done.")

my_attacking_style = AttackingStyle.WINGS
opponent_attacking_style = AttackingStyle.WINGS

print("Building attacking report...")
attacking_report = TacticDuelReport().load_data(my_lineup, opponent_lineup,
                                                my_attacking_style, opponent_attacking_style, my_players, opponent_players).build()
print("Done.")

print("Building defending report...")
defending_report = TacticDuelReport().load_data(opponent_lineup, my_lineup,
                                                opponent_attacking_style, my_attacking_style, opponent_players, my_players).build()
print("Done.")

print("====== Attacking Report ======")
print(f"style: {my_attacking_style.name}")

print("# Assist Phase:")
printDuelPlayersReport(attacking_report.assist_players,
                       attacking_report.defend_players)

print("# Finish Phase:")
print("## My finish players:")
printDuelPlayers(attacking_report.finish_players)

print("## Opponent GK player:")
printGkDuelReports(attacking_report.gk_duel_reports)

print("====== Defending Report ======")
print(f"style: {opponent_attacking_style.name}")

print("# Assist Phase:")
printDuelPlayersReport(defending_report.assist_players,
                       defending_report.defend_players)

print("# Finish Phase:")
print("## Opponent finish players:")
printDuelPlayers(defending_report.finish_players)

print("## My GK player:")
printGkDuelReports(defending_report.gk_duel_reports)
