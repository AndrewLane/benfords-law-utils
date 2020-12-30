import unittest
import pytest

from benfords_law_utils.utils import calculate_benford_stats, ascii_art_bar_graph


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


def test_ascii_art_bar_graph():
    _, ratios, __ = calculate_benford_stats(
        [111, 3000, 701234, 8675309, 8888]
    )
    bar_graph = ascii_art_bar_graph(ratios, 20)
    assert(bar_graph) == """**********             Leading 1 Ratio: 20.000%
               ^       Expected Ratio:  30.103%

                       Leading 2 Ratio: 0.000%
        ^              Expected Ratio:  17.609%

**********             Leading 3 Ratio: 20.000%
      ^                Expected Ratio:  12.494%

                       Leading 4 Ratio: 0.000%
    ^                  Expected Ratio:  9.691%

                       Leading 5 Ratio: 0.000%
   ^                   Expected Ratio:  7.918%

                       Leading 6 Ratio: 0.000%
   ^                   Expected Ratio:  6.695%

**********             Leading 7 Ratio: 20.000%
  ^                    Expected Ratio:  5.799%

********************   Leading 8 Ratio: 40.000%
  ^                    Expected Ratio:  5.115%

                       Leading 9 Ratio: 0.000%
  ^                    Expected Ratio:  4.576%

"""
