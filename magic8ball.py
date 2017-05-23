#!/usr/bin/env python
# encoding: utf-8

# 8ball
# Just Ask
#
# by Jesse Wallace (@c0deous)
# https://c0deo.us/

import random

def magic8ball():
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most Likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    return random.choice(responses)

if __name__ == '__main__':
    print(magic8ball())
