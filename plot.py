import matplotlib.pyplot as plt


def plotGenerations(generationStatuses):
    x = ['min', 'avg', 'max']
    fig = plt.figure()
    fig.suptitle('Genetic Algorithm', fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_ylabel('Fitness Function Value')
    for i in range(len(generationStatuses)):
        if i == 0:
            ax.plot(x, generationStatuses[i], label="Initial Generation")
        elif i == len(generationStatuses)-1:
            ax.plot(x, generationStatuses[i], label="Generation#" + str(len(generationStatuses)-1))
        # else:
        #     ax.plot(x, generationStatuses[i])
    plt.legend(loc='lower right')
    plt.show()
