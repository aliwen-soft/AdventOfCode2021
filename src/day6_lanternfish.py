
def read_initial_population(file_name):
    with open(file_name) as file:
        initial_population_string = file.readlines()[0]
        initial_population = [int(str) for str in initial_population_string.split(',')]
    return initial_population

def count_population(population):
    return [population.count(i) for i in range(9)]

def increment_population(population):
    # print(population)
    updated_population = population.copy()
    for i, fish_timer in enumerate(population):
        if fish_timer == 0:
            updated_population[i] = 6
            updated_population.append(8)
        else:
            updated_population[i] = updated_population[i] - 1
    return updated_population

def increment_population_counts(population_counts):
    updated_population_counts = population_counts[1:9].copy()
    updated_population_counts[6] += population_counts[0]
    updated_population_counts.append(population_counts[0])
    return updated_population_counts

def day_six_part_one(test=False):
    if test:
        population = read_initial_population('data/day_six_test.txt')
    else:
        population = read_initial_population('data/day_six.txt')
    
    for _ in range(256):
        population = increment_population(population)
    
    return(len(population))

def day_six_part_two(test=False):
    if test:
        population = read_initial_population('data/day_six_test.txt')
    else:
        population = read_initial_population('data/day_six.txt')
    
    population_counts = count_population(population)

    for _ in range(256):
        print(population_counts)
        population_counts = increment_population_counts(population_counts)
    
    return sum(population_counts)

#print(day_six_part_two(test=True))
print(day_six_part_two())
