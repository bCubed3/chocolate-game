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
game_size = (3, 3)
tiles = np.zeros(game_size)
tiles[:, :] = 1
winning_states = np.array([[0, 0, 0],
                           [0, 0, 0],
                           [0, 1, 1]])


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
    # variable used to count how many iterations the function does
    global checks
    global winning_states
    # base case : returns -1 to signify loss of the game ; returns (-1, -1) as the move to end the game if it's the
    # first iteration of the function
    if game_state[-1][-1] == 0:
        if n == 0:
            return -1, -1
        else:
            return -1
    # recursive part
    else:
        score = -2
        m_move = -1, -1
        # iterate over all the cells
        for r_index, row in enumerate(game_state):
            for c_index, cell in enumerate(row):
                checks = checks + 1
                if checks % 1000000 == 0:
                    print(checks)
                # checks if the cell is on ; if so, it it simulates the game as if it were clicked
                if cell == 1:
                    #print(game_state)
                    t_game_state = game_state.copy()
                    t_game_state[0:r_index + 1, 0:c_index + 1] = 0
                    #if t_game_state in winning_states:
                    #    t_score = -1
                    #    print(t_game_state)
                    #else:
                    # this is negative because the player has changed
                    # what would be a 1 (signifying a win) for the previous player
                    # would now be a -1 (a loss) for this player)
                    t_score = int(-minimax(t_game_state, n + 1))
                    #if t_score == 1:
                    #    print("yes")
                    #    winning_states = np.concatenate([winning_states, np.array([t_game_state])])
                    #    print(winning_states)
                    if t_score > score:
                        score = t_score
                        m_move = r_index, c_index
        if n == 0:
            return m_move
        else:
            return score


tiles = np.zeros(game_size)
tiles[:, :] = 1
t = time.time()
m = minimax(tiles)
print(time.time() - t)
print(m)
print(winning_states)
