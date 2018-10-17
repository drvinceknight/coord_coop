import random
from coord_coop.actions import C, D

def decide_action(p):
    if p == 0:
        return D
    if p == 1:
        return C
    return C if random.random() < p else D

class BaseStrategy():
    def __init__(self, sequence, p):
        self.sequence = sequence
        self.action = decide_action(p=p)

    def update_action(self, players):
        coordination_count = sum(player.action == C for player in players)
        self.action = decide_action(p=self.sequence[coordination_count])
