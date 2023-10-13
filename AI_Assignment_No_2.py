import sys
import random
import math
import matplotlib.pyplot as plt
import numpy as np

maxint = sys.maxsize
cities = ["A", "B", "C", "D", "E", "F", "G"]
order = []
totalCities = len(cities)
cityPoints = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'A': 12, 'C': 8, 'D': 12},
    'C': {'A': 10, 'B': 8, 'D': 11, 'E': 3, 'G': 9},
    'D': {'B': 12, 'C': 11, 'E': 11, 'F': 10},
    'E': {'C': 3, 'D': 11, 'F': 6, 'G': 7},
    'F': {'D': 10, 'E': 6, 'G': 9},
    'G': {'A': 12, 'C': 9, 'E': 7, 'F': 9}
}
population = []
populationSize = 50
fitness = []
bestEver = []
recordDistance = sys.maxsize

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 7))

ax1.set_xlim([0, 10])
ax1.set_ylim([0, 10])
ax2.set_xlim([0, 10])
ax2.set_ylim([0, 10])
plt.ion()
Ln, = ax1.plot(random.sample(range(0, 1000), totalCities), marker='o', color='b')
Ln2, = ax2.plot(random.sample(range(0, 1000), totalCities), marker='o', color='r')
plt.show()


def plotDistance(order, bestEver):
    cityX = []
    cityY = []
    for i in order:
        cityX.append(cityPoints[i][0])
        cityY.append(cityPoints[i][1])
    npcityX = np.array(cityX)
    npcityY = np.array(cityY)

    if bestEver:
        Ln2.set_ydata(npcityY)
        Ln2.set_xdata(npcityX)
    else:
        Ln.set_ydata(npcityY)
        Ln.set_xdata(npcityX)
    plt.pause(0.001)


def eucDistance(a, b):
    a_x, a_y = cityPoints[a]
    b_x, b_y = cityPoints[b]
    d = math.sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)
    return d


def createPopulation():
    for i in range(0, totalCities):
        order.append(i)

    for i in range(0, populationSize):
        population.append(random.sample(order, len(order)))


def calcDistance(curr_order):
    sum = 0
    for i in range(0, len(curr_order) - 1):
        d = eucDistance(cities[curr_order[i]], cities[curr_order[i + 1]])
        sum += d
    return sum


def calcFitness():
    global recordDistance, bestEver
    for i in range(0, populationSize):
        d = calcDistance(population[i])
        if (d < recordDistance):
            recordDistance = d
            ax1.set_xlabel("Best " + str(d))
            bestEver = population[i].copy()
            plotDistance(bestEver, True)
        fitness.append(1 / (d + 1))
    plotDistance(population[i], False)
    print(recordDistance)
    normalizeFitness()


def normalizeFitness():
    sum = 0
    for i in range(0, populationSize):
        sum += fitness[i]
    for i in range(0, populationSize):
        fitness[i] = fitness[i] / sum


def nextGeneration():
    newPopulation = []
    global population
    for i in range(0, populationSize):
        orderA = pickOne(population, fitness)
        orderB = pickOne(population, fitness)
        order = crossOver(orderA, orderB)
        mutate(order, 0.9)
        newPopulation.append(order)

    population = newPopulation


def crossOver(orderA, orderB):
    start = math.floor(random.randrange(0, len(orderA)))
    end = math.floor(random.randrange(start, len(orderB)))
    newOrder = orderA[start:end]

    for i in orderB:
        if i not in newOrder:
            newOrder.append(i)
    return newOrder


def pickOne(order, prob):
    index = 0
    r = random.random()
    while r > 0:
        r = r - prob[index]
        index += 1
    index -= 1
    return order[index]


def mutate(order, mutationRate):
    for i in range(0, totalCities):
        if random.random() < mutationRate:
            indexA = math.floor(random.randrange(0, len(order)))
            indexB = (indexA + 1) % totalCities
            swap(order, indexA, indexB)


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


if __name__ == "__main__":
    createPopulation()
    
    max_generations = 75  # Set the maximum number of generations
    generation = 0

    while generation < max_generations:
        calcFitness()
        nextGeneration()
        generation += 1
    print("Reached the maximum number of generations.")