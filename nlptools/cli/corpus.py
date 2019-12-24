import sys
import random
import heapq

import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--seed', type=int)
def shuffle(seed):
    random.seed(seed)
    for line in sorted(sys.stdin, key=random.random):
        print(line, end='')

@cli.command()
@click.option('-n', '--num-lines', type=int, default=10)
@click.option('--seed', type=int)
def shuffle_head(num_lines, seed):
    random.seed(seed)
    for line in heapq.nlargest(num_lines, sys.stdin, key=random.random):
        print(line, end='')

if __name__ == "__main__":
    cli()
