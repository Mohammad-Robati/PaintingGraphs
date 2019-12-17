import matplotlib.pyplot as plt


def plotGenerations(initialGeneration, lastGeneration, numberOfGenerations):
    x = ['min', 'avg', 'max']
    fig = plt.figure()
    fig.suptitle('Genetic Algorithm', fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_ylabel('Fitness Function Value')
    ax.plot(x, initialGeneration, label='Initial Generation')
    ax.plot(x, lastGeneration, label='Generation #'+str(numberOfGenerations))
    plt.legend(loc='lower right')
    plt.show()
