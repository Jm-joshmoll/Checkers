"""
This module defines the Button class for creating clickable buttons in graphical interfaces.
"""
# Import the necessary modules
import pygame
from checkers.constants import white, black

# Define the Button class
class Button:
    # Initialises a new button instance
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.rect = pygame.Rect(position, (200, 50))

    # Draws the button on a pygame surface
    def draw(self, surface):
        # Draws the button
        pygame.draw.rect(surface, white, self.rect)
        pygame.draw.rect(surface, black, self.rect, 2)
        text_surface = pygame.font.Font(None, 36).render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    # Check if button is clicked, if given position is within the button's clickable area
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
