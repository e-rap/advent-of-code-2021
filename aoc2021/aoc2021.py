"""Advent of Code 2021 solutions application"""
import importlib
import logging
import os
import sys
from types import ModuleType
from typing import List

import click

__version__ = '1.1.0'

# dynamically import every day


def import_day_modules(parent_directory_path: str) -> List[ModuleType]:
    """Dynamically imports the module for each day and returns a list of containing
    all the modules

    Args:
        parent_directory_path (str): parent directory for all the day modules

    Returns:
        List[ModuleType]: list of imported modules
    """
    _modules = []
    module_names = [file[:-3] for file in os.listdir(
        parent_directory_path) if 'day' in file]

    for name in module_names:
        _modules.append(importlib.import_module(name))
    return _modules


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, FILE_DIR)

modules = import_day_modules(FILE_DIR)

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

    solutions = [module.solution for module in modules]
    if day is None:
        log.info('Running all submissions')
        for day in range(1, len(solutions)+1):
            run_solution(day, solutions)
    else:
        run_solution(day, solutions)


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    aoc2021()
