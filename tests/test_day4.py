"""Unit tests for day 4 submission"""
from aoc2021 import day4
from aoc2021.day4 import BingoBoard


INPUT_FILE_PATH = 'tests/inputs/day4_tst.txt'

TEST_FILE_EXPECTED_NUMBERS = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14,
                              21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
TEST_FILE_EXPECTED_BOARDS = [
    BingoBoard(day4.BINGO_BOARD_DIM, [[22, 13, 17, 11,  0],
                                      [8,  2, 23,  4, 24],
                                      [21, 9, 14, 16,  7],
                                      [6, 10,  3, 18,  5],
                                      [1, 12, 20, 15, 19]]),
    BingoBoard(day4.BINGO_BOARD_DIM, [[3, 15,  0,  2, 22],
                                      [9, 18, 13, 17,  5],
                                      [19,  8,  7, 25, 23],
                                      [20, 11, 10, 24,  4],
                                      [14, 21, 16, 12,  6]]),
    BingoBoard(day4.BINGO_BOARD_DIM, [[14, 21, 17, 24,  4],
                                      [10, 16, 15,  9, 19],
                                      [18,  8, 23, 26, 20],
                                      [22, 11, 13,  6,  5],
                                      [2, 0, 12,  3,  7]])]

# pylint: disable=protected-access


def test_process_inputs():
    """Tests the input processing function to make sure each line is converted
    into the proper list of tuples
    """
    expected_numbers = TEST_FILE_EXPECTED_NUMBERS
    expected_boards = TEST_FILE_EXPECTED_BOARDS
    actual_numbers, actual_boards = day4._process_inputs(INPUT_FILE_PATH)
    assert expected_numbers == actual_numbers
    assert expected_boards == actual_boards


def test_solution():
    """Tests the whole integrated solution with a test input file
    """
    expected_output = [4512, 1924]
    actual_output = day4.solution(INPUT_FILE_PATH)
    assert actual_output == expected_output
