import io


class Position(object):
    """
    The position of a tile on a Boggle board.
    """

    def __init__(self, column, row):
        """
        :param int column: Column of the tile.
        :param int row: Row of the tile.
        """
        self.column = column
        self.row = row

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        """
        Return whether two positions are equal.
        Positions are equal iff they have the same row and column.

        :param Position other: A position to check for equality with self.
        """
        return self.row == other.row and self.column == other.column

    def touching(self, other):
        """
        Return whether two positions are touching.

        :param Position other: A position to check for equality with self.

        :return bool: True iff the tiles are touching - immediately above,
        below or diagonal.
        """
        return(
            abs(self.row - other.row) <= 1 and
            abs(self.column - other.column) <= 1)


class Word(object):
    """
    A string which can be represented by a list of strings which are each valid
    tiles.
    """

    def __init__(self, string, valid_tiles):
        """
        :param str string: A word from a dictionary, valid if found on a Board.
        :param set valid_tiles: Strings, all tile contents which are valid.

        :ivar int string_length: The length of the ``string``.
        :ivar list tiles: strings, each valid contents of a tile, joined makes
            the word's string, or an empty list if the word cannot be created
            from valid tiles.
        """
        string = string.upper()

        self.tiles = []
        string_length = len(string)
        start = 0
        while start < string_length:
            valid_tile_added = False
            for tile in valid_tiles:
                tile_length = len(tile)
                if string[start:start + tile_length] == tile.upper():
                    start += tile_length
                    self.tiles.append(tile)
                    valid_tile_added = True
                    continue
            if not valid_tile_added:
                self.tiles = []
                break


class Board(object):
    """
    Representation of a Boggle-like board. A board contains tiles at
    co-ordinates with letters on them.
    """

    def __init__(self, rows):
        """
        :param list rows: Lists of tiles. Each tile is a string.
        """
        self._tile_map = {}
        for row_index, row in enumerate(rows):
            for column_index, tile in enumerate(row):
                # TODO get the case matching piece here
                position = Position(column=column_index, row=row_index)
                if tile in self._tile_map:
                    self._tile_map[tile].add(position)
                else:
                    self._tile_map[tile] = set([position])

    def is_available_route(self, word):
        """
        Check if there is an available route to make a word in a board.

        A route is a path of positions from first tile to next, to next...
        until the last tile. It cannot include the same tile multiple times.

        :param Word word: Word to look for in the board.

        :return bool: True iff there is a valid route.
        """
        routes = []

        for tile in word:
            if tile not in self._tile_map:
                return False

            positions = self._tile_map[tile]
            new_routes = []

            if not routes:
                routes = [[position] for position in positions]
                continue

            for route in routes:
                route_length = len(route)
                last_position = route[route_length - 1]
                for position in positions:
                    if (position.touching(last_position) and
                            position not in route):

                        if route_length + 1 == len(word):
                            return True
                        new_route = route[:]
                        new_route.append(position)
                        new_routes.append(new_route)

            routes = new_routes

            if not routes:
                return False


class Boggle(object):
    """
    A Boggle game.
    """

    valid_tiles = set([
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Qu', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    ])

    def __init__(self, board, valid_words):
        """
        :param Board board: The board to play the game on.
        :param set valid_words: Words valid in the game.
        """
        self.board = board
        self.valid_words = valid_words

    def string_to_tiles(self, string, valid_tiles):
        string = string.upper()

        tiles = []
        string_length = len(string)
        start = 0
        while start < string_length:
            valid_tile_added = False
            for tile in valid_tiles:
                tile_length = len(tile)
                if string[start:start + tile_length] == tile.upper():
                    start += tile_length
                    tiles.append(tile)
                    valid_tile_added = True
                    continue
            if not valid_tile_added:
                tiles = []
                break

        return tiles

    def _matching_words(self):
        """
        :return set: :py:class:`Word`s which exist in the word list and can be
            found.
        """

        words = [self.string_to_tiles(string=string, valid_tiles=self.valid_tiles) for string in self.valid_words if len(string) > 2]

        return [word for word in words if self.board.is_available_route(word=word)]

    def list_words(self):
        """
        :return set: Strings which are valid and can be found on the ``board``.
        """
        matching_words = self._matching_words()
        return set(["".join(word) for word in matching_words])


class Dictionary(object):
    """
    Valid words for a Boggle game.
    """

    def __init__(self, path="/usr/share/dict/words"):
        """
        :param string path: Path to a list of words valid in a game.

        :ivar set words: All words in the dictionary file.
        """
        with io.open(path, encoding='latin-1') as word_file:
            self.words = set(word.strip() for word in word_file)


def list_words(board, dictionary_path=None):
    board = Board(rows=board)
    dictionary = Dictionary()
    boggle = Boggle(board=board, valid_words=dictionary.words)
    return boggle.list_words()
