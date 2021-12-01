"""Day 1 Submission """
from ast import literal_eval
from typing import List


def solution(input_file_path: str) -> int:
    """Calculates the number of sonar measurements that are larger than the
    previous measurement

    Args:
        input_file (str): path to the input file containing the sonar measurements

    Returns:
        int: number of measurements larger than its previous measurement
    """
    data = _process_inputs(input_file_path)
    num_increasing_data = _find_increasing_measurements(data)
    sliding_window_data = _sliding_window_sum(data, window_size=3)
    num_increasing_window_data = _find_increasing_measurements(
        sliding_window_data)
    return (num_increasing_data, num_increasing_window_data)


def _process_inputs(input_file_path: str) -> List[int]:
    with open(input_file_path, encoding='UTF-8') as file:
        measurements = [literal_eval(line) for line in file]
        return measurements


def _find_increasing_measurements(measurements: List[int]) -> int:
    """finds the number of increasing measurements in the list"""
    count = 0
    last_measurement = measurements[0]
    for measurement in measurements[1:]:
        if measurement > last_measurement:
            count += 1
        last_measurement = measurement
    return count


def _sliding_window_sum(data: List[int], window_size: int = 3) -> List[int]:
    """Calculates a sliding window sum for all input data

    Args:
        data (List[int]): list of data
        window_size (int, optional): Size of the sliding window for the sum.
        Defaults to 3.

    Returns:
        List[int]: list of sums for each sliding window
    """

    windows = []
    for i in range(0, len(data)-(window_size-1)):
        windows.append(sum(data[i:i+window_size]))
    return windows
