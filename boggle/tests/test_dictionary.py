"""
Tests for :class:`Dictionary`
"""

import io
from tempfile import mkstemp
from textwrap import dedent
import unittest

from boggle.boggle import Dictionary


class GetWordsTests(unittest.TestCase):
    """
    Tests for `Dictionary.get_words`.
    """

    def test_get_words(self):
        """
        A list of words from a file with whitespace stripped is returned.
        """
        file, path = mkstemp()
        with io.open(path, mode='w') as file:
            file.write(dedent(str("""\
            ABC
             DEF
            GHI  """)))

        self.assertEqual(
            Dictionary(path=path).get_words(),
            set(["ABC", "DEF", "GHI"]),
        )
