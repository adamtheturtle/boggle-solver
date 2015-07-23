"""
Tests for :class:`Word`
"""

import unittest

from boggle.boggle import Word


class WordTests(unittest.TestCase):
    """
    Tests for :class:`Word`
    """
    def test_word_from_tiles(self):
        """
        Word.tiles is a list of valid tiles which make up a string.
        """
        self.assertEqual(
            Word(string='ABC', valid_tiles=set(['C', 'AB'])).tiles,
            ['AB', 'C'],
        )

    def test_impossible_word(self):
        """
        Word.tiles is an empty list if a the string cannot be made by the
        component tiles.
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
