"""
Tests for solving a game of Boggle.
"""

import unittest

from boggle.boggle import (
    get_routes,
    list_words,
    get_positions,
    positions_touching,
)


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
