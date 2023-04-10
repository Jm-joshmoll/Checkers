import pygame
from checkers.constants import height, width, sq_size, red
# from checkers.board import Board
from checkers.game import Game

# force take
# settings
# home screen
# game over screen

FPS = 60

window = pygame.display.set_mode((height, width))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // sq_size
    col = x // sq_size
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(window)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            if game.winner() == red:
                print("Red is the winner!")
            else:
                print("Blue is the winner!")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_row_col_from_mouse(pygame.mouse.get_pos())
                game.select(row, col)

        game.update()

    pygame.quit()

main()
