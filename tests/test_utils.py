import unittest
import pytest
import os

from PIL import Image
from benfords_law_utils.utils import calculate_benford_stats, ascii_art_bar_graph, calculate_benford_stats_for_image, \
    get_pixel_values


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
    counts, ratios, total_count = calculate_benford_stats([111, 222, 333, 444, 555, 666, 777, 888, 999])
    assert(total_count) == 9
    expected_ratio = 1 / 9
    assert(ratios) == [expected_ratio] * 9
    assert(counts) == [1] * 9


def test_calculate_benford_stats_for_simple_input():
    counts, ratios, total_count = calculate_benford_stats([111, 3000, 701234, 8675309, 8888])
    assert(total_count) == 5
    assert(ratios) == [.2, 0, .2, 0, 0, 0, .2, .4, 0]
    assert(counts) == [1, 0, 1, 0, 0, 0, 1, 2, 0]


def test_ascii_art_bar_graph():
    _, ratios, __ = calculate_benford_stats([111, 3000, 701234, 8675309, 8888])
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


def test_calculate_benford_stats_for_image_one_black_pixel():
    verify_image_calculations("1black.bmp", 1, [1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [1])


def test_calculate_benford_stats_for_image_one_white_pixel():
    verify_image_calculations("1white.bmp", 1, [1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0],
                              [256 * 256 * 256])


def test_calculate_benford_stats_for_image_simple_2x2():
    verify_image_calculations("2x2.bmp", 4, [2, 0, 0, 1, 0, 0, 0, 0, 1], [.5, 0, 0, .25, 0, 0, 0, 0, .25],
                              [
                                  957760,  # 64 * 73 * 205
                                  13060672,  # 248 * 227 * 232
                                  4928,  # 16 * 11 * 28
                                  1533840,  # 240 * 77 * 83
    ]
    )


def test_calculate_benford_stats_for_image_for_real_image():
    image_path = get_fixture_path("maui.bmp")

    counts, ratios, total_count = calculate_benford_stats_for_image(image_path)
    assert(total_count) == 418 * 627
    assert(counts) == [59327, 55577, 43621, 34646, 30042, 12407, 10518, 9728, 6220]
    assert(ratios) == [0.22636462840441687, 0.2120563479163328, 0.16643773417885732, 0.1321932495440428,
                       0.11462649664613905, 0.04733942293750906, 0.040131865112978185, 0.03711758735682181,
                       0.0237326679029021]


def verify_image_calculations(fixture_file_name, expected_total_pixels, expected_counts,
                              expected_ratios, expected_pixel_calculations):
    image_path = get_fixture_path(fixture_file_name)

    with Image.open(image_path) as im:
        pixel_calculations = list(get_pixel_values(im))
        assert(pixel_calculations) == expected_pixel_calculations

    counts, ratios, total_count = calculate_benford_stats_for_image(image_path)
    assert(total_count) == expected_total_pixels
    assert(counts) == expected_counts
    assert(ratios) == expected_ratios


def get_fixture_path(file):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", file)
