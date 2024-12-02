#!/usr/bin/env python3

from lib.chinese_remainder_theorem import chinese_remainder_theorem

from pathlib import Path
import sys


def part1():

    with open('2020/_input/day13.txt', 'r') as fp:
        earliest = int(fp.readline())
        schedule = [int(s) for s in fp.readline().split(',') if s != 'x']
 
    best = min([(s, s - earliest % s) for s in schedule], key=lambda s: s[1] )
    print( best[0] * best[1] )


def part2(safeguard=1_000_000_000):
    r = []
    m = []
    with open('2020/_input/day13.txt', 'r') as fp:
        _ = int(fp.readline())
        for i, s in enumerate([int(s) if s != 'x' else s for s in fp.readline().split(',')]):
            if s == 'x':
                continue
            s = int(s)
            r.append((s - i % s) % s)
            m.append(s)
        return chinese_remainder_theorem(r, m)


print(part2())