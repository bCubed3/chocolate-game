import sys
import ctypes
import math
import copy
import numpy as np
from time import sleep
import time
from numba import jit, cuda
import pygame


user32 = ctypes.windll.user32
pygame.init()
size = width, height = round(user32.GetSystemMetrics(0) / 1.3), round(user32.GetSystemMetrics(1) / 1.3)
screen = pygame.display.set_mode(size)  # this is the surface
won = 0

# builds a numpy array of 1 values for the game board
game_size = (5, 6)
tiles = np.zeros(game_size)
tiles[:, :] = 1


# sets x,y and all tiles up and to the right to 0
def click_tiles(x, y, game_state):
    game_state = game_state.copy()
    if game_state[x][y]:
        game_state[0:x + 1, 0:y + 1] = 0
    return game_state


print(tiles)
turn = 0
checks = 0


def minimax(game_state, n=0):
    global checks
    # base case : returns -1 to signify loss of the game ; returns (-1, -1) as the move to end the game if it's the
    # first iteration of the function
    if game_state[-1][-1] == 0:
        if n == 0:
            return -1, -1
        else:
            return 1
    # recursive part
    else:
        score = -2
        # iterate over all the cells
        for r_index, row in reversed(list(enumerate(game_state))):
            for c_index, cell in reversed(list(enumerate(row))):
                if cell == 1:
                    checks += 1
                    score_t = -minimax(click_tiles(r_index, c_index, game_state), n + 1)
                    if score_t >= score:
                        score = score_t
                    if n == 0 and score == 1:
                        return r_index, c_index
                    if score == 1:
                        break
        return score


t = time.time()
m = minimax(tiles)
print(time.time() - t, "new", m)
print("checks :", checks)
tiles = click_tiles(m[0], m[1], tiles)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mx, my = pygame.mouse.get_pos()
            mx = math.floor((mx - 100) / 110)
            my = math.floor((my - 100) / 110)
            if mx < game_size[0] and my < game_size[1]:
                tiles = click_tiles(mx, my, tiles)
                move = minimax(tiles)
                print(move)
                tiles = click_tiles(move[0], move[1], tiles)

    screen.fill((255, 255, 255))
    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            if tiles[i][j] == 1:
                if (i + 1, j + 1) == game_size:
                    c = (0, 255, 0)
                else:
                    c = (255, 0, 0)
            else:
                if (i + 1, j + 1) == game_size:
                    c = (0, 127, 0)
                else:
                    c = (127, 0, 0)
            pygame.draw.rect(screen, c, pygame.Rect(i*110 + 100, j * 110 + 100, 100, 100))
    pygame.draw.circle(screen, (0, 0, ((turn + 1) % 2) * 200 + 55), (width - 100, round(height / 2)), 45)
    pygame.display.flip()
