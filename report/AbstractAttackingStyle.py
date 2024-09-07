from model.AttackingStyle import AttackingStyle
from model.Lineup import Lineup
from model.Player import Player


class AbstractAttckingStyle:
    def load_data(self, my_lineup: Lineup, opponent_lineup: Lineup, my_attacking_style: AttackingStyle, opponent_attacking_style: AttackingStyle, my_players: [Player], opponent_players: [Player]) -> AbstractAttckingStyleReport:
        pass

    def build():
        pass
