import time
import matplotlib.pyplot as plt
from copy import deepcopy


def plotter(values):
    plt.title('Tempo x Iteração')
    plt.ylabel('Tempo')
    plt.xlabel('Iteração')
    plt.plot(values, color='green')
    plt.show()


def tester(qtd, func, *args):
    times = []
    element, *params = args
    for x in range(0, qtd):
        c = deepcopy(element)
        start = time.time()
        func(c, *params)
        end = time.time()
        total = end - start
        times.append(total)
    return times