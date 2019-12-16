from geneticAlgorithm import GeneticAlgorithm

# numberOfGenerations = int(input('Number Of Generations: '))
# populationSize = int(input('Population Size: '))
# tournumentSize = int(input('Tournument Size: '))
# mutationRate = float(input('Mutation Rate: '))
#
# GeneticAlgorithm(numberOfGenerations, populationSize,
#                  tournumentSize, mutationRate).run()

GeneticAlgorithm(50, 100, 5, 0.02).run()
