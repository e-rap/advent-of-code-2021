"""Advent of Code 2021 solutions application"""
import logging
import os
import sys

import click
import day1
import day2

__version__ = '1.0.0'

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, FILE_DIR)

log = logging.getLogger()
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(sys.stdout))


def run_solution(day: int, solutions: list) -> None:
    """Runs a solution based on the given day"""
    if (day-1) > len(solutions):
        log.error('There is currently no solution for day %s.', day)
    else:
        try:
            log.info('Running day %s submission', day)
            input_file_path = os.path.join(FILE_DIR, f'inputs/day{day}.txt')
            output = solutions[day-1](input_file_path)
            log.info('Output = %s', output)
        # pylint: disable=broad-except
        except Exception:
            log.exception('Exception occurred while running the submission')


@click.command()
@click.option('--day', help='selects the submission day to run (1-31)', type=int)
def aoc2021(day):
    """Runs Advent of Code 2021 submissions
    """

    solutions = [day1.solution, day2.solution]
    if day is None:
        log.info('Running all submissions')
        for day in range(1, len(solutions)+1):
            run_solution(day, solutions)
    else:
        run_solution(day, solutions)


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    aoc2021()
