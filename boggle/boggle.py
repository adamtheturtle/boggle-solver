class Tile(object):

    def __init__(self, column, row):
        self.column = column
        self.row = row

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def touching(self, other):
        """
        Given another, check whether it is touching this tile.

        second: A Tile.

        return: Bool, true iff the tiles are touching - immediately above,
            below or diagonal.
        """
        return(
            abs(self.row - other.row) <= 1 and
            abs(self.column - other.column) <= 1)


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

    word_length = len(word)

    for letter in word:
        positions = tile_map[letter]
        new_routes = []

        for route in routes:
            last_position = route[len(route) - 1]
            for position in positions:
                if position.touching(last_position) and position not in route:
                    new_route = route[:]
                    new_route.append(position)
                    includes_whole_word = len(new_route) == word_length
                    if includes_whole_word:
                        return True
                    new_routes.append(new_route)

        if not len(routes):
            routes = routes or [[position] for position in positions]
            continue

        if not new_routes:
            return False

        routes = new_routes


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
            position = Tile(column=column_index, row=row_index)
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
            tiles_available(word=word, tile_map=tile_map) and
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
    word_list = set([word.upper() for word in word_list])
    return set([word for word in word_list if is_valid_word(word, tile_map)])
