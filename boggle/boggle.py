# TODO support multiple languages, with different valid words sections
# TODO generate api docs
# TODO change from word_list to word file
# TODO create a UI
# TODO create a "fromString" thing, then you can have a CLI shared with other
# languages
# TODO Also include a generator, to make random games
# TODO handle case where a key in the board is not valid
# TODO main docstring with my name, description of the project etc.


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

    valid_tiles = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'QU', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    ]

    def __init__(self, word):
        """
        :param str word: A word from a dictionary, valid if found on a Board.
        """
        self.word = word.upper()

    def to_tiles(self):
        """
        Return the list of tile contents necessary to form a word.

        A list of the letters in a string, except 'QU' is a tile and Q is not.

        :return list: strings, each valid contents of a tile.
        """
        word = self.word
        tiles = []
        while len(word):
            valid_tile_added = False
            for tile in self.valid_tiles:
                if word.startswith(tile):
                    word = word[len(tile):]
                    tiles.append(tile)
                    valid_tile_added = True
                    continue
            if not valid_tile_added:
                return []
        return tiles


class Board(object):
    """
    Representation of a Boggle-like board. A board contains tiles at
    co-ordinates with letters on them.
    """

    def __init__(self, rows):
        self.tile_map = self._get_tile_map(rows)

    def _get_tile_map(self, rows):
        """
        Get a mapping of tiles to positions.

        :param list rows: Lists of tiles. Each tile is a string.

        return: Dictionary, each key representing a tile content.
        """
        mapping = {}
        for row_index, row in enumerate(rows):
            for column_index, piece in enumerate(row):
                tile = piece.upper()
                position = Position(column=column_index, row=row_index)
                if tile in mapping:
                    mapping[tile].append(position)
                else:
                    mapping[tile] = [position]
        return mapping

    def _occurences(self, tile):
        """
        TODO

        returns set of tiles
        """
        if tile in self.tile_map:
            return self.tile_map[tile]

        return set([])

    def is_available_route(self, word):
        """
        Check if there is an available route to make a word in a board.

        A route is a path of positions from first tile to next, to next... until
        the last tile. It cannot include the same tile multiple times.

        word: A string.
        tile_map: Map of tiles to positions those tiles are in.

        returns: Boolean, True iff there is a valid route.
        """
        if not self._tiles_available:
            return False

        routes = []

        tiles = word.to_tiles()
        num_tiles = len(tiles)

        for tile in tiles:
            positions = self._occurences(tile)
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

            routes = new_routes

            if not routes:
                return False

    def _tiles_available(self, word):
        """
        Check if there are enough of each required tile to make a word.

        word: A string.
        tile_map: A mapping of tiles available in a Boggle board to positions on
            that board.

        return: Boolean, True iff all tiles are available.
        """
        for tile in word.tile_list:
            if word.num_occurences(tile) > len(self._occurences(tile)):
                return False
        return True


class Boggle(object):
    """
    A Boggle game.
    """

    def __init__(self, board, word_list):
        """
        :param Board board: The board to play the game on.
        :param list word_list: A list of words valid in the game.
        """
        self.board = board
        self.word_list = word_list

    def _matching_words(self):
        """
        :return set: :py:class:`Word`s which exist in the word list and can be
            found.
        """
        found = set([])
        for item in self.word_list:
            word = Word(word=item)
            if len(item) > 2 and self.board.is_available_route(word=word):
                found.add(word)
        return found

    def list_words(self):
        """
        :return set: Words which are valid and can be found on the ``board``.
        """
        matching_words = self._matching_words()
        return set([word.word for word in matching_words])


def list_words(board, word_list):
    board = Board(rows=board)
    boggle = Boggle(board=board, word_list=word_list)
    return boggle.list_words()
