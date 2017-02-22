#!/usr/bin/env python
"""
Word ladder - given a start and a target, generates the shortest chain
of words to get from start to target, changing one letter at a time,
with each step being a valid word from the Scrabble dictionary.
"""

import sys
import json
import argparse
from collections import deque

def find_ladder(start, target, linked_words):
    """
    Find the shortest word ladder from start to target

    Arguments:

    start: the start of the ladder

    target: the end of the ladder

    linked_words: a dictionary <string, list(string)> of words and the
    valid words Levenshtein distance 1 from them

    Return value is a list of words forming the ladder, or None if no ladder
    exists.
    """
    queue = deque([[start]])
    used_words = []
    while (len(queue) > 0):
        ladder = queue.popleft()
        next_words = linked_words[ladder[-1]]
        for next_word in next_words:
            attempt = list(ladder)
            attempt.append(next_word)
            if next_word == target:
                return attempt
            if next_word not in used_words:
                used_words.append(next_word)
                queue.append(attempt)
    return None

def word_type(x):
    """
    Helper type for arg parsing (ensures words are in length range 2-6)
    """
    if len(x) < 1 or len(x) > 6:
        raise argparse.ArgumentTypeError(
            "Words must be 2 to 6 chars in length")
    return x.lower()

parser = argparse.ArgumentParser()
parser.add_argument("start", type=word_type)
parser.add_argument("target", type=word_type)
args = parser.parse_args()

if len(args.start) != len(args.target):
    print "Words must be equal length"
    exit()

print "Loading dictionary"
filenames = ["twos", "threes", "fours", "fives", "sixes"]
filename = filenames[len(args.start) - 2] + ".json"
with open(filename, "r") as f:
    word_list = json.load(f)

if args.start not in word_list:
    print args.start + " is not a valid word"
    exit()
if args.target not in word_list:
    print args.target + " is not a valid word"
    exit()

print "Finding ladder"
result = find_ladder(args.start, args.target, word_list)
if result is None:
    print "No ladder exists from {} to {}".format(args.start, args.target)
else:
    for w in result: print w
