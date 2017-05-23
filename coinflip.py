#!/usr/bin/env python
# encoding: utf-8

# Coinflip
# A weighted coinflip program
#
# by Jesse Wallace (@c0deous)
# https://c0deo.us/

import random

def coinflip(headsweight=0.5, tailsweight=0.5):
    choicelist = ['Heads', 'Tails']
    chancelist = []
    headscount = 0
    tailscount = 0
    while headscount != headsweight * 100:
        chancelist.append(choicelist[0])
        headscount = headscount + 1
    while tailscount != tailsweight * 100:
        chancelist.append(choicelist[1])
        tailscount = tailscount + 1
    if len(chancelist) != 100 or headsweight + tailsweight != 1:
        print('Error')
        raise SystemExit
    return random.choice(chancelist)


if __name__ == '__main__':
    print(coinflip())

