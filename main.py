"""
This is the main file that contains the code to a checkers game that allows two players to take turns playing against
each other. The game can be run on any Python environment with Pygame installed. We utilise the constants file that
contain the necessary settings and constants to run the file. The game follows standard checkers rules and players
move their pieces diagonally across the board. The game will continue to run until a winner is declared or
the user chooses to quit.
"""

# Import the necessary modules, constants and the Game class
import pygame
from checkers.constants import height, width, sq_size, red, FPS
from checkers.game import Game

# TO DO
# force take (all options) -> modify code so that a moves list of all pieces are created instead of just the selected
# piece but still highlights the selected pieces moves
# Highlight the pieces that are forced to move because they can take

# settings screen
# home screen
# game over screen
# bug double jump when king

# We initialise our window with the correct settings
window = pygame.display.set_mode((height, width))
pygame.display.set_caption('Checkers')

# Function that will get the row and column based on mouse location
def get_row_col_from_mouse(pos):
    # Get x,y coordinates of the mouse
    x, y = pos
    # Determine row and column mouse is located based on some math logic
    row = y // sq_size
    col = x // sq_size
    # Return these values
    return row, col

# Main function of code
def main():
    # Initialise run variable
    run = True
    # Initialise clock using the pygame function
    clock = pygame.time.Clock()
    # Create an instance of the Game class
    game = Game(window)

    # Main game loop
    while run:
        # Ticks based on the given FPS
        clock.tick(FPS)

        # Check to make sure there is a winner
        if game.winner() is not None:
            # Output winner
            if game.winner() == red:
                print("Red is the winner!")
            else:
                print("Blue is the winner!")

        # For each event
        for event in pygame.event.get():
            # Check the necessary event types
            if event.type == pygame.QUIT:
                # Stops the game loop from running
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Gets the location of mouse on click
                row, col = get_row_col_from_mouse(pygame.mouse.get_pos())
                # Selects the location of the click
                game.select(row, col)

        # Update the game display / screen
        game.update()

    # Exit the program
    pygame.quit()

# Runs the main body of code
main()
