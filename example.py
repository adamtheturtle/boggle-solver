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

    size = 8

    board = []
    for row in range(size):
        board.append([random.choice(available_tiles) for i in xrange(size)])

    board = [
        ['C', 'C', 'N', 'R', 'S', 'V', 'M', 'Y'],
        ['V', 'C', 'P', 'I', 'G', 'I', 'D', 'E'],
        ['M', 'S', 'T', 'L', 'B', 'S', 'Qu', 'K'],
        ['L', 'C', 'M', 'R', 'L', 'N', 'H', 'X'],
        ['O', 'V', 'W', 'V', 'B', 'N', 'E', 'K'],
        ['T', 'U', 'W', 'A', 'O', 'G', 'A', 'S'],
        ['J', 'V', 'V', 'W', 'F', 'T', 'J', 'G'],
        ['Qu', 'U', 'G', 'V', 'F', 'P', 'N', 'I']
    ]

    found_words = list_words(
        word_list=english_words,
        board=board,
    )

    print(len(found_words))

main()
# import profile
# profile.run('main()')
