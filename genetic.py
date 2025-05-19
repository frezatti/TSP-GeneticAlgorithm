import numpy as np
import pandas as pd
import math
from tsp_io import read_tsp_coords


def calculate_distance_coordenate (city_coordenates):

    num_cities = len(city_coordenates)
    distance_matrix = np.zeros((num_cities,num_cities))


    for i in range(num_cities):
        for j in range(i+1 , num_cities):

            x1,y1 = city_coordenates[i]
            x2,y2 = city_coordenates[j]

            distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    return distance_matrix


def fitness_function(chromosome, distance_matrix):

    fitness = 0
    num_cities = len(chromosome)

    for i in range(num_cities-1):

        city_from = chromosome[i]
        city_to = chromosome[i+1]

        fitness += distance_matrix[city_from][city_to]

    fitness += distance_matrix[chromosome[-1]][chromosome[0]]
    return fitness

def initial_population(population_size, num_cities):

    population = []


    for i  in range(population_size):

        chromosome = list(range(num_cities))
        np.random.shuffle(chromosome)
        population.append(chromosome)
    return population

def tournament_selection(population, distances, tournament_size):

    competitors = np.random.choice(range(len(population)),tournament_size)
    best_index = competitors[0]
    best_distance = distances[best_index]

    for i in competitors[1:]:
        if distances[i] < best_distance:

            best_index = i 
            best_distance = distances[i]

    return population[best_index].copy()

def order_crossover(parent1, parent2):

    size = len(parent1)

    start, end = sorted(np.random.choice(range(size),2, replace = False))

    offspring  = [-1] * size


    for i in range (start, end +1):
        offspring[i] = parent1[i]

    parent2_idx = 0
    offspring_idx = (end + 1) % size
        
    while -1 in offspring:
        next_city = parent2[parent2_idx]
            
        if next_city not in offspring:
                offspring[offspring_idx] = next_city
                offspring_idx = (offspring_idx + 1) % size
                
        parent2_idx = (parent2_idx + 1) % size
        
    return offspring

def swap_mutation(chromosome, mutation_rate):
    if np.random.random() < mutation_rate:
        idx1, idx2 = np.random.choice(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    
    return chromosome


def genetic_algorithm_tsp(distance_matrix, population_size = 100, num_generations = 500, tournament_size = 3,
                          crossover_rate = 0.8, mutation_rate = 0.02, elite_size = 2  ): 
    num_cities = len(distance_matrix)

    population = initial_population(population_size, num_cities)

    best_tour = None

    best_distance =  float('inf')


    for generation in range(num_generations):
        distances = [fitness_function(individual, distance_matrix) for individual in population]

        min_idx = distances.index(min(distances))
        if distances[min_idx] < best_distance:
                    best_distance = distances[min_idx]
                    best_tour = population[min_idx].copy()
                    if generation%50 ==0: 
                        print(f"Generation {generation}: New best distance = {best_distance}")


        next_population = []


        elite_indices = sorted(range(len(distances)), key = lambda i: distances[i])[:elite_size]

        for idx in elite_indices:
            next_population.append(population[idx].copy())


        while len(next_population) < population_size:

            parent1 = tournament_selection(population, distances, tournament_size)
            parent2 = tournament_selection(population, distances, tournament_size)



            if np.random.random() < crossover_rate:
                offspring = order_crossover(parent1, parent2)

            else: 
                offspring = parent1.copy()


            offspring = swap_mutation(offspring, mutation_rate)

            next_population.append(offspring)



        population = next_population


    return best_tour, best_distance






if __name__ == "__main__":

    tsp_filepath = './berlin52.tsp' 

    city_coords = read_tsp_coords(tsp_filepath) 

    if city_coords is None:
        print("Failed to load coordinates. Exiting.")
        exit()

    if not city_coords:
        print("No coordinates found in the file. Exiting.")
        exit()

    num_cities = len(city_coords)
    city_names = [f'City {i}' for i in range(num_cities)]

    print(f"Successfully loaded {num_cities} cities from {tsp_filepath}")
    # ... (rest of your main block code remains the same) ...


    distance_matrix = calculate_distance_coordenate(city_coords)

    print("\nCalculated Distance Matrix (Partial for large files):")
    index_obj = pd.Index(city_names[:min(10, num_cities)])
    columns_obj = pd.Index(city_names[:min(10, num_cities)])
    distance_df = pd.DataFrame(distance_matrix[:min(10, num_cities), :min(10, num_cities)],
                               index=index_obj, columns=columns_obj)
    print(distance_df.to_string(float_format='{:.4f}'.format))



    POPULATION_SIZE = 100
    NUM_GENERATIONS = 1100
    TOURNAMENT_SIZE = 4  
    CROSSOVER_RATE = 0.85
    MUTATION_RATE = 0.33
    ELITE_SIZE = 2
        
        # Run the algorithm
    best_tour, best_distance = genetic_algorithm_tsp(
        distance_matrix, 
        population_size=POPULATION_SIZE,
        num_generations=NUM_GENERATIONS,
        tournament_size=TOURNAMENT_SIZE,
        crossover_rate=CROSSOVER_RATE,
        mutation_rate=MUTATION_RATE,
        elite_size=ELITE_SIZE
     )
        
        # Print results
    print(f"Best tour found: {best_tour}")
    print(f"Best distance: {best_distance}")
