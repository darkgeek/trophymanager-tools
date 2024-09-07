from utils.DataLoaders import load_players, load_lineup_data, load_lineup_json
from model.Lineup import LineupParty, Lineup, LineupPlayer

my_players = load_players("my_players.json")
print(my_players)

opponent_lineup = load_lineup_json("opponent_lineup.json", LineupParty.AWAY)
print(opponent_lineup)

my_lineup = load_lineup_data("my_lineup.data")
print(my_lineup)
