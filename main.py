from utils.FileUtils import readFileAsJson
from model.Player import Player


def load_players(players_data_file: str) -> []:
    my_players_raw_data = readFileAsJson(players_data_file)
    post = my_players_raw_data["post"]

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


my_players = load_players("my_players.json")
print(my_players)
