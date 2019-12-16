from random import randint
from copy import deepcopy
from math import inf


class GeneticAlgorithm:

    def __init__(self, numberOfGenerations, populationSize,
                 tournumentSize, mutationRate):
        self.numberOfGenerations = numberOfGenerations
        self.populationSize = populationSize
        self.tournumentSize = tournumentSize
        self.mutationRate = mutationRate
        self.numberOfProvinces = 31
        self.numberOfEdges = 73

    def makeInitialPopulation(self):
        chromosomes = []
        for i in range(self.populationSize):
            chromosome = [randint(0, 3) for i in range(self.numberOfProvinces)]
            chromosomes.append(chromosome)
        return chromosomes

    def calculateFitnessFunction(self, chromosome):
        sum = 0
        for i in range(len(chromosome)):
            for j in range(len(chromosome)):
                sum += int(chromosome[i] != chromosome[j])
        return sum / self.numberOfEdges

    def runTournument(self, chromosomes):
        parents = []
        chromosomesCopy = deepcopy(chromosomes)
        for j in range(int(self.populationSize / self.tournumentSize)):
            selecteds = []
            for i in range(self.tournumentSize):
                if len(chromosomesCopy) - 1 > 0:
                    selecteds.append(chromosomesCopy.pop(randint(0, len(chromosomesCopy) - 1)))
            max = -1
            best = -1
            for i in range(0, len(selecteds)-1):
                fitnessValue = self.calculateFitnessFunction(selecteds[i])
                if fitnessValue > max:
                    max = fitnessValue
                    best = i
            parents.append(selecteds[best])
        return parents

    def crossOver(self, parents):
        childs = []
        while len(parents) != 0:
            if len(parents)-1 > 0:
                father = parents.pop(randint(0, len(parents) - 1))  # :D
                mother = parents.pop(randint(0, len(parents) - 1))
                fatherGenes = father[0:15]
                motherGenes = mother[15:31]
                child = fatherGenes + motherGenes
                childs.append(child)
            else:
                break
        return childs

    def mutate(self, childs):
        mutatedGenomes = int(self.populationSize * self.numberOfProvinces * self.mutationRate)
        while mutatedGenomes != 0:
            childs[randint(0, len(childs) - 1)][randint(0, self.numberOfProvinces - 1)] = randint(0, 3)
            mutatedGenomes -= 1
        return childs

    def printGeneration(self, generation, i):
        print('Generation#', i)
        print(self.calculateFitnessForWholeGeneration(generation)[1])
        print()

    def calculateFitnessForWholeGeneration(self, generation):
        min = inf
        max = -inf
        sum = 0
        for chromosome in generation:
            chromosomeValue = self.calculateFitnessFunction(chromosome)
            if chromosomeValue > max:
                max = chromosomeValue
            if chromosomeValue < min:
                min = chromosomeValue
            sum += chromosomeValue
        avg = sum / len(generation)
        return min, avg, max

    def geneticAlgorithm(self, numberOfGenerations):
        initialGeneration = self.makeInitialPopulation()
        for i in range(numberOfGenerations):
            self.printGeneration(initialGeneration, i)
            newGeneration = self.mutate(self.crossOver(self.runTournument(initialGeneration)))
            for i in range(len(newGeneration)):
                initialGeneration.pop(randint(0, len(initialGeneration)-1))
            initialGeneration = newGeneration + initialGeneration

    def run(self):
        self.geneticAlgorithm(self.numberOfGenerations)
