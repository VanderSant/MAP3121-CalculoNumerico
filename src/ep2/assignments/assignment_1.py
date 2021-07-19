#!/usr/bin/env python3
# coding=utf-8

import numpy as np

from householder_method.householder_algorithm import householder_algorithm
from QR_method.QR_algorithm import QR_algorithm

def assignment_1_a():
    A = np.array([[2., 4., 1., 1.],
                  [4., 2., 1., 1.],
                  [1., 1., 1., 2.],
                  [1., 1., 2., 1.]])

    A = householder_algorithm(A)
    V,lamb = QR_algorithm(A)[0:2]
    print("V =\n",V)
    print("lamb =\n",np.diagonal(lamb))

    pass

def make_matrixB(n):
    B = np.zeros((n,n),dtype = float)
    for i in range (2,n+2,1):
        add = (i-1)*np.ones((n-i+2,n-i+2),dtype=float)
        B[0:n-i+2,0:n-i+2] = add[0:n-i+2:,0:n-i+2]
    return B

def make_matrixB_alt(n):
    B= np.zeros((n,n))
    B[0,0] = n
    for i in range (1,len(B),1):
        B[i,0:i] = n-i
        B[0:i,i] = n-i
        B[i,i] = n-i
    return B

def assignment_1_b():
    n = 20
    B = make_matrixB(n)
    B = householder_algorithm(B)
    V,lamb = QR_algorithm(B)[0:2]
    print("V =\n",V)
    print("lamb =\n",np.diagonal(lamb))
    pass

if __name__ == "__main__":
    try:
        assignment_1_b()

    except KeyboardInterrupt:
        print("\n Better luck next time")
