import unittest
import pytest

from benfords_law_utils.utils import hello_world


def test_hello_world():
    assert hello_world() == "Hello, benfords-law-utils!"
