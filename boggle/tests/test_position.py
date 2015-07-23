"""
Tests for solving a game of Boggle.
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
# class GetTileMapTests(unittest.TestCase):
#     """
#     Tests for `get_tile_map`.
#     """
#
#     def test_tile_map(self):
#         """
#         Tiles are mapped to positions they appear in.
#         """
#         self.assertEqual(
#             {
#                 'A': [
#                     Tile(column=0, row=0),
#                     Tile(column=1, row=0),
#                     Tile(column=0, row=1),
#                 ],
#                 'B': [
#                     Tile(column=1, row=1),
#                 ],
#             },
#             get_tile_map(
#                 board=[
#                     ['A', 'A'],
#                     ['A', 'B'],
#                 ],
#             )
#         )
#
#     def test_lowercase(self):
#         """
#         Lowercase tiles are mapped to their uppercase counterparts.
#         """
#         self.assertEqual(
#             {
#                 'A': [
#                     Tile(column=0, row=0),
#                 ],
#             },
#             get_tile_map(
#                 board=[
#                     ['a'],
#                 ],
#             )
#         )
#
#
# class TilesAvailableTests(unittest.TestCase):
#     """
#     Tests for `tiles_available`.
#     """
#
#     def test_tile_available(self):
#         """
#         True is returned if all there are enough available tiles of each type.
#         """
#         self.assertTrue(
#             tiles_available(
#                 word='ABC',
#                 tile_map=get_tile_map(
#                     board=[
#                         ['A', 'C', 'B'],
#                     ],
#                 ),
#             )
#         )
#
#     def test_tile_unavailable(self):
#         """
#         False is returned if a tile is unavailable.
#         """
#         self.assertFalse(
#             tiles_available(
#                 word='A',
#                 tile_map=get_tile_map(
#                     board=[
#                         ['B'],
#                     ],
#                 ),
#             )
#         )
#
#     def test_not_enough_tiles(self):
#         """
#         False is returned if there are fewer instances of a tile in the board
#         than the given word.
#         """
#         self.assertFalse(
#             tiles_available(
#                 word='AA',
#                 tile_map=get_tile_map(
#                     board=[
#                         ['A'],
#                     ],
#                 ),
#             )
#         )
#
#
# class IsAvailableRouteTests(unittest.TestCase):
#     """
#     Tests for `is_available_route`.
#     """
#
#     def test_route(self):
#         """
#         If there is a route between each letter, True is returned.
#         """
#         self.assertTrue(
#             is_available_route(
#                 word='ABC',
#                 tile_map=get_tile_map([
#                     ['A', 'B', 'C'],
#                 ]),
#             )
#         )
#
#     def test_not_in_board(self):
#         """
#         If a word is not available in the board, False is returned.
#         """
#         self.assertFalse(
#             is_available_route(
#                 word='ABC',
#                 tile_map=get_tile_map([
#                     ['A', 'C', 'B'],
#                 ]),
#             )
#         )
#
#     def test_repeated_tile(self):
#         """
#         A route which uses the same tile multiple times is not valid, so if
#         this is the only available route, False is returned.
#         """
#         self.assertFalse(
#             is_available_route(
#                 word='ABA',
#                 tile_map=get_tile_map([
#                     ['A', 'B'],
#                 ]),
#             )
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
#
#
# class ToTilesTests(unittest.TestCase):
#     """
#     Tests for `to_tiles`.
#     """
#
#     def test_to_tiles(self):
#         """
#         A list of letters is returned, except "QU" is a tile.
#         """
#         self.assertEqual(
#             to_tiles("ABQUC"),
#             ["A", "B", "QU", "C"],
#         )
