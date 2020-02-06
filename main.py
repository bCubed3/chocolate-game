import pygame
import sys
import ctypes
import math
import copy
from time import sleep

user32 = ctypes.windll.user32
pygame.init()
size = width, height = round(user32.GetSystemMetrics(0) / 1.3), round(user32.GetSystemMetrics(1) / 1.3)
screen = pygame.display.set_mode(size)  # this is the surface
won = 0

game_size = (4, 2)
tiles = []
for i in range(game_size[0]):
    tiles.append([])
    for j in range(game_size[1]):
        tiles[i].append(True)


def click_tiles(x, y, game_state):
    game_state = copy.deepcopy(game_state)
    if game_state[x][y]:
        for i in range(x + 1):
            for j in range(y + 1):
                game_state[i][j] = False
    return game_state


print(tiles)
turn = 0

def minimax(game_state, n=0):
    if not game_state[-1][-1]:
        if n == 0:
            return -1, -1
        else:
            return 1
    else:
        score = -2
        move = -1, -1
        for row in range(game_size[0]):
            for column in range(game_size[1]):
                if game_state[row][column]:
                    t_game_state = copy.deepcopy(game_state)
                    t_game_state = click_tiles(row, column, t_game_state)
                    t_score = -minimax(t_game_state, n + 1)
                    if t_score > score:
                        score = t_score
                        move = row, column
        if n == 0:
            return move
        else:
            return score


t = copy.deepcopy(tiles)
move = minimax(tiles)
tiles = click_tiles(move[0], move[1], tiles)

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

while False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 0))
    pygame.display.flip()