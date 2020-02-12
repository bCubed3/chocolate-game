import pygame
import sys
import ctypes
import math
import copy
import numpy as np
import neat
import visualize

user32 = ctypes.windll.user32
#pygame.init()
size = width, height = round(user32.GetSystemMetrics(0) / 1.3), round(user32.GetSystemMetrics(1) / 1.3)
#screen = pygame.display.set_mode(size)  # this is the surface
won = 0

# builds a numpy array of 1 values for the game board
game_size = (3, 3)
tiles = np.zeros(game_size)
tiles[:, :] = 1




# sets x,y and all tiles up and to the right to 0
def click_tiles(x, y, game_state):
    game_state = copy.deepcopy(game_state)
    if game_state[x][y]:
        game_state[0:x + 1, 0:y + 1] = 0
    return game_state


print(tiles)
turn = 0
checks = 0

def eval_genomes(genomes_p1, genomes_p2, config):
    for genome_id, genome in genomes_p1:
        genome.fitness = 4.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(xor_inputs, xor_outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0] - xo[0]) ** 2


# mostly pygame stuff
while False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mx, my = pygame.mouse.get_pos()
            mx = math.floor((mx - 100) / 110)
            my = math.floor((my - 100) / 110)
            if mx < game_size[0] and my < game_size[1]:


    screen.fill((255, 255, 255))
    # colors the tiles based on if they're on or not
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
