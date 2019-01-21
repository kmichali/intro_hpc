# Python code snippet that iterates through a matrix in PBS array run environment
# this will distribute each matrix element to one array run process
# in a corresponding job script, set PBS -J 1-N 
# where N is a total number of matrix elements

import numpy as np
import os

input = np.loadtxt('matrix.txt', dtype='f', delimiter=',')
counter = 0

for i in range(0,input.shape[0]):
    for j in range(0, input.shape[1]):
        counter = counter+1
        index = int(os.environ['PBS_ARRAY_INDEX'])
        if counter == index:
            print('processing element', input[i,j])
            # add your code here



