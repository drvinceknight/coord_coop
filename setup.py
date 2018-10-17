from setuptools import setup, find_packages

# Read in the version number
# exec(open('src/coord_coop/version.py', 'r').read())

setup(
    name="cood_coop",
    # version=__version__,
    # install_requires=requirements,
    author="Vince Knight",
    author_email=("knightva@cardiff.ac.uk"),
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="",
    license="The MIT License (MIT)",
)
