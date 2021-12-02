"""Day 2 Submission """
from typing import List
from typing import Tuple


def solution(input_file_path: str) -> List[int]:
    """Calculates the final position of the submarine based on the plotted
    course. Returns the horizontal position * depth
    """
    planned_course = _process_inputs(input_file_path)

    positions = []
    positions.append(_calculate_sub_position(planned_course))
    positions.append(_calculate_sub_position_aim(
        planned_course))
    return [(horizontal_pos*depth) for horizontal_pos, depth in positions]


def _process_inputs(input_file_path: str) -> List[Tuple[str, str]]:
    """processes all planned course inputs from file into a list of tuples
    """
    with open(input_file_path, encoding='UTF-8') as file:
        input_generator = [tuple(line.strip().split(' ')) for line in file]
        return input_generator


def _calculate_sub_position(planned_course: List[Tuple[str, str]]) -> Tuple[int, int]:
    """Calculates the position of the submarine which includes its horizontal
    position and depth from the inputs based on the planned course.

    Args:
        planned_course (List[Tuple[str,str]]): list planned course data (direction, value)

    Raises:
        RuntimeError: if the direction is invalid (not up, down, forward)

    Returns:
        Tuple[int,int]: (horizontal position, depth)
    """
    horizontal_distance = 0
    depth = 0
    for direction, value in planned_course:
        value = int(value)
        if direction == 'forward':
            horizontal_distance += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value
        else:
            raise RuntimeError('Invalid direction!')
    return horizontal_distance, depth


def _calculate_sub_position_aim(planned_course: List[Tuple[str, str]]) -> Tuple[int, int]:
    """Calculates the position of the submarine which includes its horizontal
    position and depth from the inputs based on the planned course with aim.

    Args:
        planned_course (List[Tuple[str,str]]): list planned course data (direction, value)

    Raises:
        RuntimeError: if the direction is invalid (not up, down, forward)

    Returns:
        Tuple[int,int]: (horizontal position, depth)
    """
    horizontal_distance = 0
    depth = 0
    aim = 0
    for (direction, value) in planned_course:
        value = int(value)
        if direction == 'forward':
            horizontal_distance += value
            depth += aim * value
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
        else:
            raise RuntimeError('Invalid direction!')
    return horizontal_distance, depth
