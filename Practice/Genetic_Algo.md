# 8 Queen:

```py
import random

N = 8
pCount = 100

# Generate Population
def Generate_Population():
    population = []
    for _ in range(pCount):
        chromosome = [random.randint(1, N) for _ in range(N)]  # Random row for each queen
        population.append(chromosome)
    return population

# Fitness Function: Count number of non-attacking pairs
def Fitness(chromosome):
    non_attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking_pairs += 1
    return non_attacking_pairs

# Select the best two parents
def Select(pop, fit):
    sorted_pop = sorted(zip(pop, fit), key=lambda x: x[1], reverse=True)
    return sorted_pop[0][0], sorted_pop[1][0]

# Crossover: Single Point Crossover
def crossover(p1, p2):
    point = random.randint(0, N - 1)
    child = p1[:point] + p2[point:]
    return child

# Mutation: Randomly change the position of a queen
def mutate(chromosome):
    i = random.randint(0, N - 1)
    chromosome[i] = random.randint(1, N)
    return chromosome

# Genetic Algorithm Main Loop
popuation = Generate_Population()
maxGen = 1000
mut_rate = 0.3

for gen in range(maxGen):
    fitness_score = [Fitness(i) for i in popuation]
    best_fit = max(fitness_score)
    print(f"Generation: {gen} BestFit: {best_fit}")

    if best_fit == 28:  # Maximum fitness for 8 queens
        break

    newPop = []
    for _ in range(pCount):
        p1, p2 = Select(popuation, fitness_score)
        child = crossover(p1, p2)
        if random.random() < mut_rate:
            child = mutate(child)
        newPop.append(child)

    popuation = newPop

# Output the solution
solution = popuation[fitness_score.index(best_fit)]
print("Solution:", solution)
```

# Knapsack:

```py
import random

pCount = 4

def Generate_Population():
    population = []
    for i in range(pCount):
        population.append("".join([random.choice("01") for _ in range(4)]))
        
    return population

# Fitness Function

def Fitness(bitstr):
    weight = [5,3,7,2]
    cost = [12,5,10,7]
    tWeight = 0
    tValue = 0
    for i in range(pCount):
        k = int(bitstr[i])
        tWeight += k*weight[i]
        tValue += k*cost[i]
        
    if tWeight > 12:
        return 0
    return tValue

# print(Fitness('0011'))

def Select(pop,fit):
    sortedpop = sorted(zip(pop,fit),key=lambda x:x[1],reverse=True)
    return (sortedpop[0][0],sortedpop[1][0])

def crossover(p1,p2):
    i = random.randint(0,len(p1))
    child = list(p1)
    child[:i] = list(p2[:i])
    print(i,'\n')
    return "".join(child)

# print(crossover("1111","0000"))

def mutate(bitstr):
    bitstr = list(bitstr)
    i = random.randint(0,len(bitstr)-1)
    if bitstr[i] == '1':
        bitstr[i] = '0'
        return "".join(bitstr)

    bitstr[i] = '1'
    return "".join(bitstr)

# print(mutate('1101'))

# GENETIC ALGO

popuation = Generate_Population()
maxGen = 100
mut_rate = 0.4  # k +- (gen*maxGen) +- k
for gen in range(maxGen):
    fitness_score = [Fitness(i) for i in popuation]
    best_fit = max(fitness_score)
    print(f"Generation: {gen} BestFit {best_fit}")
    
    newPop = []
    
    for i in range(pCount):
        parents = Select(popuation,fitness_score)
        p1,p2 = parents
        child = crossover(p1,p2)
        if random.random() < mut_rate:
            child = mutate(child)
        newPop.append(child)
    popuation = newPop
```
