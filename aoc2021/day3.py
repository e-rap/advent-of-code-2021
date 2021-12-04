"""Day 3 Submission """
import operator
from typing import Callable
from typing import List
from typing import Tuple


def solution(input_file_path: str) -> List[int]:
    """Calculates power consumption rating and life support rating based on the
    given diagnostic data input file

    Returns List[int]: [power consumption rating, life support rating]
    """
    diagnostic_data = _process_inputs(input_file_path)

    answers = []

    # calculate power consumption rating part 1
    zero_counts, one_counts = _calculate_position_statistics(diagnostic_data)
    gamma, epsilon = _calculate_gamma_and_epsilon(zero_counts, one_counts)
    power_consumption = gamma*epsilon

    # calculate life support rating part 2
    oxygen = _reduce_by_position(diagnostic_data, operator.ge)
    c02 = _reduce_by_position(diagnostic_data, operator.lt)
    life_support_rating = oxygen * c02

    answers.append(power_consumption)
    answers.append(life_support_rating)

    return answers


def _process_inputs(input_file_path: str) -> List[str]:
    """processes all planned course inputs from file into a list of tuples
    """
    with open(input_file_path, encoding='UTF-8') as file:
        inputs = [line.strip() for line in file]
        return inputs


def _calculate_position_statistics(diagnostic_data: List[str]) -> Tuple[List[int], List[int]]:
    """Calculates the number of zeros and number of 1s in each position within
    the list of binary numbers.

    Returns Tuple[List[int],List[int]]: (number of zeros for each position,
    number of ones for each position)
    """
    digit_length = len(diagnostic_data[0])
    zero_counts = [0] * digit_length
    one_counts = [0] * digit_length
    for number in diagnostic_data:
        for index, value in enumerate(number):
            if value == '0':
                zero_counts[index] += 1
            else:
                one_counts[index] += 1
    return zero_counts, one_counts


def _calculate_gamma_and_epsilon(zero_counts: List[int], one_counts: List[int]) -> Tuple[int, int]:
    """Calculates the gamma and epsilon rate based on the one and zero counts the returns them.

    Args:
        zero_counts (List[int]): the number of 0 digits across all diagnostic data for
        each digit position
        one_counts (List[int]): the number of 1 digits across all diagnostic data for
        each digit position

    Returns Tuple[int,int]:  (gamma, epsilon)
    """
    binary_number = ''
    binary_number_complement = ''

    for one_count, zero_count in zip(one_counts, zero_counts):
        binary_number += (str(int(one_count > zero_count)))
        binary_number_complement += (str(int(one_count < zero_count)))

    gamma = int(binary_number, base=2)
    epsilon = int(binary_number_complement, base=2)
    return gamma, epsilon


def _filter_by_bit_position_value(position: int, bit_value: bool, diagnostic_data: List[str]) -> List[str]:
    """Filters diagnostic data based on the bit position value (0 or 1)

    Args:
        position (int): bit position
        bit_value (bool): value of the bit (0 or 1)
        diagnostic_data (List[str]): all the diagnostic data

    Returns:
        List[str]: filtered list of diagnostic data
    """
    filtered_data = []
    for data in diagnostic_data:
        if data[position] == str(bit_value):
            filtered_data.append(data)
    return filtered_data


def _reduce_by_position(diagnostic_data: List[str], __operator: Callable) -> int:
    """Continuously filters the diagnostic data based on the ratio of 1s to 0s for each
    bit position within the number. Returns the final reduced value.

    Args:
        diagnostic_data (List[str]): all the diagnostic data
        operator (Callable): comparison function to determine which value should be filtered.

    Returns:
        int: reduced value
    """
    short_list = diagnostic_data.copy()

    position = 0
    while len(short_list) > 1:
        zeros, ones = _calculate_position_statistics(short_list)
        short_list = _filter_by_bit_position_value(
            position, int(__operator(ones[position], zeros[position])), short_list)
        position += 1

    reduced_value = int(short_list[0], base=2)

    return reduced_value
