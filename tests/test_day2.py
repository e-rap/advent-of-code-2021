"""Unit tests for day 2 submission"""
import aoc2021.day2 as day2

INPUT_FILE_PATH = 'tests/inputs/day2_tst.txt'

# pylint: disable=protected-access


def test_generate_input():
    """Tests the input processing function to make sure each line is converted
    into the proper list of tuples
    """
    expected_outputs = [('forward', '3'), ('down', '5'), ('down', '9'),
                        ('forward', '6'), ('down', '2'), ('forward', '2'), ('up', '1')]
    actual_outputs = day2._process_inputs(INPUT_FILE_PATH)
    assert expected_outputs == actual_outputs


def test_calculate_sub_position():
    """Tests that the horizontal position and depth are calculated correctly
    """
    expected_output = (11, 15)
    planned_course = [('forward', '3'), ('down', '5'), ('down', '9'),
                      ('forward', '6'), ('down', '2'), ('forward', '2'), ('up', '1')]
    actual_output = day2._calculate_sub_position(planned_course)
    assert expected_output == actual_output


def test_solution():
    """Tests the whole integrated solution with a test input file
    """
    expected_output = 11*15
    actual_output = day2.solution(INPUT_FILE_PATH)
    assert actual_output == expected_output
