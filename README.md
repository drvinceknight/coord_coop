# coord_coop

A library to replicate the coordinated cooperation game presented in https://www.frontiersin.org/articles/10.3389/fevo.2018.00062/full


## Development

Install development requirements:

    $ pip install pytest
    $ pip install mypy
    $ pip install isort

Install in developer mode:

    $ python setup.py develop

Run the test suit:

    $ pytest

Run the type hint checker:

    $ mypy src/coord_coop

Run the black code formatter:

    $ black -l 80

Run the isort import sorter:

    $ isort -rc .
