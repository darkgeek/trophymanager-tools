from utils.FileUtils import readFileAsJson, readFileByLines
from model.Player import Player
from model.Lineup import Lineup, LineupParty, LineupPlayer


def load_players(players_data_file: str) -> []:
    players_raw_data = readFileAsJson(players_data_file)
    post = players_raw_data["post"]

    players = []
    for player_id, player_raw in post.items():
        player = Player(no=player_raw["no"],
                        name=player_raw["player_name_nonick"],
                        position=player_raw["player_position"],
                        strength=player_raw["strength"],
                        stamina=player_raw["stamina"],
                        pace=player_raw["pace"],
                        marking=player_raw["marking"],
                        tackling=player_raw["tackling"],
                        workrate=player_raw["workrate"],
                        positioning=player_raw["positioning"],
                        crossing=player_raw["crossing"],
                        technique=player_raw["technique"],
                        passing=player_raw["passing"],
                        heading=player_raw["heading"],
                        longshots=player_raw["longshots"],
                        finishing=player_raw["finishing"],
                        setpieces=player_raw["setpieces"],
                        handling=player_raw["handling"],
                        reflexes=player_raw["reflexes"],
                        oneonones=player_raw["oneonones"],
                        arialability=player_raw["arialability"],
                        jumping=player_raw["jumping"],
                        kicking=player_raw["kicking"],
                        throwing=player_raw["throwing"],
                        communication=player_raw["communication"],
                        rutine=player_raw["rutine"])
        players.append(player)

    return players


def load_lineup_json(lineup_json_file: str, party: LineupParty) -> Lineup:
    lineup_raw_data = readFileAsJson(lineup_json_file)
    lineup_raw = lineup_raw_data["lineup"]
    lineup_for_party_raw = lineup_raw[party.value]

    lineup_players = []
    for player_id, player_raw in lineup_for_party_raw.items():
        player = LineupPlayer(
            no=player_raw["no"], position=player_raw["position"])
        lineup_players.append(player)

    return Lineup(players=lineup_players)


def load_lineup_data(lineup_data_file: str) -> Lineup:
    lineup_raw_data = readFileByLines(lineup_data_file)

    players = []
    for line in lineup_raw_data:
        line = line.replace("\n", "")
        parts = line.split()
        player = LineupPlayer(no=parts[1], position=parts[0])
        players.append(player)

    return Lineup(players=players)


my_players = load_players("my_players.json")
print(my_players)

opponent_lineup = load_lineup_json("opponent_lineup.json", LineupParty.AWAY)
print(opponent_lineup)

my_lineup = load_lineup_data("my_lineup.data")
print(my_lineup)
