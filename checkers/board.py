"""
This module defines the Board class which represents the game board itself. It contains methods for creating the board,
drawing the squares and pieces on the board, moving a piece, getting a piece at a specific location, removing pieces
from the board, and determining the winner of the game. The class also stores information about the current state of the
board, such as the number of pieces and kings for each player. This module relies on the constants.py module for colour
and size constants, and the piece.py module for the Piece class.
"""

# Import necessary packages, constants from constants.py file and Piece class
import pygame
from .constants import blue, red, dark, light, rows, cols, sq_size
from .piece import Piece

# Define the board class
class Board:
    # Initialises the board, and a few variables, an empty list representing the board, how many coloured pieces are
    # left and how many kings have been created
    def __init__(self):
        self.board = []
        self.blue_left = self.red_left = 12
        self.blue_kings = self.red_kings = 0
        # We then call create board
        self.create_board()

    # Method that will draw the squares in alternate colours
    @staticmethod
    def draw_squares(win):
        # Colour all squares dark
        win.fill(dark)
        # We then loop through the code to colour every other square light
        for row in range(rows):
            for col in range(row % 2, rows, 2):
                pygame.draw.rect(win, light, (row * sq_size, col * sq_size, sq_size, sq_size))

    # Method that creates the initial setup of the board with each piece in their respective starting position
    def create_board(self):
        # For each row
        for row in range(rows):
            # We initialise the row with an empty list
            self.board.append([])
            # For each column within the row
            for col in range(cols):
                # We check if the square is a dark square based on the position of the square on the board
                if col % 2 == ((row + 1) % 2):
                    # If the square is within the first 3 rows we add a blue piece
                    if row < 3:
                        self.board[row].append(Piece(row, col, blue))
                    # Else if the row is above 4 (in the final 3 rows) we add a red piece
                    elif row > 4:
                        self.board[row].append(Piece(row, col, red))
                    # Otherwise we add nothing
                    else:
                        self.board[row].append(0)
                # If it is a light square we add nothing
                else:
                    self.board[row].append(0)

    # Method that updates the games board after a piece has been moved
    def move(self, piece, row, col):
        # Swaps the current position with the new position on the board
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        # Uses the piece move method to update the piece's attributes
        piece.move(row, col)

        # Logic to determine whether to promote a piece to a king and increment the number of that colour's king pieces
        if row == rows - 1 or row == 0:
            piece.make_king()
            if piece.colour == red:
                self.red_kings += 1
            elif piece.colour == blue:
                self.blue_kings += 1

    # Method that returns the piece object at a specified position on the game board.
    def get_piece(self, row, col):
        return self.board[row][col]

    # Method that draws the game board and its pieces to the pygame window
    def draw(self, win):
        # Draws the squares on the board
        self.draw_squares(win)
        # Loops through each row and each column
        for row in range(rows):
            for col in range(cols):
                # Define variable piece, will return nothing where there's no piece
                piece = self.board[row][col]
                # Draws the piece if a square contains one
                if piece:
                    piece.draw(win)

    # Method that removes a specified piece from the board and updates how many pieces are left after
    def remove(self, pieces):
        # for each piece that has been removed
        for piece in pieces:
            # Set the value of the removed piece to 0
            self.board[piece.row][piece.col] = 0
            # If a piece has been removed
            if piece != 0:
                # Remove one from the respective piece colour
                if piece.colour == red:
                    self.red_left -= 1
                elif piece.colour == blue:
                    self.blue_left -= 1

    # Method that checks if there is a winner based on the number of pieces left for each colour
    def winner(self):
        if self.red_left <= 0:
            return blue
        elif self.blue_left <= 0:
            return red

        return None

    # Method that returns a dictionary of valid moves that a piece can make
    def get_valid_moves(self, piece):
        # Initialise an empty dictionary
        moves = {}
        # Define what left and right mean
        left = piece.col - 1
        right = piece.col + 1
        # Define the row a piece is on, and its "place"
        row = piece.row
        place = piece.row, piece.col

        # We define the possibilities of valid moves available to the piece based on left and right movement in the
        # correct direction depending on which colour it is but as king pieces move in all directions we are not
        # worried about the colour that a king is. We call the _traverse_left / _traverse_right methods to search the
        # extent of valid moves
        if piece.colour == red or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.colour, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.colour, right))
        if piece.colour == blue or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, rows), 1, piece.colour, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, rows), 1, piece.colour, right))

        return moves, place

    # Method that takes several arguments amd returns a dictionary of valid moves that a piece can make to its left
    def _traverse_left(self, start, stop, step, colour, left, skipped=None):
        # Initialise a few lists and dictionaries used
        if skipped is None:
            skipped = []
        moves = {}
        last = []

        # Iterate between the starting row and the end row by the row step
        for r in range(start, stop, step):
            # If the left column is out of bounds i.e. we are at the left edge of the board we break out of the loop
            if left < 0:
                break
            # Otherwise we look to the left
            current = self.board[r][left]
            # If the square is empty
            if current == 0:
                # If the piece has skipped over another piece, and there's no further moves we break the loop
                if skipped and not last:
                    break
                # Else if we have already skipped a piece and there are other pieces to skip we add that to list
                elif skipped:
                    moves[(r, left)] = last + skipped
                # Else we add last to move dictionary
                else:
                    moves[(r, left)] = last

                # If there was a move recursively call function
                if last:
                    # Ensures the next row is the correct row depending on direction
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rows)
                    # Calls itself to update the list with the next moves
                    moves.update(self._traverse_left(r + step, row, step, colour, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, colour, left + 1, skipped=last))
                break

            # If the current position is the same colour break out of the code
            elif current.colour == colour:
                break
            # Otherwise adds position to the list
            else:
                last = [current]

            left -= 1
        # Returns the generated move dictionary
        return moves

    # Method similar to _traverse_left except it searches to the right instead
    def _traverse_right(self, start, stop, step, colour, right, skipped=None):
        if skipped is None:
            skipped = []
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
