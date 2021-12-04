"""Unit tests for day 2 submission"""
import operator
from functools import reduce

import aoc2021.day2 as day2


INPUT_FILE_PATH = 'tests/inputs/day2_tst.txt'

TEST_FILE_EXPECTED_INPUT = [('forward', '5'), ('down', '5'), ('forward', '8'),
                            ('up', '3'), ('down', '8'), ('forward', '2')]

EXPECTED_POSITION_OUTPUT = (15, 10)
EXPECTED_POSITION_AIM_OUTPUT = (15, 60)


def multiply(__iterable):
    """Return the multiplication of a 'start' value (default: 1) plus an iterable
    of numbers

    When the iterable is empty, return the start value. This function is intended
    specifically for use with numeric values and may reject non-numeric types.
    """
    return reduce(operator.mul, __iterable)


# pylint: disable=protected-access


def test_process_inputs():
    """Tests the input processing function to make sure each line is converted
    into the proper list of tuples
    """
    expected_outputs = TEST_FILE_EXPECTED_INPUT
    actual_outputs = day2._process_inputs(INPUT_FILE_PATH)
    assert expected_outputs == actual_outputs


def test_calculate_sub_position():
    """Tests that the horizontal position and depth are calculated correctly
    """
    expected_output = EXPECTED_POSITION_OUTPUT
    planned_course = TEST_FILE_EXPECTED_INPUT
    actual_output = day2._calculate_sub_position(planned_course)
    assert expected_output == actual_output


def test_calculate_sub_position_aim():
    """Tests that the horizontal position and depth are calculated correctly when
    using aim
    """
    expected_output = EXPECTED_POSITION_AIM_OUTPUT
    planned_course = TEST_FILE_EXPECTED_INPUT
    actual_output = day2._calculate_sub_position_aim(planned_course)
    assert expected_output == actual_output


def test_solution():
    """Tests the whole integrated solution with a test input file
    """
    expected_output = [multiply(EXPECTED_POSITION_OUTPUT),
                       multiply(EXPECTED_POSITION_AIM_OUTPUT)]
    actual_output = day2.solution(INPUT_FILE_PATH)
    assert actual_output == expected_output
