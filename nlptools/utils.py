import sys
import logging

import click

logger = logging.getLogger(__name__)

@click.group()
def cli():
    LOG_FORMAT = '[%(asctime)s] [%(levelname)s] %(message)s (%(funcName)s@%(filename)s:%(lineno)s)'
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

class Segment:
    def __init__(self, start=None, end=None, exact=None):
        self.start = start
        self.end = end
        self.exact = exact

    def match(self, line_n):
        if self.exact is not None:
            if line_n != self.exact:
                return False
        else:
            if self.start is not None and line_n < self.start:
                return False

            if self.end is not None and self.end < line_n:
                return False

        return True

@cli.command()
@click.argument('line-selector', type=str)
def lut(line_selector):
    def parse_seg(seg):
        x = seg.split('-')
        if len(x) == 1:
            return Segment(exact=int(x[0]))
        elif len(x) == 2:
            start = int(x[0]) if x[0] != '' else None
            end = int(x[1]) if x[1] != '' else None
            return Segment(start=start, end=end)

    segments = [parse_seg(seg) for seg in line_selector.split(',')]

    cur = 0
    matched = False

    for i, line in enumerate(sys.stdin, 1):
        if segments[cur].match(i):
            print(line, end='')
            matched = True
        elif matched:
            cur += 1
            matched = False
            if cur >= len(segments):
                break
            

if __name__ == '__main__':
    cli()
