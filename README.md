[![Build Status](https://travis-ci.org/drvinceknight/coord_coop.svg?branch=master)](https://travis-ci.org/drvinceknight/coord_coop)
[![Coverage Status](https://coveralls.io/repos/github/drvinceknight/coord_coop/badge.svg?branch=master)](https://coveralls.io/github/drvinceknight/coord_coop?branch=master)

# coord_coop

A library to replicate the coordinated cooperation game presented in https://www.frontiersin.org/articles/10.3389/fevo.2018.00062/full

## Usage

Here is an example showing a single version of the negotiation for 3 boundary
types players:

    >>> import random
    >>> import coord_coop as cc
    >>> random.seed(0)
    >>> players = (
    ...     cc.strategies.SingleBoundaryStrategy(
    ...         boundary=1, number_of_players=3, p=0
    ...     ),
    ...     cc.strategies.SingleBoundaryStrategy(
    ...         boundary=1, number_of_players=3, p=1
    ...     ),
    ...     cc.strategies.SingleBoundaryStrategy(
    ...         boundary=2, number_of_players=3, p=1
    ...     ),
    ... )
    >>> cc.negotiate(players)
    [('D', 'C', 'C'), ('C', 'C', 'C')]
    >>> cc.utility(players, r=3, c=1)
    (2.0, 2.0, 2.0)

## Development

Install development requirements:

    $ pip install pytest
    $ pip install pytest-cov
    $ pip install mypy
    $ pip install isort

Install in developer mode:

    $ python setup.py develop

Run the test suit:

    $ pytest

Run the doctests:

    $ python -m doctest README.md

Run the type hint checker:

    $ mypy src/coord_coop

Run the black code formatter:

    $ black -l 80

Run the isort import sorter:

    $ isort -rc .
