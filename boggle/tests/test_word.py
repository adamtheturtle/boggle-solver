"""
Tests for :class:`Word`
"""

import unittest

from boggle.boggle import Word


class GetTilesTests(unittest.TestCase):
    """
    Tests for :py:func:`Word.get_tiles`
    """
    def test_word_from_tiles(self):
        """
        :py:func:`Word.get_tiles` returns a list of valid tiles which make up
            a string.
        """
        self.assertEqual(
            Word(string='ABC', valid_tiles=set(['C', 'AB'])).get_tiles(),
            ['AB', 'C'],
        )

    def test_impossible_word(self):
        """
        :py:func:`Word.get_tiles` returns empty list if a the string cannot be
            made by the component tiles.
        """
        self.assertEqual(
            Word(string='ABCD', valid_tiles=set(['C', 'AB'])).get_tiles(),
            [],
        )

    def test_string_case_insensitive(self):
        """
        A given string's case does not change the tile list.
        """
        self.assertEqual(
            Word(string='abc', valid_tiles=set(['C', 'AB'])).get_tiles(),
            ['AB', 'C'],
        )

    def test_tile_case_insensitive(self):
        """
        An unmatching tile's case appears in the tile list.
        """
        self.assertEqual(
            Word(string='ABC', valid_tiles=set(['C', 'Ab'])).get_tiles(),
            ['Ab', 'C'],
        )
