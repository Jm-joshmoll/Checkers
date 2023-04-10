import pygame
from .constants import red, blue, green, glow, sq_size
from .board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = red
        self.valid_moves = {}
        self.place = {}

    def winner(self):
        return self.board.winner()

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.place, self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.valid_moves = {}
                self.place = {}
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.colour == self.turn:
            self.selected = piece
            self.valid_moves, self.place = self.board.get_valid_moves(piece)
            return True

        return False

    def deselect(self, row, col):
        self.selected = None

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.move(self.selected, row, col)
                self.board.remove(skipped)
            else:
                self.board.move(self.selected, row, col)
            self.change_turn()

        else:
            return False

        return True

    def draw_valid_moves(self, place, moves):
        for _ in place:
            r, c = place
            piece = self.board.get_piece(r, c)
            piece.highlight(self.win)

        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, green, (col * sq_size + sq_size // 2, row * sq_size + sq_size // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        self.place = {}
        if self.turn == red:
            self.turn = blue
        elif self.turn == blue:
            self.turn = red
