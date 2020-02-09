import pygame
import sys
import ctypes
import math
import copy
import numpy as np
from time import sleep
import time

user32 = ctypes.windll.user32
#pygame.init()
size = width, height = round(user32.GetSystemMetrics(0) / 1.3), round(user32.GetSystemMetrics(1) / 1.3)
#screen = pygame.display.set_mode(size)  # this is the surface
won = 0

game_size = (3, 3)
tiles = np.zeros(game_size)
tiles[:, :] = 1


def click_tiles(x, y, game_state):
    game_state = copy.deepcopy(game_state)
    if game_state[x][y]:
        game_state[0:x + 1, 0:y + 1] = 0
    return game_state


print(tiles)
turn = 0
checks = 0


def minimax(game_state, n=0):
    global checks
    if game_state[-1][-1] == 0:
        if n == 0:
            return -1, -1
        else:
            return -1
    else:
        score = -2
        m_move = -1, -1
        for r_index, row in enumerate(game_state):
            for c_index, cell in enumerate(row):
                checks = checks + 1
                if checks % 1000000 == 0:
                    print(checks)
                if cell == 1:
                    t_game_state = click_tiles(r_index, c_index, game_state)
                    t_score = -minimax(t_game_state, n + 1)
                    if t_score > score:
                        score = t_score
                        m_move = r_index, c_index
        if n == 0:
            print(checks)
            return m_move
        else:
            return score


graph = []

if True:
    for g_wid in range(5):
        for g_height in range(4):
            checks = 0
            game_size = (g_wid + 1, g_height + 1)
            tiles = np.zeros(game_size)
            tiles[:, :] = 1
            t = time.time()
            m = minimax(tiles)
            print(time.time() - t)
            graph.append((game_size, m, checks))
            print(graph)

#checks = 0
#t = copy.deepcopy(tiles)
#move = minimax(tiles)
#tiles = click_tiles(move[0], move[1], tiles)

while False:
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
