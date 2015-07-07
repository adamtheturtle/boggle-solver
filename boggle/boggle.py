import copy

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


def is_valid_route(word, route):
    """
    Check if a route is valid.

    A route is valid if it contains the same number of letters as the word it
    represents and does not use the same tile multiple times.

    word: A string.
    route: A list of tile positions.

    return: Boolean, True iff a route is valid.
    """
    no_duplicates = len(set(route)) == len(route)
    includes_whole_word = len(route) == len(word)
    return no_duplicates and includes_whole_word


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

    return [route for route in routes if is_valid_route(word, route)]


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
