import random
import sys
import functools
import bisect
import logging

import click

logger = logging.getLogger(__name__)

@functools.total_ordering
class ScoredLine:
    def __init__(self, score: float, line: str):
        self.score = score
        self.line = line

    def __lt__(self, value):
        return self.score < value.score

    def __eq__(self, value):
        return self.score == value.score

@click.group()
def cli():
    LOG_FORMAT = '[%(asctime)s] [%(levelname)s] %(message)s (%(funcName)s@%(filename)s:%(lineno)s)'
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

@cli.command()
@click.option('--n-lines', '-n', type=int)
@click.option('--seed', type=int)
def shuffle(n_lines, seed):
    random.seed(seed)

    lines = []

    for line in sys.stdin:
        line = ScoredLine(score=random.random(), line=line)
        bisect.insort_left(lines, line)
        if n_lines:
            lines = lines[:n_lines]
        
    for line in lines:
        print(line.line, end='')

if __name__ == '__main__':
    cli()







