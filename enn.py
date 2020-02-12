import numpy as np
import random as r
from copy import deepcopy


class EvoNeuralNetwork:
    def __init__(self, sizes, child_weights=0):
        self.sizes = sizes
        self.weights = []
        self.biases = []
        if child_weights == 0:
            for i in range(len(sizes) - 1):
                self.weights.append(np.random.rand(sizes[i], sizes[i + 1]))
                self.weights[i] = self.weights[i] - 0.5
                self.weights[i] = self.weights[i] * 2
                self.biases.append(np.random.rand(sizes[i], sizes[i + 1]))

        else:
            pass

    def forward_propagate(self, inp_arr):
        if len(inp_arr) == self.sizes[0]:
            t_layer = deepcopy(inp_arr)



nn = EvoNeuralNetwork([3, 2, 4])
print(nn.weights)

