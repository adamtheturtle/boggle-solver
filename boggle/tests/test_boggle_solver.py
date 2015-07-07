"""
Tests for solving a game of Boggle.
"""

import unittest

from boggle.boggle import (
    list_words,
    positions_touching,
    tiles_available,
    get_tile_map,
    is_available_route,
    is_valid_route,
    is_valid_word,
)


class IsValidWord(unittest.TestCase):
    """
    Tests for `is_valid_word`.
    """

    def test_valid_word(self):
        """
        Words of at least three letters which have an available route are
        valid.
        """
        self.assertFalse(
            is_valid_word(
                word='AB',
                tile_map=get_tile_map(
                   board=[
                       ['A', 'B'],
                    ],
                )
            )
        )

    def test_short_word(self):
        """
        Words shorter than 3 letters are not valid.
        """
        self.assertFalse(
            is_valid_word(
                word='AB',
                tile_map=get_tile_map(
                   board=[
                       ['A', 'B'],
                    ],
                )
            )
        )

    def test_no_route(self):
        """
        Words without an available route are not valid.
        """
        self.assertFalse(
            is_valid_word(
                word='ABC',
                tile_map=get_tile_map(
                   board=[
                       ['A', 'C', 'B'],
                    ],
                )
            )
        )

    def test_q_u_together(self):
        """
        Q and u are on the same tile, so a word consisting of two tiles but
        three letters is valid.
        """
        self.assertTrue(
            is_valid_word(
                word='QUA',
                tile_map=get_tile_map(
                    board=[
                        ['Qu', 'A'],
                    ],
                ),
            ),
        )

    def test_case_insensitive(self):
        """
        A word is valid regardless of case.
        """
        self.assertTrue(
            is_valid_word(
                word='AbC',
                tile_map=get_tile_map(
                    board=[
                        ['A', 'B', 'C'],
                    ],
                ),
            ),
        )


class GetTileMapTests(unittest.TestCase):
    """
    Tests for `get_tile_map`.
    """

    def test_tile_map(self):
        """
        Tiles are mapped to positions they appear in.
        """
        self.assertEqual(
            {
                'A': [(0, 0), (1, 0), (0, 1)],
                'B': [(1, 1)],
            },
            get_tile_map(
                board=[
                    ['A', 'A'],
                    ['A', 'B'],
                ],
            )
        )

    def test_lowercase(self):
        """
        Lowercase tiles are mapped to their uppercase counterparts.
        """
        self.assertEqual(
            {
                'A': [(0, 0)],
            },
            get_tile_map(
                board=[
                    ['a'],
                ],
            )
        )

    def test_qu_mapped_to_u(self):
        """
        "Qu" tiles are mapped to "Q".
        """
        self.assertEqual(
            {
                'Q': [(0, 0)],
            },
            get_tile_map(
                board=[
                    ['Qu'],
                ],
            )
        )


class TilesAvailableTests(unittest.TestCase):
    """
    Tests for `tiles_available`.
    """

    def test_tile_available(self):
        """
        True is returned if all there are enough available tiles of each type.
        """
        self.assertTrue(
            tiles_available(
                word='ABC',
                tile_map=get_tile_map(
                    board=[
                        ['A', 'C', 'B'],
                    ],
                ),
            )
        )

    def test_tile_unavailable(self):
        """
        False is returned if a tile is unavailable.
        """
        self.assertFalse(
            tiles_available(
                word='A',
                tile_map=get_tile_map(
                    board=[
                        ['B'],
                    ],
                ),
            )
        )

    def test_not_enough_tiles(self):
        """
        False is returned if there are fewer instances of a tile in the board
        than the given word.
        """
        self.assertFalse(
            tiles_available(
                word='AA',
                tile_map=get_tile_map(
                    board=[
                        ['A'],
                    ],
                ),
            )
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
                tile_map=get_tile_map([
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
                tile_map=get_tile_map([
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
                tile_map=get_tile_map([
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
                word_list=set(['ABC', 'DEF', 'GHI']),
                board=[
                    ['A', 'B', 'C'],
                    ['D', 'E', 'F'],
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
