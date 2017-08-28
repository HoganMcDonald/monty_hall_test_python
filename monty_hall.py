# https://www.youtube.com/watch?v=ggDQXlinbME
import random as r


# constants
population_size = 100
change_answer = True


# cluster of doors
doors = {'0': True, '1': False, '2': False}

i = r.randint(0, 2)
print(str(i), doors[str(i)])


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


pop = generate_initial_distribution(population_size)
print('initial population: ', pop)
print('count of each guess: ', return_count(pop))