import sys
import ctypes
import math
import copy
import numpy as np
from time import sleep
import time
from numba import jit, cuda

won = 0

# builds a numpy array of 1 values for the game board
game_size = (4, 4)
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


def minimax(game_state, n=0, alpha=-10, beta=10):
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
        if n % 2 == 0:  # maximizing player
            score = -2
            # iterate over all the cells
            for r_index, row in enumerate(game_state):
                for c_index, cell in enumerate(row):
                    if cell == 1:
                        checks += 1
                        score = max(score, -minimax(click_tiles(r_index, c_index, game_state), n + 1))
                        alpha = max(score, alpha)
                        if beta <= alpha:
                            break

        else:  # minimizing player
            score = 2
            # iterate over all the cells
            for r_index, row in enumerate(game_state):
                for c_index, cell in enumerate(row):
                    if cell == 1:
                        score = min(score, -minimax(click_tiles(r_index, c_index, game_state), n + 1))
                        beta = min(score, beta)
                        if beta <= alpha:
                            break
        return score


tiles = np.zeros(game_size)
tiles[:, :] = 1
t = time.time()
m = minimax(tiles, 0)
print(time.time() - t)
print(m)