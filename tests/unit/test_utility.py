import coord_coop as cc
from coord_coop.utility import utility


def test_utility():
    players = (
        cc.strategies.SingleBoundaryStrategy(
            boundary=0, number_of_players=2, p=0
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=0, number_of_players=2, p=1
        ),
    )
    assert utility(players=players, r=1, c=3) == (1.5, -1.5)
    assert utility(players=players, r=1, c=1) == (0.5, -0.5)

    players = (
        cc.strategies.SingleBoundaryStrategy(
            boundary=0, number_of_players=2, p=0
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=0, number_of_players=2, p=0
        ),
    )
    assert utility(players=players, r=1, c=3) == (0, 0)
    assert utility(players=players, r=1, c=0) == (0, 0)

    players = (
        cc.strategies.SingleBoundaryStrategy(
            boundary=0, number_of_players=2, p=1
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=0, number_of_players=2, p=1
        ),
        cc.strategies.SingleBoundaryStrategy(
            boundary=0, number_of_players=2, p=0
        ),
    )
    assert utility(players=players, r=1, c=3) == (-1, -1, 2)
