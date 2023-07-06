"""
Tests for the add module
"""

# pylint: disable=import-error
from module import add


def test_two_plus_two():
    """ test the add module """
    assert add.add(2, 2) == 4
