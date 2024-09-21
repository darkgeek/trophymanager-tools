from utils.FileUtils import readFileAsJson, readFileByLines
from model.Player import Player
from model.Lineup import Lineup, LineupParty, LineupPlayer


def load_players(players_data_file: str) -> []:
    players_raw_data = readFileAsJson(players_data_file)
    post = players_raw_data["post"]

    players = []
    for player_id, player_raw in post.items():
        player = Player(no=int(player_raw["no"]),
                        name=player_raw["player_name_nonick"],
                        position=player_raw["player_position"],
                        strength=int(player_raw["strength"]),
                        stamina=int(player_raw["stamina"]),
                        pace=int(player_raw["pace"]),
                        marking=int(player_raw["marking"]),
                        tackling=int(player_raw["tackling"]),
                        workrate=int(player_raw["workrate"]),
                        positioning=int(player_raw["positioning"]),
                        crossing=int(player_raw["crossing"]),
                        technique=int(player_raw["technique"]),
                        passing=int(player_raw["passing"]),
                        heading=int(player_raw["heading"]),
                        longshots=int(player_raw["longshots"]),
                        finishing=int(player_raw["finishing"]),
                        setpieces=int(player_raw["setpieces"]),
                        handling=int(player_raw["handling"]),
                        reflexes=int(player_raw["reflexes"]),
                        oneonones=int(player_raw["oneonones"]),
                        arialability=int(player_raw["arialability"]),
                        jumping=int(player_raw["jumping"]),
                        kicking=int(player_raw["kicking"]),
                        throwing=int(player_raw["throwing"]),
                        communication=int(player_raw["communication"]),
                        rutine=float(player_raw["rutine"]))
        players.append(player)

    return players


def load_lineup_json(lineup_json_file: str, party: LineupParty) -> Lineup:
    lineup_raw_data = readFileAsJson(lineup_json_file)
    lineup_raw = lineup_raw_data["lineup"]
    lineup_for_party_raw = lineup_raw[party.value]

    lineup_players = []
    for player_id, player_raw in lineup_for_party_raw.items():
        player = LineupPlayer(
            no=int(player_raw["no"]), position=player_raw["position"])
        lineup_players.append(player)

    return Lineup(players=lineup_players)


def load_lineup_data(lineup_data_file: str) -> Lineup:
    lineup_raw_data = readFileByLines(lineup_data_file)

    players = []
    for line in lineup_raw_data:
        line = line.replace("\n", "")
        parts = line.split()
        player = LineupPlayer(no=int(parts[1]), position=parts[0])
        players.append(player)

    return Lineup(players=players)
