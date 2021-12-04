"""Unit tests for day 3 submission"""
import aoc2021.day3 as day3


INPUT_FILE_PATH = 'tests/inputs/day3_tst.txt'

TEST_FILE_EXPECTED_INPUT = ['00100',
                            '11110',
                            '10110',
                            '10111',
                            '10101',
                            '01111',
                            '00111',
                            '11100',
                            '10000',
                            '11001',
                            '00010',
                            '01010']

TEST_FILE_EXPECTED_STATS = ([5, 7, 4, 5, 7], [7, 5, 8, 7, 5])
TEST_FILE_EXPECTED_RATES = (22, 9)

# pylint: disable=protected-access


def test_process_inputs():
    """Tests the input processing function to make sure each line is converted
    into the proper list of tuples
    """
    expected_outputs = TEST_FILE_EXPECTED_INPUT
    actual_outputs = day3._process_inputs(INPUT_FILE_PATH)
    assert expected_outputs == actual_outputs


def test_calculate_position_statistics():
    """Tests that position statistics for each digit are generated correctly
    """
    diagnostic_inputs = TEST_FILE_EXPECTED_INPUT
    expected_output = TEST_FILE_EXPECTED_STATS
    actual_output = day3._calculate_position_statistics(diagnostic_inputs)
    assert expected_output == actual_output


def test_calculate_gamma_and_epsilon():
    """Tests gamma and epsilon calculation
    """
    zero_counts, one_counts = TEST_FILE_EXPECTED_STATS
    expected_output = TEST_FILE_EXPECTED_RATES
    actual_output = day3._calculate_gamma_and_epsilon(zero_counts, one_counts)
    assert expected_output == actual_output


def test_solution():
    """Tests the whole integrated solution with a test input file
    """
    expected_output = [198, 230]
    actual_output = day3.solution(INPUT_FILE_PATH)
    assert actual_output == expected_output
