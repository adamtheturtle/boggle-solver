"""
Tests for :class:`Boggle`
"""

import unittest

from boggle.boggle import Board, Boggle


class BoggleTests(unittest.TestCase):
    """
    Tests for `Boggle`.
    """

    def test_default_valid_tiles(self):
        """
        The default valid tiles are the same as in the English version of
        Boggle.
        """
        board = Board(rows=[
            ['A', 'B', 'C'],
        ])

        self.assertEqual(
            Boggle(board=board, word_list=[]).valid_tiles,
            set([
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Qu', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z',
            ]),
        )

    def test_list_words(self):
        """
        A set of words with available routes is returned.
        """
        board = Board(rows=[
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
        ])
        word_list = set(['ABC', 'DEF', 'GHI'])
        self.assertEqual(
            Boggle(board=board, word_list=word_list).list_words(),
            set(['ABC', 'DEF']),
        )

    def test_short_words_not_listed(self):
        """
        Words shorter than 3 letters are not listed as valid results.
        """
        board = Board(rows=[
            ['A', 'B', 'C'],
        ])
        word_list = set(['AB'])
        self.assertEqual(
            Boggle(board=board, word_list=word_list).list_words(),
            set([]),
        )

    def test_no_route_not_listed(self):
        """
        Words without an available route are not listed as valid results.
        """
        board = Board(rows=[
            ['A', 'B', 'C'],
        ])
        word_list = set(['ACB'])
        self.assertEqual(
            Boggle(board=board, word_list=word_list).list_words(),
            set([]),
        )
