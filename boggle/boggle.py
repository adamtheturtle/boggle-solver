# TODO support multiple languages, with different valid words sections
# TODO generate api docs
# TODO change from word_list to word file
# TODO create a UI
# TODO create a "fromString" thing, then you can have a CLI shared with other
# languages
# TODO Also include a generator, to make random games
# TODO handle case where a key in the board is not valid
# TODO main docstring with my name, description of the project etc.
# TODO try hypothesis for making a word - can it be broken?

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

    def __init__(self, string, valid_tiles):
        """
        :param str string: A word from a dictionary, valid if found on a Board.
        :param set valid_tiles: Strings, all tile contents which are valid.

        :ivar list tiles: strings, each valid contents of a tile.
        """
        string = string.upper()

        self.tiles = []
        while len(string):
            valid_tile_added = False
            for tile in valid_tiles:
                if string.startswith(tile.upper()):
                    string = string[len(tile):]
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
        self.tile_map = self._get_tile_map(rows)

    def _get_tile_map(self, rows):
        """
        Get a mapping of tiles to positions.

        :param list rows: Lists of tiles. Each tile is a string.

        return: Dictionary, each key representing a tile content.
        """
        mapping = {}
        for row_index, row in enumerate(rows):
            for column_index, tile in enumerate(row):
                # TODO get the case matching piece here
                position = Position(column=column_index, row=row_index)
                if tile in mapping:
                    mapping[tile].append(position)
                else:
                    mapping[tile] = [position]
        return mapping

    def is_available_route(self, word):
        """
        Check if there is an available route to make a word in a board.

        A route is a path of positions from first tile to next, to next... until
        the last tile. It cannot include the same tile multiple times.

        word: A string.
        tile_map: Map of tiles to positions those tiles are in.

        returns: Boolean, True iff there is a valid route.
        """
        routes = []

        for tile in word.tiles:
            if tile not in self.tile_map:
                return False

            positions = self.tile_map[tile]
            new_routes = []

            if not routes:
                routes = [[position] for position in positions]
                continue

            for route in routes:
                last_position = route[len(route) - 1]
                for position in positions:
                    if position.touching(last_position) and position not in route:
                        new_route = route[:]
                        new_route.append(position)
                        includes_whole_word = len(new_route) == len(word.tiles)
                        if includes_whole_word:
                            return True
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
        for string in self.word_list:
            word = Word(string=string, valid_tiles=self.valid_tiles)
            if len(string) > 2 and self.board.is_available_route(word=word):
                found.add(word)
        return found

    def list_words(self):
        """
        :return set: Words which are valid and can be found on the ``board``.
        """
        matching_words = self._matching_words()
        return set(["".join(word.tiles) for word in matching_words])


def list_words(board, word_list):
    board = Board(rows=board)
    boggle = Boggle(board=board, word_list=word_list)
    return boggle.list_words()
