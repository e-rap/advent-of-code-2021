"""Day 4 Submission """
from io import TextIOWrapper
from typing import List
from typing import Optional
from typing import Tuple

BINGO_BOARD_DIM = (5, 5)


class BoardNumber():
    """Stores the value and the marked state of a bingo board number
    """

    def __init__(self, value):
        """Initializes an unmarked BoardNumber with the given value
        """
        self.value = value
        self.is_marked = False

    def __eq__(self, __o: object) -> bool:
        """Checks if two board numbers are equal
        """
        if isinstance(__o, BoardNumber):
            if __o.value == self.value and __o.is_marked == self.is_marked:
                return True
        return False


Row = List[BoardNumber]


class InvalidNumCols(ValueError):
    """Raised when the number of entries within a row is larger than the bingo
    board col length dimensions"""


class InvalidNumRows(ValueError):
    """Raised when the number of rows is larger than the bingo board row length
    dimensions"""


class BingoBoard():
    """Creates, stores and updates the state of a bingo board
    """

    def __init__(self, dimension: Tuple[int, int],
                 board_values: Optional[List[int]] = None):
        """initializes an empty bingo board with the given dimension. Can
        optionally provide all the values of the board.

        Args:
            dimension (Tuple[int, int]): [description]
            board_values (Optional[List[Row]], optional): All numbers for the
            board. Defaults to None.
        """
        self._rows: List[Row] = []
        self._dim: Tuple(int, int) = dimension

        if board_values is not None:
            for row in board_values:
                self.add_row(row)

    def __eq__(self, __o: object) -> bool:
        """Compares if two bingo boards are equal
        """
        if isinstance(__o, BingoBoard):
            if __o._rows == self._rows and __o._dim == self._dim:
                return True
        return False

    def add_row(self, row: List[int]):
        """Adds a row to the bingo board

        Args:
            row (List[int]): numbers for the row

        Raises:
            ValueError: If the number of rows is larger than the dimension of the board
            ValueError: If the number of numbers within a row is larger than
            the dimension of the board
        """
        if len(self._rows) == self._dim[1]:
            raise InvalidNumRows(
                F'Can not add row as the board is at its maximum'
                F' length ({self._dim[1]})')

        if len(row) > self._dim[0]:
            raise InvalidNumCols(
                F'Row length ({len(row)}) is larger than the board'
                F' length ({self._dim[0]})')

        self._rows.append([BoardNumber(value=num)
                           for num in row])

    def mark(self, marked_value: int) -> bool:
        """Marks the bingo board if the given value is on the board then checks
        to see if the board has won.

        Args:
            marked_value (int): value to mark on the board

        Returns:
            bool: True if the board has won, else False
        """
        for row_index, row in enumerate(self._rows):
            for col_index, board_number in enumerate(row):
                if board_number.value == marked_value:
                    self._rows[row_index][col_index].is_marked = True

        return self._check_for_win()

    def get_unmarked_numbers(self) -> List[int]:
        """Returns a list of all numbers within the bingo board which has not been
        marked
        """
        return [board_number.value for row in self._rows
                for board_number in row
                if board_number.is_marked is False]

    def _check_for_win(self) -> Optional[Tuple[str, int]]:
        """Checks the bingo board for a win condition

        Returns:
            Optional[Tuple[str, int]]: if there is a win returns the row/col index
            that won
        """

        # check rows & build index for cols
        cols_marked = [True] * self._dim[0]
        for row_index in range(0, self._dim[1]):
            row_marked = True
            for col_index in range(0, self._dim[0]):
                board_number = self._rows[row_index][col_index]
                row_marked = row_marked and board_number.is_marked
                cols_marked[col_index] = cols_marked[col_index] and board_number.is_marked
            if row_marked:
                return True

        # check cols
        if any(cols_marked):
            return True

        return False


def solution(input_file_path: str) -> List[int]:
    """Calculates the score of the winning bingo board
    """

    answers = []
    bingo_numbers, bingo_boards = _process_inputs(input_file_path)

    winners = _play_bingo(bingo_numbers, bingo_boards)
    first_winner = winners[0]
    last_winner = winners[-1]

    answers.append(_calculate_score(first_winner[0], first_winner[1]))
    answers.append(_calculate_score(last_winner[0], last_winner[1]))

    return answers


def _calculate_score(last_number: int, bingo_board: BingoBoard) -> int:
    """returns the final bingo score

    Args:
        last_number (int): the last number called before winning
        bingo_board (BingoBoard): the bingo board that won
    """
    return last_number * sum(bingo_board.get_unmarked_numbers())


def _parse_board(file: TextIOWrapper, board_dimension: Tuple[int, int]) -> Optional[BingoBoard]:
    """Parses a single bingo board from the input file

    Args:
        file (TextIOWrapper): input file
        board_dimension (Tuple[int,int]): the length and width of the bingo board

    Returns:
        Optional[BingoBoard]: parsed BingoBoard object or None if there are no lines
        in the file
    """
    board = BingoBoard(board_dimension)
    for _ in range(0, board_dimension[1]):
        if line := file.readline():
            line = line.strip()
            row = list(map(int, line.split()))
            board.add_row(row)
        else:
            return None
    return board


def _process_inputs(input_file_path: str) -> Tuple[List[int], List[BingoBoard]]:
    """Process the input file and returns a list of bingo numbers to mark and a
    list of all bingo boards

    Args:
        input_file_path (str): input file path
    """
    with open(input_file_path, encoding='UTF-8') as file:
        bingo_numbers = file.readline().strip().split(',')
        bingo_numbers = [int(number) for number in bingo_numbers]
        file.readline()  # read empty line

        bingo_boards: List[BingoBoard] = []
        while board := _parse_board(file, BINGO_BOARD_DIM):
            bingo_boards.append(board)
            file.readline()  # read past empty line

        return bingo_numbers, bingo_boards


def _play_bingo(called_numbers: List[int],
                bingo_boards: List[BingoBoard]) -> List[Tuple[int, BingoBoard]]:
    """Plays bingo using the list of called numbers for all the bingo boards.
    Returns a list of all the winning boards wit the last called number
    Args:
        called_numbers (List[int]): list of drawn numbers
        bingo_boards (List[BingoBoard]): all the bingo boards playing

    Returns:
        List[Tuple[int, BingoBoard]]: List of winning boards with the last
        called number
    """
    winners = []

    for number in called_numbers:
        boards_to_remove = []
        for board in enumerate(bingo_boards):
            if board.mark(number):
                winners.append((number, board))
                boards_to_remove.append(board)
        for board in boards_to_remove:
            bingo_boards.remove(board)

    return winners
