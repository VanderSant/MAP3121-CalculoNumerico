import numpy as np
import sympy as sym

def print_fraction(A, print_min_value=False,print_max_value=False):
    matrix_shape = np.shape(A)
    if(len(matrix_shape)==1):
        A = A[:,np.newaxis]
    variable_row = len(A)
    variable_columns = len(A[0])
    for i in range(0, variable_row):
        for j in range(0,variable_columns):
            print(f"A{i + 1}{j + 1} = {sym.nsimplify(A[i][j])}\n\r")
    if(print_max_value == True):
        print(f"Amax = {sym.nsimplify(max(A)[0])}")
    if(print_min_value == True):
        print(f"Amin = {sym.nsimplify(min(A)[0])}")

def sassenfeld_criteria(A, print_B=False):
    matrix_len = len(A)
    B = np.full(matrix_len, 1, dtype=float)
    for i in range(0, matrix_len):
        B[i] *= 1 / abs(float(A[i,i]))
        next_elements_sum = 0
        for j in range(i + 1, matrix_len):
            next_elements_sum += abs(float(A[i,j]))
        prev_elements_sum = 0
        for j in range(0, i):
            prev_elements_sum += (B[j] * abs(float(A[i,j])))
        B[i] *= (prev_elements_sum + next_elements_sum)
    if(print_B == True):
        print_fraction(B,print_max_value=True)
    return max(B)

#exemple_1
A = np.array([[3,-1,1],[-1,3,1],[1,3,3]])
sassenfeld_criteria(A,True)

#exemple_2
A = np.array([[-5.9,9.6,-8.4],[-9.9,-2.1,5.6],[5.1,-6.6,6.0]])
sassenfeld_criteria(A,True)
