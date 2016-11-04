"""
Author: Rafeh Qazi.
Modified: November 2016.
Program: Chess.
"""
import pprint
import random

pp = pprint.PrettyPrinter()
BOARD = [['{}{}'.format(file_, rank) for file_ in 'abcdefgh'] for rank in range(1, 9)]
square_to_indices_map = {key: (row_index, col_index)
                         for row_index, row in enumerate(BOARD) for col_index, key in enumerate(row)}


class Piece:
    occupied_squares = {}
    captured_pieces = []
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
        self.square = square
        self.color = color

        self.value = self.PIECE_VALUES[self.name]
        self.id = '{}{}{}{}{}'.format(self.name[0], self.color, self.square, self.__class__.count, Piece.count)
        self.file, self.rank = square
        self.occupied_squares[self.square] = self

        Piece.pieces.append(self)
        Piece.count += 1

    def valid_moves(self):
        raise NotImplementedError

    def move(self, square):
        allowed_moves, capture_moves = self.valid_moves()
        if square in allowed_moves:
            previous_square = self.square
            self.square = square

            # update the piece's key in occupied_squares.
            self.occupied_squares[self.square] = self.occupied_squares.pop(previous_square)

            self.occupied_squares[self.square] = self

        elif square in capture_moves:
            previous_square = self.square
            self.square = square

            # update the piece's key in occupied_squares.
            self.occupied_squares[self.square] = self.occupied_squares.pop(previous_square)

            self.occupied_squares[self.square] = self


        else:
            raise AssertionError(
                "Not a valid move. Your {} is currently at {} but it is trying to get to {} {}.".format(
                    self.name, self.square, square)
            )

    def __repr__(self):
        return '\'{}("{}", "{}")\''.format(self.name.title(), self.color, self.square)


class Knight(Piece):
    count = 0

    def __init__(self, square, color='w'):
        super(Knight, self).__init__('knight', square, color)
        Knight.count += 1

    def valid_moves(self):
        row, col = square_to_indices_map[self.square]
        try:
            one = BOARD[row + 2][col + 1]
        except IndexError:
            one = None

        try:
            assert col - 1 >= 0
            two = BOARD[row + 2][col - 1]
        except (IndexError, AssertionError):
            two = None

        try:
            three = BOARD[row + 1][col + 2]
        except IndexError:
            three = None

        try:
            assert col - 2 >= 0
            four = BOARD[row + 1][col - 2]
        except (IndexError, AssertionError):
            four = None

        try:
            assert row - 1 >= 0 and col - 2 >= 0
            five = BOARD[row - 1][col - 2]
        except (IndexError, AssertionError):
            five = None

        try:
            assert row - 1 >= 0
            six = BOARD[row - 1][col + 2]
        except (IndexError, AssertionError):
            six = None

        try:
            assert row - 2 >= 0 and col - 1 >= 0
            seven = BOARD[row - 2][col - 1]
        except (IndexError, AssertionError):
            seven = None

        try:
            assert row - 2 >= 0
            eight = BOARD[row - 2][col + 1]
        except (IndexError, AssertionError):
            eight = None

        knight_moves = {one, two, three, four, five, six, seven, eight}
        # allowed_on_board_moves = {move for move in knight_moves if move and move not in self.occupied_squares}
        allowed = set()
        capture_moves = set()

        for move in knight_moves:
            if move:
                if move not in self.occupied_squares:
                    allowed.add(move)
                else:
                    if not self.occupied_squares[move].color == self.color:
                        capture_moves.add(move)

        return allowed, capture_moves


def simulate_moves(piece):
    moves = []
    play_board = [['-' for _ in range(1, 9)] for _ in range(1, 9)]
    for _ in range(1000):
        allowed_moves, capture_moves = piece.valid_moves()
        piece.move(random.choice(list(allowed_moves)))
        print(piece.square)
        moves.append(piece.square)

    print(moves)
    for i, move in enumerate(moves):
        row, col = square_to_indices_map[move]
        play_board[row][col] = '{}{}'.format(i + 1, piece.name[:2])

    pprint.pprint(play_board[::-1])


# simulate_moves(Knight('b1'))
# n2 = Knight('b1')
# n3 = Knight('c3')
# # print(n2.valid_moves())
# # print(n3.valid_moves())
# assert 'b1' not in n3.valid_moves()
# assert 'c3' not in n2.valid_moves()
# print(Piece.occupied_squares)
# n2.move('a3')
# print(Piece.occupied_squares)
# # print(n2)
# # Knight('b1')
# pprint.pprint(BOARD)
# n2 = Knight('b1')
# print(n2.square)
# print(BOARD[7][7])
# print(square_to_indices_map)
n1 = Knight('g1', 'b')
n2 = Knight('f3')
print(Piece.occupied_squares)
print(n1.valid_moves())
