import random
from coord_coop.actions import C, D

class BaseStrategy():
    def __init__(self, sequence, p):
        self.sequence = sequence
        self.action = C if random.random() < p else D

    def update_action(self, players):
        coordination_count = sum(player.action == C for player in players)
        self.action = self.sequence[coordination_count]
