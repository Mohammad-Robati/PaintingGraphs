from random import randint, uniform
from copy import deepcopy
from math import log2


class SimulatedAnnealing:

    def __init__(self, initalTemp, probabilityFunction, numberOfProvinces, numberOfEdges, graph):
        self.initialTemp = initalTemp
        self.probabiltyFunction = probabilityFunction
        self.numberOfProvinces = numberOfProvinces
        self.numberOfEdges = numberOfEdges
        self.graph = graph

    def initializeState(self):
        return [randint(0, 3) for i in range(self.numberOfProvinces)]

    def getRandomNextState(self, state):
        newState = deepcopy(state)
        r = randint(0, len(state) - 1)
        choices = list({0, 1, 2, 3} - {state[r]})
        newState[r] = choices[randint(0, 2)]
        return newState

    def calculateValue(self, state):
        sum = 0
        for node in self.graph:
            for neighbour in self.graph[node]:
                sum += int(state[int(node)] != state[int(neighbour)])
        return sum / self.numberOfEdges

    def calculateProbabilty(self, type, t):
        if type == 1:
            return self.initialTemp * pow(0.85, t)
        elif type == 2:
            return self.initialTemp / (1 + (1.6) * log2(1 + t))
        elif type == 3:
            return self.initialTemp / 1 + 1.6 * t
        elif type == 4:
            return self.initialTemp / 1 + 1.6 * pow(t, 2)

    def simulatedAnnealingAlgorithm(self):
        state = self.initializeState()
        print('Initial Value:  ', self.calculateValue(state))
        print(state)
        print()
        for t in range(1000):
            next = self.getRandomNextState(state)
            valueDiff = self.calculateValue(next) - self.calculateValue(state)
            if valueDiff > 0:
                state = next
            else:
                if uniform(0, 1) <= self.calculateProbabilty(self.probabiltyFunction, t):
                    state = next
        print('Final Value:    ', self.calculateValue(state))
        print(state)

    def run(self):
        self.simulatedAnnealingAlgorithm()
