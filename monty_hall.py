# https://www.youtube.com/watch?v=ggDQXlinbME
import random as r


# constants
population_size = 10000
change_answer = True
doors = {'0': True, '1': False, '2': False}  # cluster of doors


# create list of initial gueses (expect equal distribution)
def generate_initial_distribution(pop_size):
    pop = []
    for i in range(pop_size):
        pop.append(r.randint(0, 2))
    return pop


# returns the count of each door in a given population as a dictionary
def return_count(population):
    a, b, c = 0, 0, 0
    for i in population:
        if i == 0:
            a += 1
        elif i == 1:
            b += 1
        elif i == 2:
            c += 1
        else:
            print('invalid population at i: ' + str(i))
    return {'0': a, '1': b, '2': c, 'total': a + b + c}


# takes initial pop and bool for changing guess on second round. Creates a new population of final guesses.
def second_guess(population, change_bool):
    # array to be returned
    population_2 = []
    # loop through existing population
    for i in population:
        # if meant to change
        if change_bool:
            new_guess = i
            # will continue generating new guesses until it doesn't match first guess. Simulates
            # changing mind while preserving randomness of second guess.
            while new_guess == i:
                new_guess = r.randint(0, 2)
            population_2.append(new_guess)
        # will result in identical array returned
        else:
            return population
    return population_2


# returns the percentage of guesses that were correct
def percent_correct(population):
    total_correct = 0
    for i in population:
        if doors[str(i)]:
            total_correct += 1
    return total_correct / len(population)


pop = generate_initial_distribution(population_size)
# print('initial population: ', pop)
print('count of each guess in initial distribution: ', return_count(pop))
second_pop = second_guess(pop, change_answer)
print('count of each guess in final distribution: ', return_count(second_pop))
print('the accuracy of this method was: ', percent_correct(second_pop))
