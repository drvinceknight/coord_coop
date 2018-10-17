import coord_coop as cc
from coord_coop.actions import C, D
import random

def test_base_player_random_init():
    random.seed(0)
    n = 3
    player = cc.strategies.SingleBoundaryStrategy(boundary=2,
            number_of_players=3, p=.5)
    assert player.sequence == (D, D, C)

    player = cc.strategies.SingleBoundaryStrategy(boundary=2,
            number_of_players=4, p=.5)
    assert player.sequence == (D, D, C, C)

    player = cc.strategies.SingleBoundaryStrategy(boundary=0,
            number_of_players=4, p=.5)
    assert player.sequence == (C, C, C, C)
