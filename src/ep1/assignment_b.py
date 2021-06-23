import numpy as np
import matplotlib.pyplot as plt

from QR_fatoration import QR_fatoration
from QR_algorithm import QR_algorithm

def make_A_matrix(n,k,m):
    A = np.zeros((n,n))
    for i in range(1,n):
        ki = k(i)
        ki_plus = k(i+1)
        A[i-1,i-1] = ki + ki_plus
        A[(i-1),(i-1)+1] = A[(i-1)+1,(i-1)] = -ki_plus
    A[n-1,n-1] = k(n) + k(n+1)
    A = A/m
    return A
    pass

if __name__ == "__main__":
    # dates
    m = 2 # kg
    n = 5 # numbers of mass
    k = lambda i: 40 + 2*i # k mola

    x0_1 = np.array([-2,-3,-1,-3,-1])
    x0_2 = np.array([1,10,-4,3,-2])

    A = make_A_matrix(n,k,m)

    
    pass
