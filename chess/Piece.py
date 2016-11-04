"""
Chess pieces file.
"""
import pprint
import random

pp = pprint.PrettyPrinter()
BOARD = [['{}{}'.format(file_, rank) for file_ in 'abcdefgh'] for rank in range(1, 9)]
square_to_indices_map = {key: (row_index, col_index)
                         for row_index, row in enumerate(BOARD) for col_index, key in enumerate(row)}


class Piece:
    occupied_squares = {}
    pieces = []
    count = 0
    PIECE_VALUES = {
        'pawn'  : 1,
        'knight': 3,
        'bishop': 3,
        'rook'  : 5,
        'queen' : 9,
        'king'  : 10000
    }

    def __init__(self, name, square, color='w'):
        self.name = name
        self.color = color
        self.square = square
        self.value = self.PIECE_VALUES[self.name]
        self.id = '{}{}{}{}{}'.format(self.name[0], self.color, self.square, self.__class__.count, Piece.count)
        self.occupied_squares[self.id] = self.square

        Piece.pieces.append(self)
        Piece.count += 1

    def valid_moves(self):
        raise NotImplementedError

    def update_id(self):
        self.id = '{}{}{}{}{}'.format(self.name[0], self.color, self.square, self.__class__.count, Piece.count)

    def get_new_id(self):
        return '{}{}{}{}{}'.format(self.name[0], self.color, self.square, self.__class__.count, Piece.count)

    def __repr__(self):
        return '\'{}("{}", "{}")\''.format(self.name.title(), self.color, self.square)


class Knight(Piece):
    count = 0

    def __init__(self, square, color='w'):
        super(Knight, self).__init__('knight', square, color)
        Knight.count += 1
        self.file, self.rank = square[0], square[1]

    def valid_moves(self):
        row, col = square_to_indices_map[self.square]
        try:
            one = BOARD[row + 2][col + 1]
        except IndexError:
            one = None

        try:
            assert col - 1 > 0
            two = BOARD[row + 2][col - 1]
        except (IndexError, AssertionError):
            two = None

        try:
            three = BOARD[row + 1][col + 2]
        except IndexError:
            three = None

        try:
            assert col - 2 > 0
            four = BOARD[row + 1][col - 2]
        except (IndexError, AssertionError):
            four = None

        try:
            assert row - 1 > 0 and col - 2 > 0
            five = BOARD[row - 1][col - 2]
        except (IndexError, AssertionError):
            five = None

        try:
            assert row - 1 > 0
            six = BOARD[row - 1][col + 2]
        except (IndexError, AssertionError):
            six = None

        try:
            assert row - 2 > 0 and col - 1 > 0
            seven = BOARD[row - 2][col - 1]
        except (IndexError, AssertionError):
            seven = None

        try:
            assert row - 2 > 0
            eight = BOARD[row - 2][col + 1]
        except (IndexError, AssertionError):
            eight = None

        knight_moves = {one, two, three, four, five, six, seven, eight}
        allowed_on_board_moves = {move for move in knight_moves if move is not None}
        return allowed_on_board_moves

    def move(self, square):
        row, col = square_to_indices_map[square]
        if square in self.valid_moves():
            self.square = square

            # update the piece's key in occupied_squares.
            self.occupied_squares[self.get_new_id()] = self.occupied_squares.pop(self.id)

            self.update_id()
            self.occupied_squares[self.id] = self.square
        else:
            print("Not a valid move.")


n = Knight('g1')
play_board = [[0 for i in range(1, 9)] for k in range(1, 9)]
moves = []
for _ in range(20):
    print(n.valid_moves())
    n.move(random.choice(list(n.valid_moves())))
    print(n.square)
    moves.append(n.square)

print(moves)
for i, move in enumerate(moves):
    row, col = square_to_indices_map[move]
    play_board[row][col] = '{}N'.format(i+1)

pprint.pprint(play_board[::-1])
n2 = Knight('b5')
