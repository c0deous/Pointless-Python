#!/usr/bin/env python
# encoding: utf-8

# aesthetic
# Makes a string more a e s t h e t i c

import sys

def aesthetic(intext="vaporwave is dead"):
    outtext = ''
    for letter in intext:
        outtext = outtext + letter + ' '
    return outtext

if __name__ == '__main__':
    try:
        print(aesthetic(sys.argv[1]))
    except IndexError:
        print(aesthetic())
