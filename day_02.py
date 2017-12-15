#!/usr/bin/env python3

def checksum(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)

if __name__ == '__main__':

    import re

    with open('day_02.txt') as f:
        spreadsheet = [ [ int(n) for n in re.split('\s+', line[:-1]) ] for line in f ]
        print(checksum(spreadsheet))
