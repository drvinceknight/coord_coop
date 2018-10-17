import random
from coord_coop.actions import C, D
from typing import Sequence

def decide_action(p: float):
    """
    Return an action C with probability p otherwise returns D.
    """
    if p == 0:
        return D
    if p == 1:
        return C
    return C if random.random() < p else D

class BaseStrategy():
    """
    A base strategy class. Defined by a sequence of probabilities which maps
    number of cooperators to a probability of cooperating.
    """
    def __init__(self, sequence: Sequence[float], p: float):
        """
        Initialises an instance of the class:

        - sequence: an iterable of probabilities of cooperating.
        - p: probability of cooperating as an initial action.
        """
        self.sequence = sequence
        self.action = decide_action(p=p)

    def update_action(self, players: Sequence):
        """
        Given a list of players: updates the action of a given player according
        to number of players currently cooperating.
        """
        coordination_count = sum(player.action == C for player in players)
        self.action = decide_action(p=self.sequence[coordination_count])
