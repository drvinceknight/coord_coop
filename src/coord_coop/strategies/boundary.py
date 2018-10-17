import random
from coord_coop.actions import C, D
from .base import BaseStrategy


class SingleBoundaryStrategy:
    """
    A deterministic strategy that defects until a given number of players
    cooperate.
    """

    def __init__(self, boundary: int, number_of_players: int, p: float) -> None:
        """
        Initialises an instance of the class:

        - boundary: the number of cooperates needed before this player
          cooperates
        - number_of_players: the total number of players playing
        - p: probability of cooperating as an initial action.
        """
        self.sequence = tuple(
            [int(i >= boundary) for i in range(number_of_players)]
        )
        self.action = C if random.random() < p else D
