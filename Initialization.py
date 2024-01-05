"""
Defining Weeks-Chandler-Andersen potential and function that computes partition function via exponential integration
"""

import numpy as np
import random
from sklearn.neighbors import NearestNeighbors


def WCA(sigmas, distances):
    return (4*((sigmas/distances)**12 - (sigmas/distances)**6) + 1)

def Partition_coef(rad, data, num_atoms, n_neighbors, box_dim, number_of_insertions):
    Average_Partition_coef_total = 0
    time_steps = int(len(data)/num_atoms)
    
    for time_step in np.arange(0, time_steps, 1):
        data_timestep = data[time_step*num_atoms : ((time_step + 1) * num_atoms)] # Reading one time_step
        coordinates = data_timestep[:, 1:] # Last three columns are coordinates
        radii = data_timestep[:, 0] # First column is radius
        
        KNN = NearestNeighbors(n_neighbors=n_neighbors).fit(coordinates)
        insert_coordinates = (np.random.rand(number_of_insertions,3) - 0.5) * box_dim # Randomly generating insertion coordinates
        distances, indices = KNN.kneighbors(insert_coordinates)
        
        sigmas = rad + radii[indices] # Shape = (number_of_insertions, n_neighbors) 
        energies = WCA(sigmas, distances)
        energies[distances > sigmas*(2**(1/6))] = 0
        Partition_coefs = np.exp(-np.sum(energies , axis = 1))
        Average_Partition_coef_total += np.mean(Partition_coefs) # Averaging for one time step
    
    Average_Partition_coef = Average_Partition_coef_total/time_steps # Averaging for all time steps
    
    return Average_Partition_coef
