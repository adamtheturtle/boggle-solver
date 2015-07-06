from __future__ import print_function
import copy
import unittest
import io

# TODO Add pyflakes to travis
# TODO add code coverage to travis
# TODO add a way to input a board (text file / photo)
# TODO possible optimisations -
#   * Decrease the dictionary length to remove "'"s etc.
#   * Decrease the dictionary length to remove two letter words.
#   * Stop after one valid route


def get_positions(letter, board):
    """
    Return a list of positions a letter can be found on a board.

    letter: A letter on a tile.
    return: List of (column, row) co-ordinates of tiles containing this letter.
    """
    positions = []
    for row_index, row in enumerate(board):
        for column_index, piece in enumerate(row):
            if piece[0].upper() == letter[0].upper():
                positions.append((column_index, row_index))
    return positions


def positions_touching(first, second):
    """
    Given two tile positions, check whether they are touching.

    first: Tuple of co-ordinates of a tile.
    second: Tuple of co-ordinates of a tile.

    return: Bool, true iff the tiles are touching - immediately above, below
        or diagonal.
    """
    return abs(first[0] - second[0]) <= 1 and abs(first[1] - second[1]) <= 1


def get_routes(word, board):
    """
    Get available routes to make a word in a board.

    A route is a path of positions from first tile to next, to next... until
    the last tile. It cannot include the same tile multiple times.

    word: A string.
    board: A list of lists of tiles. Each list in the list of lists represents
        a row of a Boggle board.

    returns: List of lists of tile positions.
    """
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

    valid_routes = []
    for route in routes:
        no_duplicates = len(set(route)) == len(route)
        includes_whole_word = len(route) == len(word)
        if no_duplicates and includes_whole_word:
            valid_routes.append(route)

    return valid_routes


def list_words(board, dictionary):
    """
    Return all words from a given dictionary which are in a board.

    dictionary: A set of valid words.
    board: A list of lists of tiles. Each list in the list of lists represents
        a row of a Boggle board.

    returns: A set of strings.
    """
    word_list = set()
    for word in dictionary:
        word = word.upper()
        routes = get_routes(word.replace('QU', 'Q'), board)
        if len(routes) and len(word) > 2:
            word_list.add(word)
    return word_list


class GetRoutesTests(unittest.TestCase):
    """
    Tests for `get_routes`.
    """

    def test_route(self):
        """
        A list of lists positions between the first and last letter is
        returned.
        """
        self.assertEqual(
            [
                [(0, 0), (1, 0), (2, 0)],
            ],
            get_routes(
                word='ABC',
                board=[
                    ['A', 'B', 'C'],
                ],
            )
        )

    def test_not_in_board(self):
        """
        If a word is not available in the board, an empty list is returned.
        """
        self.assertEqual(
            [],
            get_routes(
                word='ABC',
                board=[
                    ['D', 'E', 'F'],
                ],
            )
        )

    def test_cannot_reuse_tile(self):
        """
        The same tile cannot be reused.
        """
        self.assertEqual(
            [],
            get_routes(
                word='ABA',
                board=[
                    ['A', 'B'],
                ],
            )
        )

    def test_all_letters_necessary(self):
        """
        A route does not exist if not all letters are available.
        """
        self.assertEqual(
            [],
            get_routes(
                word='ABCD',
                board=[
                    ['A', 'C', 'D'],
                ],
            )
        )


class ListWordsTests(unittest.TestCase):
    """
    Tests for `list_words`.
    """
    def test_list_words(self):
        """
        A set of available words is returned.
        """
        self.assertEqual(
            set(['ABC', 'DEF']),
            list_words(
                dictionary=set(['ABC', 'DEF', 'GHI']),
                board=[
                    ['A', 'B', 'C'],
                    ['D', 'E', 'F'],
                ],
            )
        )

    def test_short_word_ignored(self):
        """
        Only words of 3 or more letters are returned.
        """
        self.assertEqual(
            set(),
            list_words(
                dictionary=set(['AB']),
                board=[
                    ['A', 'B'],
                ],
            )
        )

    def test_q_u_together(self):
        """
        Q and u are on the same tile.
        """
        self.assertEqual(
            set(['QUA']),
            list_words(
                dictionary=set(['QUA']),
                board=[
                    ['Qu', 'A'],
                ],
            )
        )

    def test_case_insensitive_dictionary(self):
        """
        Listing words is case insensitive to dictionary case.
        """
        self.assertEqual(
            set(['ABC']),
            list_words(
                dictionary=set(['AbC']),
                board=[
                    ['A', 'B', 'C'],
                ],
            )
        )

    def test_case_insensitive_board(self):
        """
        Listing words is case insensitive to board case.
        """
        self.assertEqual(
            set(['ABC']),
            list_words(
                dictionary=set(['ABC']),
                board=[
                    ['A', 'B', 'c'],
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

    def test_case_insensitive(self):
        """
        The case of the letter does not matter.
        """
        self.assertEqual(
            [(0, 0), (0, 1)],
            get_positions(
                letter='a',
                board=[
                    ['a'],
                    ['A'],
                ],
            )
        )

    def test_first_letter_only(self):
        """
        Only the first letter is compared. This is to handle the "Qu" tile.
        """
        self.assertEqual(
            [(0, 0)],
            get_positions(
                letter='AB',
                board=[
                    ['AC'],
                ],
            )
        )


class PositionsTouchingTests(unittest.TestCase):
    """
    Tests for `positions_touching`.
    """

    def test_touching(self):
        """
        If tiles are touching, positions_touching returns True.
        """
        self.assertTrue(
            all([
                # Second on right on first.
                positions_touching(first=(1, 0), second=(0, 0)),
                # Second on left of first.
                positions_touching(first=(1, 0), second=(0, 0)),
                # Second above first.
                positions_touching(first=(0, 1), second=(0, 0)),
                # Second below first.
                positions_touching(first=(0, 0), second=(0, 1)),
                ],
                ))

    def test_not_touching(self):
        """
        If tiles are not touching, positions_touching returns False.
        """
        self.assertFalse(positions_touching(first=(0, 0), second=(0, 2)))

if __name__ == "__main__":
    with io.open("english_words.txt", encoding='latin-1') as word_file:
        english_words = set(word.strip() for word in word_file)

    found_words = list_words(
        dictionary=english_words,
        board=[
            ['Qu', 'A', 'A', 'M', 'D'],
            ['A', 'L', 'G', 'O', 'O'],
            ['R', 'G', 'I', 'D', 'E'],
            ['O', 'N', 'F', 'Y', 'R'],
            ['R', 'E', 'L', 'L', 'S'],
        ],
    )
    print(len(found_words))
    from pprint import pprint
    pprint(sorted(list(found_words)))
