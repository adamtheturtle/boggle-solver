# TODO generate api docs

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
    """

    def __init__(self, word):
        """docstring for __init__"""
        self.word = word.upper()
        self.tile_list = self._to_tiles()
        self.num_tiles = len(self.tile_list)
        self.is_valid = len(self.word) > 2 and self.num_tiles

    def _to_tiles(self):
        """
        Return the list of tile contents necessary to form a word.

        A list of the letters in a string, except 'QU' is a tile and Q is not.

        word: A string.
        return: List of strings.
        """
        valid_tiles = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'QU', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        ]

        word = self.word
        tiles = []
        while len(word):
            valid_tile_added = False
            for tile in valid_tiles:
                if word.startswith(tile):
                    word = word[len(tile):]
                    tiles.append(tile)
                    valid_tile_added = True
                    continue
            if not valid_tile_added:
                return []
        return tiles

    def num_occurences(self, tile):
        return self.tile_list.count(tile)


class Board(object):

    # TODO Also include a generator

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

        for tile in word.tile_list:
            positions = self._occurences(tile)
            new_routes = []

            for route in routes:
                last_position = route[len(route) - 1]
                for position in positions:
                    if position.touching(last_position) and position not in route:
                        new_route = route[:]
                        new_route.append(position)
                        includes_whole_word = len(new_route) == word.num_tiles
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


class Game(object):
    """
    TODO
    """

    # TODO change from word_list to word file
    # TODO create a UI
    # TODO create a "fromString" thing
    def __init__(self, board, word_list):
        """
        TODO
        """
        self.board = board
        self.word_list = word_list

    def _matching_words(self):
        """
        Return all words from a given dictionary which are in a board.

        word_list: A set of valid words.
        board: A list of lists of tiles. Each list in the list of lists represents
            a row of a Boggle board.

        returns: A set of strings.
        """
        found = set([])
        for word in self.word_list:
            word = Word(word=word)
            if word.is_valid and self.board.is_available_route(word=word):
                found.add(word)
        return found

    def list_words(self):
        matching_words = self._matching_words()
        return set([word.word for word in matching_words])



def list_words(board, word_list):
    board = Board(rows=board)
    game = Game(board=board, word_list=word_list)
    return game.list_words()