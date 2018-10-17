import random
from typing import Sequence

from .strategies import BaseStrategy


def get_actions(players: Sequence[BaseStrategy]) -> Sequence[str]:
    """
    Obtain the actions of all the players.
    """
    return tuple([player.action for player in players])


def update_random_player(players: Sequence[BaseStrategy]) -> bool:
    """
    Pick a random player to update their action based on underlying sequence. If
    picked player does not update another player will be picked.

    Returns a boolean which is True if a player has updated. If they no player
    updates then False is returned.
    """
    number_of_players = len(players)
    player_indices = list(range(number_of_players))
    random.shuffle(player_indices)
    for i in player_indices:
        player = players[i]
        others = tuple([player for j, player in enumerate(players) if j != i])
        thought = player.action
        player.update_action(players=others)
        if thought != player.action:
            return True
    return False


def negotiate(players: Sequence[BaseStrategy]) -> Sequence[Sequence[str]]:
    """
    Negotiate the coordination cooperation game. Returns the history of the
    negotiation.
    """
    history = [get_actions(players)]
    while update_random_player(players):
        history.append(get_actions(players))
    return history
