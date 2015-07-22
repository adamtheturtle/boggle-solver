class Tile(object):

    def __init__(self, column, row):
        """
        # TODO doc
        """
        self.column = column
        self.row = row

    def __eq__(self, other):
        """
        Tiles are equal iff they are in the same position.

        # TODO doc other
        """
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


class Word(object):
    """
    """

    def __init__(self, word):
        """docstring for __init__"""
        self.word = word.upper()
        self.length = len(self.word)
        self.tiles = self.to_tiles(self.word)


    def to_tiles(self, word):
        """
        Return the list of tile contents necessary to form a word.

        A list of the letters in a string, except 'QU' is a tile and Q is not.

        word: A string.
        return: List of strings.
        """
        word = word.replace('QU', 'Q')
        tiles = []
        for letter in word:
            if letter == 'Q':
                tiles.append('QU')
            else:
                tiles.append(letter)
        return tiles


class Board(object):

    def __init__(self, rows):
        """docstring for __init__"""
        self.tile_map = self._get_tile_map(rows)

    def _get_tile_map(self, board):
        """
        Get a mapping of tiles to positions.

        board: A list of lists of tiles. Each list in the list of lists represents
            a row of a Boggle board.

        return: Dictionary, each key representing a tile content.
        """
        mapping = {}
        for row_index, row in enumerate(board):
            for column_index, piece in enumerate(row):
                # TODO handle case where a key is not valid
                key = piece.upper()
                tile = Tile(column=column_index, row=row_index)
                try:
                    mapping[key].append(tile)
                except KeyError:
                    mapping[key] = [tile]
        return mapping

    def occurences(self, tile):
        """
        TODO

        returns set of tiles
        """
        if tile in self.tile_map:
            return self.tile_map[tile]

        return set([])

def is_available_route(word, board):
    """
    Check if there is an available route to make a word in a board.

    A route is a path of positions from first tile to next, to next... until
    the last tile. It cannot include the same tile multiple times.

    word: A string.
    tile_map: Map of tiles to positions those tiles are in.

    returns: Boolean, True iff there is a valid route.
    """
    routes = []

    tiles = word.tiles
    num_tiles = len(tiles)

    for tile in tiles:
        positions = board.occurences(tile)
        new_routes = []

        for route in routes:
            last_position = route[len(route) - 1]
            for position in positions:
                if position.touching(last_position) and position not in route:
                    new_route = route[:]
                    new_route.append(position)
                    includes_whole_word = len(new_route) == num_tiles
                    if includes_whole_word:
                        return True
                    new_routes.append(new_route)

        if not routes:
            routes = routes or [[position] for position in positions]
            continue

        if not new_routes:
            return False

        routes = new_routes


def tiles_available(word, board):
    """
    Check if there are enough of each required tile to make a word.

    word: A string.
    tile_map: A mapping of tiles available in a Boggle board to positions on
        that board.

    return: Boolean, True iff all tiles are available.
    """
    for tile in word.tiles:
        if word.tiles.count(tile) > len(board.occurences(tile)):
            return False
    return True


def is_valid_word(word, board):
    """
    Return whether a word is valid and can be found on a board.

    word: A string.
    tile_map: A mapping of tiles available in a Boggle board to positions on
        that board.

    return: Boolean, True iff a word is valid.
    """
    return (word.length > 2 and
            tiles_available(word=word, board=board) and
            is_available_route(word=word, board=board))


def list_words(board, word_list):
    """
    Return all words from a given dictionary which are in a board.

    word_list: A set of valid words.
    board: A list of lists of tiles. Each list in the list of lists represents
        a row of a Boggle board.

    returns: A set of strings.
    """
    board = Board(rows=board)
    return set([word.upper() for word in word_list if
               is_valid_word(Word(word=word), board)])
