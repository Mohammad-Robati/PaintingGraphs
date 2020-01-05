from geneticAlgorithm import GeneticAlgorithm
from simulatedAnnealing import SimulatedAnnealing

# Iran Map
# numberOfProvinces = 31
# numberOfEdges = 72
# graph = {'0': ['1', '3', '4'], '1': ['2', '4'], '2': ['4', '5'], '3': ['6', '7', '4'], '4': ['5', '8', '7'], '5': ['8', '9'], '6': ['7', '10', '11'], '7': ['8', '11', '12'], '8': ['12', '15'], '9': ['15', '14', '20', '21'], '10': ['11', '16'], '11': ['12', '19', '17', '16'], '12': ['13', '14', '15', '19'], '13': ['14', '19', '20'], '14': ['15', '20'], '16': ['17', '18', '28'], '17': ['18', '19'], '18': ['26', '28', '19'], '19': ['20', '25', '26'], '20': ['21', '22', '23', '24', '25'], '21': ['22'], '22': ['23'], '23': ['24'], '24': ['25', '27'], '25': ['26', '27'], '26': ['27', '28', '29'], '27': ['29', '30'], '28': ['29'], '29': ['30']}

numberOfProvinces = int(input('Enter Number Of Provinces: '))
numberOfEdges = int(input('Enter Number Of Edges: '))
print('Enter Neighbours: (ex. 0 1)')
graph = {}
for i in range(numberOfEdges):
    neighbours = input().split()
    if neighbours[0] in graph:
        graph[neighbours[0]].append(neighbours[1])
    else:
        graph[neighbours[0]] = [neighbours[1]]

algorithm = int(input('Which Algorithm You Want To Use:\n1.Genetics Algorithm\n2.Simulated Annealing:'))

if algorithm == 1:
    numberOfGenerations = int(input('Number Of Generations: '))
    populationSize = int(input('Population Size: '))
    tournumentSize = int(input('Tournument Size: '))
    if tournumentSize>populationSize/2:
        print('Tournument Size > Population Size / 2 !!!')
        print('No Parents can be produced!')
        exit(0)
    mutationRate = float(input('Mutation Rate: '))
    GeneticAlgorithm(numberOfGenerations, populationSize,
                     tournumentSize, mutationRate, numberOfProvinces, numberOfEdges, graph).run()
elif algorithm == 2:
    # initialTemp = int(input('InitialTemp: '))
    # probabiltyFunction = int(input('Probability Function: '))
    SimulatedAnnealing(1.8, 1, numberOfProvinces, numberOfEdges, graph).run()



