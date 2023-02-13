import numpy as np

#generate 1D array of floating point numbers
a=1.0*np.arange(0,25,3) 
print('\n My 1D array: \n', a)

#Transform it from 1D array (1x9) to 3x3 square matrix using two methods
b = np.reshape(a, (3, 3)) 
print('\n 1D array reshaped into square matrix using method 1: \n', b)

b = a.reshape((3, 3)) 
print('\n ...and method 2 \n', b)

#Select sequence of elements from an array
print('\n Elements of a from 0th to 7th with the step of 2: \n', a[0:7:2]) 
print('\n All elements of a from 0th to 7th: \n', a[0:7:]) 
print('\n All elements of a from 0th to 7th (method 2): \n', a[:7]) 

##generate a new 3x3 matrix it contains all elements of matrix b, but multiplied by 2.4 
c=2.4*b

#Concatenate them vertically 
d=np.concatenate([b,c])
print('\n Vertically concatenated matrix, method 1: \n', d)
d=np.vstack([b,c])
print('\n ...and method 2: \n', d)

#Concatenate them horizontally
d=np.concatenate([b,c], axis=1)
print('\n Horizontally concatenated matrix, method 1: \n', d)
d=np.hstack([b,c])
print('\n ...and method 2: \n', d)

##Transpose a matrix (swap rows and columns)
d=np.transpose(d)
print('\n Trnsposed matrix: \n', d)