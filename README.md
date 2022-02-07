# combination-search

This is a genetic algorithim application to a simple problem of finding a combination of 10 digits, it follows the general iteration/execution structure of davpal's eight queens genetic algorithm solution that you can find here: https://github.com/davpal/eight-queens. 

My modifications have been to the initialization process and data handling during the exection of the algorithm, I have created the methods fitness(individual) and crossover(x, y) specifically for this combination guessing application.

The general idea is of generating a randomized list of 100 10-digit combinations, and being able to use the general genetic algorithm concept of ranking by fitness, selecting for the next generation with crossover and mutation.

Modifications to alter the behavior and execution of the algorithm can be made with the mutation probability, population size @ line 83, editing the length of the combination, and presetting the base combination.

Created for possible use in my IB Extended Essay on February 8th, 2022

Manas Rajendran
