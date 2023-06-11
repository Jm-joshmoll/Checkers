"""
This module defines the Piece class, which represents each checkers piece on the game board.
"""

# import necessary packages and constants from constants.py file
import pygame
from .constants import glow, blue, red, sq_size, bCrown, rCrown, bLight, rLight

# Define the class
class Piece:
    # Class variables that are used for drawing the pieces
    # Each padding represents a different place to draw from
    # We start off with the padding between the sides of the square and the piece itself
    padding = 12
    # Then the padding between the circles outer edge and its "ridge" seen by the darker shade
    padding2 = 25
    # Then the inner circle after its ridge giving us a more 3d looking piece
    padding3 = 30
    # Define the midpoint of each square
    mid_point = sq_size // 2

    # Initialises a new Piece object with the given position(row/column) and its colour
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False

        # Initialise direction of movement and the lighter colour that represents the piece
        if self.colour == blue:
            self.direction = -1
            self.light_colour = bLight
        elif self.colour == red:
            self.direction = 1
            self.light_colour = rLight
        else:
            print("error")

        # Initialise the x and y coordinates
        self.x = 0
        self.y = 0
        # Set to correct x,y position
        self.calc_pos()

    # Method that calculates the pixel position of the piece on the board based on its row and column
    def calc_pos(self):
        self.x = sq_size * self.col + self.mid_point
        self.y = sq_size * self.row + self.mid_point

    # Method to change the value of the piece if it is promoted to a king
    def make_king(self):
        self.king = True

    # Method to draw the piece on the board
    def draw(self, win):
        # Find the radius of each circle based on the padding values
        radius = self.mid_point - self.padding
        radius2 = self.mid_point - self.padding2
        radius3 = self.mid_point - self.padding3
        # Draws each circle that makes up the overall checker piece
        pygame.draw.circle(win, self.light_colour, (self.x, self.y), radius)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius2)
        pygame.draw.circle(win, self.light_colour, (self.x, self.y), radius3)
        # If the piece is a king will draw the crown on top of the piece
        if self.king:
            if self.colour == blue:
                crown_rect = bCrown.get_rect(center=(self.x, self.y))
                win.blit(bCrown, crown_rect)
            elif self.colour == red:
                crown_rect = rCrown.get_rect(center=(self.x, self.y))
                win.blit(rCrown, crown_rect)

    # Method that will highlight the piece if it is selected
    def highlight(self, win):
        # Padding/radius for the glow colour around the piece
        h_padding = 10
        h_radius = self.mid_point - h_padding
        # Draws the new glow circle
        pygame.draw.circle(win, glow, (self.x, self.y), h_radius)
        self.draw(win)

    # Method that updates the position of the piece on the board based on its new row and col values
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    # Method that returns a string representation of the colour of the piece
    def __repr__(self):
        return str(self.colour)
