from __future__ import print_function
import io

from boggle.boggle import list_words

with io.open("english_words.txt", encoding='latin-1') as word_file:
    english_words = set(word.strip() for word in word_file)

found_words = list_words(
    dictionary=english_words,
    board=[
        ['Qu', 'A', 'A', 'M', 'D'],
        ['A', 'L', 'G', 'O', 'O'],
        ['R', 'G', 'I', 'D', 'E'],
        ['O', 'N', 'F', 'Y', 'R'],
        ['R', 'E', 'L', 'L', 'S'],
    ],
)
print(len(found_words))
from pprint import pprint
pprint(sorted(list(found_words)))
