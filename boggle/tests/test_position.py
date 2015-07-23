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
