import pygame
from .constants import glow, blue, red, sq_size, bCrown, rCrown, bLight, rLight

class Piece:
    padding = 12
    padding2 = 25
    padding3 = 30
    outline = 5

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False

        if self.colour == blue:
            self.direction = -1
            self.light = bLight
        elif self.colour == red:
            self.direction = 1
            self.light = rLight
        else:
            print("error")

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = sq_size * self.col + sq_size // 2
        self.y = sq_size * self.row + sq_size // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = sq_size // 2 - self.padding
        radius2 = sq_size // 2 - self.padding2
        radius3 = sq_size // 2 - self.padding3
        pygame.draw.circle(win, self.light, (self.x, self.y), radius)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius2)
        pygame.draw.circle(win, self.light, (self.x, self.y), radius3)
        if self.king:
            if self.colour == blue:
                win.blit(bCrown, (self.x - bCrown.get_width()//2, self.y - bCrown.get_height()//2))
            elif self.colour == red:
                win.blit(rCrown, (self.x - rCrown.get_width() // 2, self.y - rCrown.get_height()//2))

    def highlight(self, win):
        h_padding = 10
        h_radius = sq_size // 2 - h_padding
        pygame.draw.circle(win, glow, (self.x, self.y), h_radius)
        self.draw(win)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.colour)
