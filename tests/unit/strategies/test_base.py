import coord_coop as cc
from coord_coop.actions import C, D
import random

def test_base_player_random_init():
    random.seed(0)
    sequence = (C, C, D)
    player = cc.strategies.BaseStrategy(sequence=sequence, p=.5)
    assert player.sequence == sequence
    assert player.action == D

    random.seed(1)
    player = cc.strategies.BaseStrategy(sequence=sequence, p=.5)
    assert player.sequence == sequence
    assert player.action == C

    player = cc.strategies.BaseStrategy(sequence=sequence, p=0)
    assert player.sequence == sequence
    assert player.action == D

    player = cc.strategies.BaseStrategy(sequence=sequence, p=1)
    assert player.sequence == sequence
    assert player.action == C

def test_update_action():
    sequence = (C, C, D)
    players = (cc.strategies.BaseStrategy(sequence=sequence, p=0),
               cc.strategies.BaseStrategy(sequence=sequence, p=0))
    player = cc.strategies.BaseStrategy(sequence=sequence, p=0)
    assert player.action == D
    player.update_action(players=players)
    assert player.action == C

    players = (cc.strategies.BaseStrategy(sequence=sequence, p=1),
               cc.strategies.BaseStrategy(sequence=sequence, p=1))
    player.update_action(players=players)
    assert player.action == D

    players = (cc.strategies.BaseStrategy(sequence=sequence, p=1),
               cc.strategies.BaseStrategy(sequence=sequence, p=0))
    player.update_action(players=players)
    assert player.action == C
