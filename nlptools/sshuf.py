import random
import sys
import functools
import bisect

import click

@functools.total_ordering
class ScoredLine:
    def __init__(self, score: float, line: str):
        self.score = score
        self.line = line

    def __lt__(self, value):
        return self.score < value.score

    def __eq__(self, value):
        return self.score == value.score

@click.command()
@click.option('--n-lines', '-n', type=int, default=10)
@click.option('--seed', type=int)
def main(n_lines, seed):
    random.seed(seed)

    lines = []

    for line in sys.stdin:
        line = ScoredLine(score=random.random(), line=line)
        bisect.insort_left(lines, line)
        lines = lines[:n_lines]
        
    for line in lines:
        print(line.line, end='')

if __name__ == '__main__':
    main()







