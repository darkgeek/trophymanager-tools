from utils.DataLoaders import load_players, load_lineup_data, load_lineup_json
from model.Lineup import LineupParty, Lineup, LineupPlayer
from report.TacticDuelReport import TacticDuelReport
from model.AttackingStyle import AttackingStyle

my_players = load_players("my_players.json")
print(my_players)

opponent_players = load_players("opponent_players.json")
print(opponent_players)

opponent_lineup = load_lineup_json("opponent_lineup.json", LineupParty.AWAY)
print(opponent_lineup)

my_lineup = load_lineup_data("my_lineup.data")
print(my_lineup)

directReport = TacticDuelReport().load_data(my_lineup, opponent_lineup, AttackingStyle.DIRECT,
                                            AttackingStyle.DIRECT, my_players, opponent_players).build()
print(directReport)
