import pygame
import sys
import ctypes
import math

user32 = ctypes.windll.user32
pygame.init()
size = width, height = round(user32.GetSystemMetrics(0) / 1.3), round(user32.GetSystemMetrics(1) / 1.3)
screen = pygame.display.set_mode(size)  # this is the surface
game = True
won = 0

game_size = (7, 4)
tiles = []
for i in range(game_size[0]):
    tiles.append([])
    for j in range(game_size[1]):
        tiles[i].append(1)

print(tiles)
turn = 0

# player 1
# player 2

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mx, my = pygame.mouse.get_pos()
            mx = math.floor((mx - 100) / 110)
            my = math.floor((my - 100) / 110)
            if mx < game_size[0] and my < game_size[1]:
                if tiles[mx][my] == 1:
                    turn += 1
                    for i in range(mx + 1):
                        for j in range(my + 1):
                            tiles[i][j] = 0
                            if (i + 1, j + 1) == game_size:
                                game = False
                                won = turn % 2 + 1
                                print("Player", won, "won the game !")

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
    pygame.draw.circle(screen, (0, 0, ((turn + 1) % 2) * 200 + 55), (width - 200, round(height / 2)), 90)
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 0))
    pygame.display.flip()