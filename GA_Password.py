#!/usr/bin/env python

import random

def random_individual():
    return [ random.randint(0, 9) for _ in range(10) ]
    # return [4,2,3,1,5,5,7,8,9,0]

combination = random_individual()
def fitness(individual):
    fitnessNum = 0
    for x in range (0, len(individual)):
        if individual[x] == combination[x]:
            fitnessNum += 2
        else:
            for y in combination:
                if individual[x] == combination[y]:
                    fitnessNum += 1
                    break
    return fitnessNum

def probability(individual, fitness):
    return fitness(individual) / 20

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"

def crossover(x, y):
    child = []
    num = 0
    while len(child) < len(x):
        n = random.randint(0, 1)
        if n == 0:    
            child.append(x[num])
        else:
            child.append(y[num])
        
        num += 1
    
    return child

def mutate(x):
    n = len(x)
    
    for num in range(0, random.randint(1, 3)):
        c = random.randint(0, n - 1)
        m = random.randint(0, 9)
        x[c] = m
    return x
     
def genetic_queen(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities)
        y = random_pick(population, probabilities)
        child = crossover(x, y)
        if random.random() < mutation_probability:
            child = mutate(child)
        print_individual(child)
        new_population.append(child)
        if fitness(child) == 20: break
    return new_population

def print_individual(x):
    print("{},  fitness = {}, probability = {:.6f}"
        .format(str(x), fitness(x), probability(x, fitness)))

if __name__ == "__main__":
    # individual = random_individual()
    # print (individual)
    # print (fitness(individual))

    population = [random_individual() for _ in range(100)]
    generation = 1

    while not 20 in [fitness(x) for x in population]:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population, fitness)
        print("Maximum fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1

    print("Solved in Generation {}!".format(generation-1))
    print("Original Combination: "+str(combination))
    for x in population:
        if fitness(x) == 20:
            print_individual(x)

