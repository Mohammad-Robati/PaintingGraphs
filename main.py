from geneticAlgorithm import GeneticAlgorithm
from simulatedAnnealing import SimulatedAnnealing

algorithm = int(input('Which Algorithm You Want To Use:\n1.Genetics Algorithm\n2.Simulated Annealing:'))


if algorithm == 1:
    numberOfGenerations = int(input('Number Of Generations: '))
    populationSize = int(input('Population Size: '))
    tournumentSize = int(input('Tournument Size: '))
    mutationRate = float(input('Mutation Rate: '))
    GeneticAlgorithm(numberOfGenerations, populationSize,
                     tournumentSize, mutationRate).run()
elif algorithm == 2:
    # initialTemp = int(input('InitialTemp: '))
    # probabiltyFunction = int(input('Probability Function: '))
    SimulatedAnnealing(1.8, 1).run()



