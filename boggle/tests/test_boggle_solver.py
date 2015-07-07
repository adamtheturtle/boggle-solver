"""
Tests for solving a game of Boggle.
"""

import unittest

from boggle.boggle import (
    list_words,
    positions_touching,
    get_tile_mapping,
    is_available_route,
    is_valid_route,
)


class IsAvailableRouteTests(unittest.TestCase):
    """
    Tests for `is_available_route`.
    """

    def test_route(self):
        """
        If there is a route between each letter, True is returned.
        """
        self.assertTrue(
            is_available_route(
                word='ABC',
                tile_map=get_tile_mapping([
                    ['A', 'B', 'C'],
                ]),
            )
        )

    def test_not_in_board(self):
        """
        If a word is not available in the board, False is returned.
        """
        self.assertFalse(
            is_available_route(
                word='ABC',
                tile_map=get_tile_mapping([
                    ['A', 'C', 'B'],
                ]),
            )
        )

    def test_invalid_route(self):
        """
        If only an invalid route is available, False is returned.
        """
        self.assertFalse(
            is_available_route(
                word='ABA',
                tile_map=get_tile_mapping([
                    ['A', 'B'],
                ]),
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


class IsValidRouteTests(unittest.TestCase):
    """
    Tests for `is_valid_route`.
    """

    def test_valid_route(self):
        """
        A route which includes no duplicates and is of the same length as the
        given word is valid.
        """
        self.assertTrue(is_valid_route('abc', [(0, 0), (1, 0), (2, 0)]))

    def test_duplicate_tiles(self):
        """
        A route which uses the same tile multiple times is not valid.
        """
        self.assertFalse(is_valid_route('abc', [(0, 0), (0, 0), (2, 0)]))

    def test_mismatching_length(self):
        """
        A route which has a different length to the given word is not valid.
        """
        self.assertFalse(is_valid_route('abc', [(0, 0), (1, 0)]))
