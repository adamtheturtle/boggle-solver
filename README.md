[![Build Status](https://travis-ci.org/adamtheturtle/boggle-solver.svg?branch=travis-test)](https://travis-ci.org/adamtheturtle/boggle-solver) [![Coverage Status](https://coveralls.io/repos/adamtheturtle/boggle-solver/badge.svg)](https://coveralls.io/r/adamtheturtle/boggle-solver)

# boggle-solver

Gives a list of all valid words in a Boggle board.

A Boggle board is an `n * n` board of tiles.
Each tile has either one letter of the alphabet (not including "Q") or "Qu".

A valid word is one which can be made from adjacent tiles (including diagonally adjacent tiles).
Each tile can be used at most once for each word.
A valid word is at least three letters long.

# Tests

[Travis-CI](https://travis-ci.org/adamtheturtle/boggle-solver) runs all of the tests on various versions of Python.

Run the tests locally using:

```
python -m unittest discover
```
