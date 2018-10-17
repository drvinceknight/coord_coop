import random

import coord_coop as cc
from coord_coop.actions import C, D


def test_base_player_random_init():
    random.seed(0)
    n = 3
    player = cc.strategies.SingleBoundaryStrategy(
        boundary=2, number_of_players=3, p=0.5
    )
    assert player.sequence == (0, 0, 1)

    player = cc.strategies.SingleBoundaryStrategy(
        boundary=2, number_of_players=4, p=0.5
    )
    assert player.sequence == (0, 0, 1, 1)

    player = cc.strategies.SingleBoundaryStrategy(
        boundary=0, number_of_players=4, p=0.5
    )
    assert player.sequence == (1, 1, 1, 1)
