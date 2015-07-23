"""
Tests for :class:`Position`.
"""

import unittest

from boggle.boggle import Position


class TouchingTests(unittest.TestCase):
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


class EqualityTests(unittest.TestCase):
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
#
# class IsValidWord(unittest.TestCase):
#     """
#     Tests for `is_valid_word`.
#     """
#
#     def test_valid_word(self):
#         """
#         Words of at least three letters which have an available route are
#         valid.
#         """
#         self.assertTrue(
#             is_valid_word(
#                 word='ABC',
#                 tile_map=get_tile_map(
#                     board=[
#                         ['A', 'B', 'C'],
#                     ],
#                 )
#             )
#         )
#
#     def test_short_word(self):
#         """
#         Words shorter than 3 letters are not valid.
#         """
#         self.assertFalse(
#             is_valid_word(
#                 word='AB',
#                 tile_map=get_tile_map(
#                     board=[
#                         ['A', 'B'],
#                     ],
#                 )
#             )
#         )
#
#     def test_no_route(self):
#         """
#         Words without an available route are not valid.
#         """
#         self.assertFalse(
#             is_valid_word(
#                 word='ABC',
#                 tile_map=get_tile_map(
#                     board=[
#                         ['A', 'C', 'B'],
#                     ],
#                 )
#             )
#         )
#
#     def test_q_u_together(self):
#         """
#         Q and u are on the same tile, so a word consisting of two tiles but
#         three letters is valid.
#         """
#         self.assertTrue(
#             is_valid_word(
#                 word='QUA',
#                 tile_map=get_tile_map(
#                     board=[
#                         ['Qu', 'A'],
#                     ],
#                 ),
#             ),
#         )
#
#
# class ListWordsTests(unittest.TestCase):
#     """
#     Tests for `list_words`.
#     """
#
#     def test_list_words(self):
#         """
#         A set of available words is returned.
#         """
#         self.assertEqual(
#             set(['ABC', 'DEF']),
#             list_words(
#                 word_list=set(['ABC', 'DEF', 'GHI']),
#                 board=[
#                     ['A', 'B', 'C'],
#                     ['D', 'E', 'F'],
#                 ],
#             )
#         )
#
#     def test_case_insensitive(self):
#         """
#         A word is valid regardless of case.
#         """
#         self.assertEqual(
#             set(['ABC']),
#             list_words(
#                 word_list=set(['abc']),
#                 board=[
#                     ['A', 'B', 'C'],
#                 ],
#             )
#         )
#
#     def test_no_duplicates(self):
#         """
#         Words which, ignoring case, are duplicated in the word list, are only
#         returned once.
#         """
#         self.assertEqual(
#             set(['ABC']),
#             list_words(
#                 word_list=set(['ABC', 'abc']),
#                 board=[
#                     ['A', 'B', 'C'],
#                 ],
#             )
#         )
