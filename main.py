"""
This is the main file that contains the code to a checkers game that allows two players to take turns playing against
each other. The game can be run on any Python environment with Pygame installed. We utilise the constants file that
contain the necessary settings and constants to run the file. The game follows standard checkers rules and players
move their pieces diagonally across the board. The game will continue to run until a winner is declared or
the user chooses to quit.
"""

# Import the necessary modules, constants and the Game class
import pygame
import sys
from checkers.constants import height, width
from checkers.menus import MainMenu, SettingsMenu
from checkers.game_loop import game_loop


# TODO: game over screen

# Initialise pygame
pygame.init()

# We initialise our window with the correct settings
window = pygame.display.set_mode((height, width))
pygame.display.set_caption('Checkers')

# Main function of code
def main():
    current_menu = MainMenu(width, height)
    running = True

    # Main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting...")
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                action = current_menu.handle_events(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
                if action == "settings":
                    print("Opening Settings...")
                    current_menu = SettingsMenu(width, height)
                elif action == "menu":
                    print("Returning to menu...")
                    current_menu = MainMenu(width, height)
                elif action == "pvp":
                    game_loop()

        current_menu.draw(window)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Runs the main body of code
main()
