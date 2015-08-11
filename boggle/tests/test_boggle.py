"""
Tests for a Boggle solver.
"""

import unittest
import io

from tempfile import mkstemp
from textwrap import dedent

from boggle.boggle import Board, Boggle, Language, Word, Position


class LanguageTests(unittest.TestCase):
    """
    Tests for `Language`.
    """

    def test_words(self):
        """
        A list of list of tiles is returned, each representing the words which
        can exist on a board.
        """
        file, path = mkstemp()
        with io.open(path, mode='w') as file:
            file.write(dedent(u"""\
            ABC
             DEF
            GHI  """))

        self.assertEqual(
            sorted(Language(path=path).words),
            sorted([['A', 'B', 'C'], ['G', 'H', 'I'], ['D', 'E', 'F']]),
        )

    def test_short_words_not_listed(self):
        """
        Words shorter than 3 letters are not listed as valid results.
        """
        file, path = mkstemp()
        with io.open(path, mode='w') as file:
            file.write(u"AB")

        self.assertEqual(
            Language(path=path).words,
            [],
        )


class BoggleTests(unittest.TestCase):
    """
    Tests for `Boggle`.
    """

    def test_list_words(self):
        """
        A set of words with available routes is returned.
        """
        board = Board(rows=[
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
        ])
        valid_words = set(['ABC', 'DEF', 'GHI'])
        self.assertEqual(
            Boggle(board=board, valid_words=valid_words).list_words(),
            set(['ABC', 'DEF']),
        )

    def test_no_route_not_listed(self):
        """
        Words without an available route are not listed as valid results.
        """
        board = Board(rows=[
            ['A', 'B', 'C'],
        ])
        valid_words = set(['ACB'])
        self.assertEqual(
            Boggle(board=board, valid_words=valid_words).list_words(),
            set([]),
        )


class TilesTests(unittest.TestCase):
    """
    Tests for :py:func:`Word.tiles`
    """
    def test_word_from_tiles(self):
        """
        :py:func:`Word.tiles` is a list of valid tiles which make up a string.
        """
        self.assertEqual(
            Word(string='ABC', valid_tiles=set(['C', 'AB'])).tiles,
            ['AB', 'C'],
        )

    def test_impossible_word(self):
        """
        :py:func:`Word.tiles` is an empty list if a the string cannot be made
            by the component tiles.
        """
        self.assertEqual(
            Word(string='ABCD', valid_tiles=set(['C', 'AB'])).tiles,
            [],
        )

    def test_string_case_insensitive(self):
        """
        A given string's case does not change the tile list.
        """
        self.assertEqual(
            Word(string='abc', valid_tiles=set(['C', 'AB'])).tiles,
            ['AB', 'C'],
        )

    def test_tile_case_insensitive(self):
        """
        An unmatching tile's case appears in the tile list.
        """
        self.assertEqual(
            Word(string='ABC', valid_tiles=set(['C', 'Ab'])).tiles,
            ['Ab', 'C'],
        )


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

        self.assertTrue(board.is_available_route(word=['A', 'B', 'C']))

    def test_not_in_board(self):
        """
        If a word is not available in the board, False is returned.
        """
        board = Board(rows=[
            ['A', 'C', 'B'],
        ])

        self.assertFalse(board.is_available_route(word=['A', 'B', 'C']))

    def test_repeated_tile(self):
        """
        A route which uses the same tile multiple times is not valid, so if
        this is the only available route, False is returned.
        """
        board = Board(rows=[
            ['A', 'B'],
        ])

        self.assertFalse(board.is_available_route(word=['A', 'B', 'A']))


class PositionTouchingTests(unittest.TestCase):
    """
    Tests for `Position.touching`.
    """

    def test_touching(self):
        """
        If positions are touching, True is returned.
        """
        position = Position(column=1, row=1)
        self.assertTrue(
            all([
                # Second on right on first.
                position.touching(Position(column=2, row=1)),
                # Second on left of first.
                position.touching(Position(column=0, row=1)),
                # Second above first.
                position.touching(Position(column=1, row=0)),
                # Second below first.
                position.touching(Position(column=1, row=2)),
                ],
                ))

    def test_not_touching(self):
        """
        If positions are not touching, False is returned.
        """
        tile = Position(column=1, row=1)
        self.assertFalse(tile.touching(Position(column=3, row=3)))


class PositionEqualityTests(unittest.TestCase):
    """
    Tests for `Position.__eq__`
    """

    def test_same_row_same_column_equal(self):
        """
        Positions with the same row and column are equal.
        """
        self.assertEqual(
            Position(column=0, row=0),
            Position(column=0, row=0),
        )

    def test_different_column_not_equal(self):
        """
        Positions with the same row but a different column are not equal.
        """
        self.assertNotEqual(
            Position(column=0, row=0),
            Position(column=1, row=0),
        )

    def test_different_crow_not_equal(self):
        """
        Positions with the same column but a different row are not equal.
        """
        self.assertNotEqual(
            Position(column=0, row=0),
            Position(column=0, row=1),
        )
