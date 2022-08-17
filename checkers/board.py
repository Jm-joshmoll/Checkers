import pygame
from .constants import blue, red, dark, light, rows, cols, sq_size
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        self.blue_left = self.red_left = 12
        self.blue_kings = self.red_kings = 0

    @staticmethod
    def draw_squares(win):
        win.fill(dark)
        for row in range(rows):
            for col in range(row % 2, rows, 2):
                pygame.draw.rect(win, light, (row * sq_size, col * sq_size, sq_size, sq_size))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == rows - 1 or row == 0:
            piece.make_king()
            if piece.colour == red:
                self.red_kings += 1
            elif piece.colour == blue:
                self.blue_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, blue))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, red))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.colour == red:
                    self.red_left -= 1
                elif piece.colour == blue:
                    self.blue_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return blue
        elif self.blue_left <= 0:
            return red

        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        place = piece.row, piece.col

        if piece.colour == red or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.colour, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.colour, right))
        if piece.colour == blue or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, rows), 1, piece.colour, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, rows), 1, piece.colour, right))

        return moves, place

    def _traverse_left(self, start, stop, step, colour, left, skipped=[]):
        moves = {}
        last = []

        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rows)

                    moves.update(self._traverse_left(r + step, row, step, colour, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, colour, left + 1, skipped=last))
                break

            elif current.colour == colour:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, colour, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= cols:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rows)

                    moves.update(self._traverse_left(r + step, row, step, colour, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, colour, right + 1, skipped=last))
                break

            elif current.colour == colour:
                break
            else:
                last = [current]

            right += 1

        return moves
