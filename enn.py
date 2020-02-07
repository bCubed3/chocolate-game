import numpy as np
import random as r
from copy import deepcopy


class EvoNeuralNetwork:
    def __init__(self, sizes, child_weights=0):
        self.sizes = sizes
        self.weights = []
        if child_weights == 0:
            for layer in range(len(sizes) - 1):
                self.weights.append([])
                for node in range(sizes[layer + 1]):
                    self.weights[layer].append([])
                    for weight in range(sizes[layer]):
                        self.weights[layer][node].append(2 * r.random() - 1)
        else:
            pass

    def forward_propagate(self, inp_arr):
        if len(inp_arr) == self.sizes[0]:
            t_layers = [deepcopy(inp_arr)]
            for w_layer in self.weights:
                for n_index, node in enumerate(w_layer):
                    t_layers.append([])
                    t_node_value = 0
                    print(t_layers)
                    for w_index, weight in enumerate(node):
                        print(w_index)
                        t_node_value = t_node_value + t_layers[-2][w_index] * weight
                    t_layers[-1].append(t_node_value)



nn = EvoNeuralNetwork([3, 3, 3])
print(nn.forward_propagate([10, 3, 4]))
print(nn.weights)
