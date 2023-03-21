
import random
import pdb
import numpy as np
#pdb.set_trace()
#Random Sampling

a = ['apple','banan','orange','apple','grape']

sample_size =4

k2= random.sample(a,sample_size)
print(k2)


#Sytematic Sampling
# population data
population = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# sample size
sample_size = 5

# determine the interval
interval = len(population) // sample_size

# select the sample using systematic sampling
sample = population[::interval]

print("Population: ", population)
print("Sample: ", sample)


#Cluster Sampling

# population data
population = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# define the number of clusters
num_clusters = 2

# randomly select the clusters
cluster_indices = np.random.choice(num_clusters, size=num_clusters, replace=False)

# select the clusters from the population
cluster_sample = population[cluster_indices]

# print the cluster sample
print(cluster_sample)