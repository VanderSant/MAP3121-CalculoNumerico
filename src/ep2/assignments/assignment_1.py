#!/usr/bin/env python3
# coding=utf-8

import numpy as np

from householder_method.householder_algorithm import householder_algorithm
from QR_method.QR_algorithm import QR_algorithm

INFO = '''
TAREFA 4.1:
(a) Tarefa 4.1.a: Calculo dos auto valores e autovetores da matriz:
    [2., 4., 1., 1.]
    [4., 2., 1., 1.]
    [1., 1., 1., 2.]
    [1., 1., 2., 1.]

(b) Tarefa 4.1.b: Calculo dos auto valores e autovetores da matriz:
    [ n  n-1 n-2 ...  2   1 ]
    [n-1 n-1 n-2 ...  2   1 ]
    [n-2 n-2 n-2 ...  2   1 ]
    [ :   :   :  ...  :   : ]
    [ 2   2   2   2   2   1 ]
    [ 1   1   1   1   1   1 ]
'''
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

def get_eigenvalues(n):
    lamb = np.array([])
    eigenvaluesi = lambda i: ((1/2)*((1 - np.cos((2*i-1)*np.pi/(2*n+1)))**(-1)))
    for i in range(1,n+1):
        lamb = np.append(lamb,eigenvaluesi(i))
    return lamb

def assignment_1_a(debug = False):
    np.set_printoptions(precision=5,threshold=5) #print options
    A = np.array([[2., 4., 1., 1.],
                  [4., 2., 1., 1.],
                  [1., 1., 1., 2.],
                  [1., 1., 2., 1.]])

    A = householder_algorithm(A)
    V,lamb = QR_algorithm(A)[0:2]
    print("autovetores =\n",V)
    print("autovalores =\n",np.diagonal(lamb),"\n")

    if(debug == True):
        for i in range(0,len(A)):
            print('teste {j}'.format(j=i))
            print(A@V[:,i],"\n",np.diagonal(lamb)[i]*V[:,i],"\n")

def assignment_1_b():
    np.set_printoptions(precision=3,threshold=200,linewidth=1000) #print options
    n = 20
    B = make_matrixB(n)
    B = householder_algorithm(B)
    V,lamb = QR_algorithm(B)[0:2]
    eigenvalues = get_eigenvalues(n)

    print("autovetores =\n",V)
    print("autovalores =\n",np.diagonal(lamb))
    print("autovalores esperados =\n",eigenvalues)

def assignment_1():
    print(INFO,"\n")
    item = input("Gostaria de ver qual item? ")
    if ((item == "a") or (item == "4.1.a")):
        assignment_1_a()
        print("\n")
    elif ((item == "b") or (item == "4.1.b")):
        assignment_1_b()
        print("\n")
    else:
        print("your input isn't valid \nplease, try again\n")

if __name__ == "__main__":
    try:
        assignment_1()

    except KeyboardInterrupt:
        print("\n Better luck next time")
