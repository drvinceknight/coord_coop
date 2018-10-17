import random

import coord_coop as cc
from coord_coop.actions import C, D
from coord_coop.negotiation import get_actions, negotiate, update_random_player


def test_update_random_player_and_get_actions():
    players = (
        cc.strategies.SingleBoundaryStrategy(
            boundary=1, number_of_players=3, p=0
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=1, number_of_players=3, p=1
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=2, number_of_players=3, p=1
        ),
    )
    assert get_actions(players) == (D, C, C)
    random.seed(0)
    assert update_random_player(players) is True
    assert get_actions(players) == (C, C, C)
    assert update_random_player(players) is False

    players = (
        cc.strategies.SingleBoundaryStrategy(
            boundary=1, number_of_players=3, p=0
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=1, number_of_players=3, p=1
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=2, number_of_players=3, p=1
        ),
    )
    assert get_actions(players) == (D, C, C)
    random.seed(1)
    assert update_random_player(players) is True
    assert get_actions(players) == (D, C, D)
    assert update_random_player(players) is True
    assert get_actions(players) == (C, C, D)
    assert update_random_player(players) is True
    assert get_actions(players) == (C, C, C)
    assert update_random_player(players) is False


def test_negotiate():
    players = (
        cc.strategies.SingleBoundaryStrategy(
            boundary=1, number_of_players=3, p=0
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=1, number_of_players=3, p=1
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=2, number_of_players=3, p=1
        ),
    )
    random.seed(0)
    assert negotiate(players) == [(D, C, C), (C, C, C)]

    players = (
        cc.strategies.SingleBoundaryStrategy(
            boundary=1, number_of_players=3, p=0
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=1, number_of_players=3, p=1
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=2, number_of_players=3, p=1
        ),
    )
    random.seed(2)
    assert negotiate(players) == [(D, C, C), (D, C, D), (D, D, D)]
