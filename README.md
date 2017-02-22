Simple Python [word ladder](https://en.wikipedia.org/wiki/Word_ladder)
generator that finds the shortest ladder between two words.

`generate.py` precomputes the dictionaries used to build the ladder (only
needs to run once, or never, since the output jsons are in the repo)

`ladder.py` takes a `start` and `target` argument and outputs a ladder, if
one exists.

Currently only supports words from 2-6 characters, though easy enough to
extend.

Thanks to [ahupp](https://github.com/ahupp) for the
[Burkhard-Keller tree implementation](https://github.com/ahupp/bktree)
