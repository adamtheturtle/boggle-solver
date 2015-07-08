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

    size = 15

    board = []
    for row in range(size):
        board.append([random.choice(available_tiles) for i in xrange(size)])

    from pprint import pprint
    board = [
        ['K', 'O', 'O', 'L', 'J', 'S', 'J', 'B', 'B', 'O', 'K', 'N', 'C', 'A', 'K'],
        ['C', 'M', 'M', 'V', 'C', 'G', 'H', 'G', 'V', 'Qu', 'Y', 'M', 'Z', 'M', 'D'],
        ['Qu', 'S', 'E', 'K', 'E', 'U', 'A', 'C', 'V', 'E', 'O', 'P', 'O', 'H', 'O'],
        ['K', 'D', 'Y', 'W', 'B', 'J', 'R', 'C', 'U', 'T', 'D', 'D', 'E', 'S', 'N'],
        ['Z', 'N', 'C', 'L', 'J', 'A', 'H', 'X', 'I', 'U', 'R', 'V', 'N', 'I', 'L'],
        ['U', 'B', 'A', 'S', 'W', 'K', 'E', 'S', 'K', 'K', 'C', 'P', 'A', 'X', 'R'],
        ['F', 'A', 'C', 'X', 'H', 'F', 'Z', 'V', 'E', 'E', 'F', 'O', 'L', 'P', 'Z'],
        ['Y', 'Z', 'G', 'O', 'I', 'D', 'X', 'N', 'O', 'D', 'A', 'W', 'V', 'I', 'H'],
        ['E', 'L', 'N', 'M', 'I', 'L', 'J', 'A', 'O', 'N', 'Qu', 'K', 'Y', 'O', 'M'],
        ['P', 'N', 'C', 'P', 'G', 'Y', 'M', 'D', 'J', 'Z', 'F', 'D', 'C', 'J', 'U'],
        ['J', 'Z', 'W', 'R', 'L', 'L', 'B', 'M', 'T', 'X', 'V', 'Y', 'K', 'Y', 'J'],
        ['Z', 'U', 'G', 'S', 'N', 'B', 'R', 'F', 'N', 'C', 'Qu', 'U', 'D', 'U', 'F'],
        ['S', 'K', 'I', 'Z', 'B', 'Z', 'C', 'T', 'M', 'S', 'P', 'B', 'D', 'O', 'Y'],
        ['V', 'U', 'S', 'B', 'V', 'N', 'T', 'Y', 'E', 'L', 'U', 'M', 'O', 'V', 'S'],
        ['S', 'X', 'Y', 'M', 'N', 'S', 'R', 'C', 'W', 'U', 'V', 'T', 'E', 'Qu', 'E']
    ]

    found_words = list_words(
        word_list=english_words,
        board=board,
    )

    print(len(found_words))

main()
# import profile
# profile.run('main()')
