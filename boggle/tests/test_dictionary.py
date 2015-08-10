"""
Tests for :class:`Dictionary`
"""

import io
from tempfile import mkstemp
from textwrap import dedent
import unittest

from boggle.boggle import Dictionary


class WordsTests(unittest.TestCase):
    """
    Tests for `Dictionary.words`.
    """

    def test_words(self):
        """
        A list of words from a file with whitespace stripped is returned.
        """
        file, path = mkstemp()
        with io.open(path, mode='w') as file:
            file.write(dedent(u"""\
            ABC
             DEF
            GHI  """))

        self.assertEqual(
            Dictionary(path=path).words,
            set(["ABC", "DEF", "GHI"]),
        )
