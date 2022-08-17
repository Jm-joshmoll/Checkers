import pygame

height, width = 1000, 1000
rows, cols = 8, 8
sq_size = width // cols

# rgb

white = (255, 255, 255)
black = (0, 0, 0)
blue = (35, 101, 129)
bLight = (59, 168, 215)
red = (105, 27, 27)
rLight = (248, 49, 87)
green = (120, 217, 113)
glow = (197, 207, 216)

# Dark coloured squares rgb values
dark = (60, 60, 58)
# Light coloured squares rgb values
light = (237, 237, 237)
grey = (128, 128, 128)
# Background rgb values
background = (49, 46, 43)

rCrown = pygame.image.load('images/rCrown.png')
bCrown = pygame.image.load('images/bCrown.png')
