import copy

# TODO add a way to input a board (text file / photo)


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


def is_available_route(word, tile_map):
    """
    Check if there is an available route to make a word in a board.

    A route is a path of positions from first tile to next, to next... until
    the last tile. It cannot include the same tile multiple times.

    word: A string.
    tile_map: Map of tiles to positions those tiles are in.

    returns: Boolean, True iff there is a valid route.
    """
    routes = []

    if not tiles_available(word=word, tile_map=tile_map):
        return False

    for letter in word:
        positions = tile_map[letter]
        if not len(routes):
            routes = [[position] for position in positions]
        else:
            new_routes = []

            for route in routes:
                for position in positions:
                    if positions_touching(route[len(route) - 1], position):
                        new_route = copy.copy(route)
                        new_route.append(position)
                        if is_valid_route(word, new_route):
                            return True
                        new_routes.append(new_route)

            routes = copy.copy(new_routes)

    return False


def get_tile_map(board):
    """
    Get a mapping of tiles to positions.

    board: A list of lists of tiles. Each list in the list of lists represents
        a row of a Boggle board.

    return: Dictionary, each key representing a tile content (letter of
        alphabet [not Q] or Qu)
    """
    mapping = {}
    for row_index, row in enumerate(board):
        for column_index, piece in enumerate(row):
            tile = board[row_index][column_index].upper().replace('QU', 'Q')
            position = (column_index, row_index)
            try:
                mapping[tile].append(position)
            except KeyError:
                mapping[tile] = [position]
    return mapping


def tiles_available(word, tile_map):
    """
    Check if there are enough of each required tile to make a word.

    word: A string.
    tile_map: A mapping of tiles available in a Boggle board to positions on
        that board.

    return: Boolean, True iff all tiles are available.
    """
    for letter in word:
        try:
            if word.count(letter) > len(tile_map[letter]):
                return False
        except KeyError:
            return False
    return True


def is_valid_word(word, tile_map):
    """
    Return whether a word is valid and can be found on a board.

    word: A string.
    tile_map: A mapping of tiles available in a Boggle board to positions on
        that board.

    return: Boolean, True iff a word is valid.
    """
    long_enough = len(word) > 2
    word = word.upper().replace('QU', 'Q')
    return (long_enough and
            is_available_route(word=word, tile_map=tile_map))


def list_words(board, word_list):
    """
    Return all words from a given dictionary which are in a board.

    word_list: A set of valid words.
    board: A list of lists of tiles. Each list in the list of lists represents
        a row of a Boggle board.

    returns: A set of strings.
    """
    tile_map = get_tile_map(board)
    valid_words = filter(lambda word: is_valid_word(word, tile_map), word_list)
    return set(map(lambda word: word.upper(), valid_words))
