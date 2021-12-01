"""Unit tests for day 1 submission"""
import aoc2021.day1 as day1

INPUT_FILE_PATH = 'tests/inputs/day1_tst.txt'

# pylint: disable=protected-access


def test_process_input():
    """Tests the input processing function to make sure each line is converted
    into a list
    """
    expected_output = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    actual_output = day1._process_inputs(INPUT_FILE_PATH)
    assert expected_output == actual_output


def test_find_increasing_measurements():
    """_find_increasing_measurements should count all the number of increasing
    measurements (where current is > last)
    """
    increasing = ([1, 2, 3, 4], 3)
    decreasing = ([4, 3, 2, 1], 0)
    both = ([4, 5, 4, 2, 3], 2)
    same = ([3, 4, 4, 5, 6], 3)

    tests = [increasing, decreasing, both, same]

    for test_input, expected_output in tests:
        actual_output = day1._find_increasing_measurements(test_input)
        assert actual_output == expected_output


def test_sliding_window_sum():
    """make sure the sliding window sum works correctly
    """
    tests = [([1, 1, 1, 1, 1, 1], 3, [3, 3, 3, 3]),
             ([1, 2, 3, 4, 5], 2, [3, 5, 7, 9]),
             ([1, 2, 3], 4, [])]

    for test_input, window_size, expected_output in tests:
        actual_output = day1._sliding_window_sum(test_input, window_size)
        assert expected_output == actual_output


def test_solution():
    """Tests the whole integrated solution with a test input file
    """
    expected_output = (7, 5)
    actual_output = day1.solution(INPUT_FILE_PATH)
    assert actual_output == expected_output
