from __future__ import print_function
import string
import random

from boggle.boggle import Boggle, Language, Board


def main():
    available_tiles = [letter for letter in string.ascii_uppercase]
    available_tiles.remove('Q')
    available_tiles.append('Qu')

    # A boggle board is an n * n square. Set n:
    size = 10

    board = []
    for row in range(size):
        board.append([random.choice(available_tiles) for i in range(size)])

    language = Language(dictionary_path="/usr/share/dict/words")
    boggle = Boggle(
        board=Board(rows=board['board']),
        valid_words=language.words)

    found_words = boggle.list_words()
    print

if __name__ == '__main__':
    main()