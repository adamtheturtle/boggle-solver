"""
Tests for :class:`Board`
"""

import unittest

from boggle.boggle import Board, Word, Boggle

class IsValidWord(unittest.TestCase):
    """
    Tests for `is_valid_word`.
    """

    def test_valid_word(self):
        """
        Words of at least three letters which have an available route are
        valid.
        """
        self.assertTrue(
            is_valid_word(
                word='ABC',
                tile_map=get_tile_map(
                    board=[
                        ['A', 'B', 'C'],
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

    def test_case_insensitive(self):
        """
        A word is valid regardless of case.
        """
        self.assertEqual(
            set(['ABC']),
            list_words(
                word_list=set(['abc']),
                board=[
                    ['A', 'B', 'C'],
                ],
            )
        )

    def test_no_duplicates(self):
        """
        Words which, ignoring case, are duplicated in the word list, are only
        returned once.
        """
        self.assertEqual(
            set(['ABC']),
            list_words(
                word_list=set(['ABC', 'abc']),
                board=[
                    ['A', 'B', 'C'],
                ],
            )
        )
