from __future__ import print_function

import copy
import io

# TODO Add pyflakes to travis
# TODO add a way to input a board (text file / photo)
# TODO possible optimisations -
#   * Decrease the dictionary length to remove "'"s etc.
#   * Decrease the dictionary length to remove two letter words.
#   * Stop after one valid route


def get_positions(letter, board):
    """
    Return a list of positions a letter can be found on a board.

    letter: A letter on a tile.
    return: List of (column, row) co-ordinates of tiles containing this letter.
    """
    positions = []
    for row_index, row in enumerate(board):
        for column_index, piece in enumerate(row):
            if piece[0].upper() == letter[0].upper():
                positions.append((column_index, row_index))
    return positions


def positions_touching(first, second):
    """
    Given two tile positions, check whether they are touching.

    first: Tuple of co-ordinates of a tile.
    second: Tuple of co-ordinates of a tile.

    return: Bool, true iff the tiles are touching - immediately above, below
        or diagonal.
    """
    return abs(first[0] - second[0]) <= 1 and abs(first[1] - second[1]) <= 1


def get_routes(word, board):
    """
    Get available routes to make a word in a board.

    A route is a path of positions from first tile to next, to next... until
    the last tile. It cannot include the same tile multiple times.

    word: A string.
    board: A list of lists of tiles. Each list in the list of lists represents
        a row of a Boggle board.

    returns: List of lists of tile positions.
    """
    routes = []

    for letter in word:
        positions = get_positions(letter, board)
        if not len(routes):
            new_routes = [[position] for position in positions]
        else:
            new_routes = []

            for route in routes:
                for position in positions:
                    if positions_touching(route[len(route) - 1], position):
                        new_route = copy.copy(route)
                        new_route.append(position)
                        new_routes.append(new_route)

        routes = copy.copy(new_routes)

    valid_routes = []
    for route in routes:
        no_duplicates = len(set(route)) == len(route)
        includes_whole_word = len(route) == len(word)
        if no_duplicates and includes_whole_word:
            valid_routes.append(route)

    return valid_routes


def list_words(board, dictionary):
    """
    Return all words from a given dictionary which are in a board.

    dictionary: A set of valid words.
    board: A list of lists of tiles. Each list in the list of lists represents
        a row of a Boggle board.

    returns: A set of strings.
    """
    word_list = set()
    for word in dictionary:
        word = word.upper()
        routes = get_routes(word.replace('QU', 'Q'), board)
        if len(routes) and len(word) > 2:
            word_list.add(word)
    return word_list

if __name__ == "__main__":
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
