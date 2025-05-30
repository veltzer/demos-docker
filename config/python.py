""" python requirements for this project """

from typing import List


config_requires: List[str] = []
dev_requires: List[str] = []
install_requires: List[str] = []
build_requires: List[str] = [
    "flask",
    "mysql-connector-python",
    "pyvardump",
    "requests",
    "types-requests",

    "pymakehelper",
    "pypitools",
    "pycmdtools",

    "black",

    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pyflakes",
    "mypy",
    "pydmt",
    "pyclassifiers",
]
test_requires: List[str] = []
requires = config_requires + install_requires + build_requires + test_requires
