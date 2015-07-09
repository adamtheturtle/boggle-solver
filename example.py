from __future__ import print_function
import io
import string
import random

from boggle.boggle import list_words


def main():
    with io.open("/usr/share/dict/words", encoding='latin-1') as word_file:
        english_words = set(word.strip() for word in word_file)

    available_tiles = [letter for letter in string.ascii_uppercase]
    available_tiles.remove('Q')
    available_tiles.append('Qu')

    # A boggle board is an n * n square. Set n:
    size = 10

    board = []
    for row in range(size):
        board.append([random.choice(available_tiles) for i in range(size)])

    found_words = list_words(
        word_list=english_words,
        board=board,
    )

    print(len(found_words))

main()
