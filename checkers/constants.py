"""
This module contains constants and global settings used in the game program.
"""

import pygame

# Define game settings
# Set height/width of game window and number of rows/cols in game window
FPS = 60
width, height = 1000, 1000
rows, cols = 8, 8

# Set the size of each square
sq_size = width // cols

# RGB values of different colours
white = (255, 255, 255)
black = (0, 0, 0)
blue = (35, 101, 129)
bLight = (59, 168, 215)
red = (105, 27, 27)
rLight = (248, 49, 87)
green = (120, 217, 113)
glow = (197, 207, 216)
grey = (128, 128, 128)

# Dark coloured squares RGB values
dark = (60, 60, 58)
# Light coloured squares RGB values
light = (237, 237, 237)
# Background RGB values
background = (49, 46, 43)

# Load crown images for pieces
rCrown = pygame.image.load('images/rCrown.png')
bCrown = pygame.image.load('images/bCrown.png')
