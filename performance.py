from __future__ import print_function
import io
import os

from boggle.boggle import list_words


def main():

    large_board = [
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
        ['S', 'X', 'Y', 'M', 'N', 'S', 'R', 'C', 'W', 'U', 'V', 'T', 'E', 'Qu', 'E'],
        ['S', 'X', 'Y', 'M', 'N', 'S', 'R', 'C', 'W', 'U', 'V', 'T', 'E', 'Qu', 'E'],
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
        ['S', 'X', 'Y', 'M', 'N', 'S', 'R', 'C', 'W', 'U', 'V', 'T', 'E', 'Qu', 'E'],
        ['S', 'X', 'Y', 'M', 'N', 'S', 'R', 'C', 'W', 'U', 'V', 'T', 'E', 'Qu', 'E'],
        ['P', 'N', 'C', 'P', 'G', 'Y', 'M', 'D', 'J', 'Z', 'F', 'D', 'C', 'J', 'U'],
        ['E', 'L', 'N', 'M', 'I', 'L', 'J', 'A', 'O', 'N', 'Qu', 'K', 'Y', 'O', 'M'],
        ['K', 'O', 'O', 'L', 'J', 'S', 'J', 'B', 'B', 'O', 'K', 'N', 'C', 'A', 'K'],
    ]

    small_board = [
        ["Qu", "A", "A", "M", "D"],
        ["A", "L", "G", "O", "O"],
        ["R", "G", "I", "D", "E"],
        ["O", "N", "F", "Y", "R"],
        ["R", "E", "L", "L", "S"],
    ]

    boards = [
        # {'board': large_board, 'file': 'large_board'},
        {'board': small_board, 'file': 'small_board'},
    ]

    for board in boards:
        found_words = list_words(board=board['board'])

        if not os.path.exists(board['file']):
            with io.open(board['file'], 'wb') as word_file:
                for word in found_words:
                    word_file.write(word + '\n')
            return

        with io.open(board['file'], 'rb') as word_file:
            expected_words = set(word.strip() for word in word_file)

        if len(expected_words) != len(found_words):
            for word in found_words:
                if word not in expected_words:
                    print(word + ': found, not expected')
            for word in expected_words:
                if word not in found_words:
                    print(word + ': expected, not found')
main()
# import profile
# profile.run('main()')
