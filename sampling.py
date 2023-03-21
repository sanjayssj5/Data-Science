
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


#Weighted Sampling

elements = ['a', 'b', 'c', 'd', 'e']

# Define a list of weights for each element
weights = [0.03, 0.03, 0.9, 0.02, 0.02]

# Use NumPy's choice() function to perform weighted sampling
samples = np.random.choice(elements, size=2, p=weights)

# Print the samples
print(samples)


#Stratified Sampling

import numpy as np

# Create a population array with 4 groups of data
population = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Create an array of labels for the groups
labels = np.array([0, 1, 0, 1])

# Get the unique labels and their counts
unique_labels, counts = np.unique(labels, return_counts=True)

# Define the sample size for each group
sample_size = 1

# Initialize an empty sample array
sample = np.array([])

# Iterate over the unique labels and take a random sample from each group
for label in unique_labels:
    # Get the indices of the current label
    indices = np.where(labels == label)[0]
    # Take a random sample of the specified size from the indices
    sample_indices = np.random.choice(indices, size=sample_size, replace=False)
    # Append the sampled data to the sample array
    sample = np.append(sample, population[sample_indices])

# Reshape the sample array to the correct shape
sample = sample.reshape((len(unique_labels) * sample_size, -1))

# Print the sample
print(sample)

