import unittest
import pytest

from benfords_law_utils.utils import calculate_benford_stats


def test_calculate_benford_stats_for_empty_input():
    counts, ratios, total_count = calculate_benford_stats([])
    assert(total_count) == 0
    assert(ratios) == [0] * 9
    assert(counts) == [0] * 9


def test_calculate_benford_stats_for_single_input():
    counts, ratios, total_count = calculate_benford_stats([1234])
    assert(total_count) == 1
    assert(ratios) == [1, 0, 0, 0, 0, 0, 0, 0, 0]
    assert(counts) == [1, 0, 0, 0, 0, 0, 0, 0, 0]


def test_calculate_benford_stats_for_uniform_input():
    counts, ratios, total_count = calculate_benford_stats(
        [111, 222, 333, 444, 555, 666, 777, 888, 999]
    )
    assert(total_count) == 9
    expected_ratio = 1 / 9
    assert(ratios) == [expected_ratio] * 9
    assert(counts) == [1] * 9


def test_calculate_benford_stats_for_simple_input():
    counts, ratios, total_count = calculate_benford_stats(
        [111, 3000, 701234, 8675309, 8888]
    )
    assert(total_count) == 5
    assert(ratios) == [.2, 0, .2, 0, 0, 0, .2, .4, 0]
    assert(counts) == [1, 0, 1, 0, 0, 0, 1, 2, 0]
