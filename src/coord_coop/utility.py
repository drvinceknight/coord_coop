
from .actions import C, D
from .strategies import BaseStrategy
from typing import Sequence


def utility( players: Sequence[BaseStrategy], r: float, c: float) -> Sequence[float]:
    """
    Returns a tuple of utilities for all players as defined by:

    W_C = -c  + r * k * c / n
    W_D = r * k * c / n
    """
    n = len(players)
    k = sum(player.action == C for player in players)
    return tuple(
        r * k * c / n - c * int(player.action == C) for player in players
    )
