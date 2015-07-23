"""
Tests for :class:`Board`
"""

import unittest

from boggle.boggle import Board, Word


class IsAvailableRouteTests(unittest.TestCase):
    """
    Tests for `Board.is_available_route`.
    """

    def test_route(self):
        """
        If there is a route between each letter, True is returned.
        """
        board = Board(rows=[
            ['A', 'B', 'C'],
        ])

        self.assertTrue(
            board.is_available_route(
                word=Word(
                    string='ABC',
                    valid_tiles=set(['A', 'B', 'C']),
                ),
            ),
        )

    def test_not_in_board(self):
        """
        If a word is not available in the board, False is returned.
        """
        board = Board(rows=[
            ['A', 'C', 'B'],
        ])
        self.assertFalse(
            board.is_available_route(
                word=Word(
                    string='ABC',
                    valid_tiles=set(['A', 'B', 'C']),
                ),
            ),
        )

    def test_repeated_tile(self):
        """
        A route which uses the same tile multiple times is not valid, so if
        this is the only available route, False is returned.
        """
        board = Board(rows=[
            ['A', 'B'],
        ])

        self.assertFalse(
            board.is_available_route(
                word=Word(
                    string='ABA',
                    valid_tiles=set(['A', 'B']),
                ),
            ),
        )
