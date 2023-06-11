"""
This module defines the Game class which represents the game of checkers. It uses the pygame library for graphics
rendering and the Board class to represent the game board. The Game class provides methods for initializing the game,
selecting and moving pieces, and updating the graphics.
"""

# Import the necessary modules, constants and the Board class
import pygame
from .constants import red, blue, green, sq_size
from .board import Board


# Define the Game class
class Game:
    # Initialises the game and sets the game window
    def __init__(self, win):
        self._init()
        self.win = win

    # Initialises the game required variables
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = red
        self.valid_moves = {}
        self.place = {}

    # Method to call the Board class method to determine if we have a winner
    def winner(self):
        return self.board.winner()

    # Method that updates the game board and displays the valid moves
    def update(self):
        self.board.draw(self.win)
        if self.selected:
            self.draw_valid_moves(self.place, self.valid_moves)
        pygame.display.update()

    # Method that is used to reset the game by calling the ._init method()
    def reset(self):
        self._init()

    # Method that is used to select the piece
    def select(self, row, col):
        # If the piece is already selected we aim to move the piece
        if self.selected:
            result = self._move(row, col)
            # If the highlighted square isn't valid for whatever reason we deselect the piece
            if not result:
                self.selected = None

        # Get the piece based on location of selection
        piece = self.board.get_piece(row, col)
        # If piece and correct colour
        if piece != 0 and piece.colour == self.turn:
            # Get valid moves and select piece
            self.selected = piece
            self.valid_moves, self.place = self.board.get_valid_moves(piece)

            return True

        return False

    # Method that moves a piece by calling the Board class's move() method and changes turn if the move is valid
    def _move(self, row, col):
        # Get the piece from Board class.get_piece method
        piece = self.board.get_piece(row, col)
        # Check to see if there is a piece, and we have a row, column and valid moves
        if self.selected and piece == 0 and (row, col) in self.valid_moves:  # LOGIC TO ENSURE VALID SELECTION
            # Move piece to new position
            self.board.move(self.selected, row, col)
            # Add list of skipped pieces
            skipped = self.valid_moves[(row, col)]
            if skipped:
                # Remove these pieces with the Board class remove method
                self.board.remove(skipped)
            # Change the turn to the next player
            self.change_turn()

        else:
            return False

        return True

    # Method that draws the valid moves on the game board
    def draw_valid_moves(self, place, moves):
        # For each position
        for _ in place:
            # Set row and column
            r, c = place
            # Get piece
            piece = self.board.get_piece(r, c)
            # Highlight selected piece
            piece.highlight(self.win)

        # For each valid move
        for move in moves:
            # Get the location of the moves available
            row, col = move
            # Draws a small green circle for the valid moves
            pygame.draw.circle(self.win, green, (col * sq_size + sq_size // 2, row * sq_size + sq_size // 2), 15)

    # Method that changes the turn and resets necessary values
    def change_turn(self):
        self.valid_moves = {}
        self.place = {}
        if self.turn == red:
            self.turn = blue
        elif self.turn == blue:
            self.turn = red
