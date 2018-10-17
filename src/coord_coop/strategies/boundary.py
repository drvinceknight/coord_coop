import random
from coord_coop.actions import C, D
from .base import BaseStrategy

class SingleBoundaryStrategy():
    def __init__(self, boundary, number_of_players, p):
        self.sequence = tuple([D if i < boundary else C for i in range(number_of_players)])
        self.action = C if random.random() < p else D
