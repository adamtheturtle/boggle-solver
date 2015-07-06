# python -m unittest boggle

import copy
import unittest

# TODO does this handle Qu?
# TODO always lowercase
# TODO docstrings
# TODO travis

def get_positions(letter, board):
    positions = []
    for row_index, row in enumerate(board):
        for column_index, piece in enumerate(row):
            if piece == letter:
                positions.append((column_index, row_index))
    return positions

def positions_touching(first, second):
    return abs(first[0] - second[0]) <= 1 and abs(first[1] - second[1]) <= 1


def get_touching_positions(first_positions, second_positions):
    touching_positions = []

    for first_position in first_positions:
        for second_position in second_positions:
            if positions_touching(first_position, second_position):
                touching_positions.append([first_position, second_position])

    return touching_positions

def get_routes(word, board):
    routes = []

    for letter in word:
        positions = get_positions(letter, board)
        if not len(routes):
            new_routes = [[position] for position in positions]
        else:
            new_routes = []

            for route in routes:
                for position in positions:
                    if positions_touching(route[len(route) - 1], position):
                        new_route = copy.copy(route)
                        new_route.append(position)
                        new_routes.append(new_route)

        routes = copy.copy(new_routes)

    routes_without_duplicates = []
    for route in routes:
        if len(set(route)) == len(route):
            routes_without_duplicates.append(route)

    whole_word_routes = []
    for route in routes_without_duplicates:
        if len(route) == len(word):
            whole_word_routes.append(route)
    return whole_word_routes

def list_words(board, dictionary):
    """
    board: list of lists.
    """
    word_list = set()
    for word in dictionary:
        if len(word) > 2:
            routes = get_routes(word, board)
            if len(routes):
                word_list.add(word)
    return word_list

class GetRoutesTests(unittest.TestCase):

    def test_route(self):
        self.assertEqual(
            [
                [(0, 0), (1, 0), (2, 0)],
            ],
            get_routes(
                word='foo',
                board=[
                    ['f', 'o', 'o']
                ],
            )
        )

    def test_not_in_board(self):
        self.assertEqual(
            [],
            get_routes(
                word='not',
                board=[
                    ['w', 'o', 'r', 'd']
                ]
            )
        )

    def test_cannot_reuse_letter(self):
        self.assertEqual(
            [],
            get_routes(
                word='wow',
                board=[
                    ['w', 'o', 'r', 'd']
                ],
            )
        )

    def test_all_letters_necessary(self):
        self.assertEqual(
            [],
            get_routes(
                word='ptop',
                board=[
                    ['p', 'o', 'p'],
                ],
            )
        )

class ListWordsTests(unittest.TestCase):

    def test_list_words(self):
        self.assertIn(
            'zoo',
            list_words(
                dictionary=set(['zoo']),
                board=[
                    ['z', 'o', 'o', 'a', 'a'],
                    ['a', 'a', 'a', 'a', 'a'],
                ],
            )
        )

    def test_word_not_in_dict(self):
        self.assertNotIn(
            'zoo',
            list_words(
                dictionary=set(['foo']),
                board=[
                    ['z', 'o', 'o', 'a', 'a'],
                    ['a', 'a', 'a', 'a', 'a'],
                ],
            )
        )

    def test_word_not_found(self):
        self.assertNotIn(
            'zoo',
            list_words(
                dictionary=set(['zoo']),
                board=[
                    ['a', 'a', 'a', 'a', 'a'],
                    ['a', 'a', 'a', 'a', 'a'],
                ],
            )
        )

    def test_short_word_ignored(self):
        self.assertNotIn(
            'zo',
            list_words(
                dictionary=set(['zo']),
                board=[
                    ['z', 'o'],
                ],
            )
        )

class GetPositionsTests(unittest.TestCase):
    """
    Tests for get_positions.
    """

    def test_get_positions(self):
        """
        A list of position tuples
        """
        self.assertEqual(
            [(0, 0), (2, 0), (0, 1)],
            get_positions(
                letter='A',
                board=[
                    ['A', 'X', 'A', 'X', 'X'],
                    ['A', 'X', 'X', 'X', 'X'],
                ],
            )
        )

class PositionsTouchingTests(unittest.TestCase):
    """
    Tests for `positions_touching`.
    """

    def test_adjacent_left(self):
        """
        If the second piece is on the left of the first, the pieces are
        touching.
        """
        self.assertTrue(positions_touching(first=(1, 0), second=(0, 0)))

    def test_adjacent_right(self):
        """
        If the second piece is on the right of the first, the pieces are
        touching.
        """
        self.assertTrue(positions_touching(first=(0, 0), second=(1, 0)))

    def test_adjacent_above(self):
        """
        If the second piece is above the first, the pieces are touching.
        """
        self.assertTrue(positions_touching(first=(0, 1), second=(0, 0)))

    def test_adjacent_below(self):
        """
        If the second piece is below the first, the pieces are touching.
        """
        self.assertTrue(positions_touching(first=(0, 0), second=(0, 1)))

    def test_diagonal(self):
        """
        If the second piece is diagonal to the first, the pieces are touching.
        """
        self.assertTrue(positions_touching(first=(0, 0), second=(1, 1)))

    def test_not_touching(self):
        """
        Unconnected pieces are not touching.
        """
        self.assertFalse(positions_touching(first=(0, 0), second=(0, 2)))

if __name__ == "__main__":
    with open("english_words.txt") as word_file:
        english_words = set(word.strip().lower() for word in word_file)
    found_words = list_words(
        dictionary=english_words,
        board=[
            ['qu', 'a', 'a', 'm', 'd'],
            ['a', 'l', 'g', 'o', 'o'],
            ['r', 'g', 'i', 'd', 'e'],
            ['o', 'n', 'f', 'y', 'r'],
            ['r', 'e', 'l', 'l', 's'],
        ],
    )
    print len(found_words)
    from pprint import pprint
    pprint(sorted(list(found_words)))