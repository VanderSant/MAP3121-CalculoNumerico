#!/usr/bin/env python3
# coding=utf-8

import numpy as np

def get_e(n):
    e = np.zeros((1,n))
    e[0,0] = 1
    return e

def get_alfa(A,j):
    alfa = np.array([])
    for i in range (1,len(A),1):
        alfa = np.append(alfa,A[i,j])
    return alfa

def get_delta(A):
    return (A[1,0]/abs(A[1,0]))

def norm(A):
    x=0
    for i in range (len(A)):
        x=x+(A[i]**2)
    x = np.sqrt(x)
    return x

def get_wi(A):
    ai = np.array([])
    ai = np.append(ai,get_alfa(A,0))
    n = len(ai)
    wi = ai+(get_delta(A)*norm(ai)*get_e(n))
    return wi

def householder_algorithm(A,debug = False):
    get_hwi_x = lambda w,x: (x - (2*(np.inner(w,x)/np.inner(w,w))*w))
    n = len(A)
    new_A = np.zeros((n,n))
    for i in range(0,n-2):
        m = len(A)
        wi = get_wi(A)
        for j in range(0,m):
            A[1:m,j] = get_hwi_x(wi,get_alfa(A,j))
        for j in range(0,m):
            A[j,1:m] = get_hwi_x(wi,get_alfa(np.transpose(A),j))
        new_A[i:n,i:n] = A
        A = np.delete(A,0,0)
        A = np.delete(A,0,1)
    new_A[n-2:n,n-2:n] = A
    if(debug==True):
        print("new_A = \n",np.matrix.round(new_A,4),"\n")
    return new_A

def test_wi(A):
    alfa = get_alfa(A)
    wi = get_wi(A)
    y = alfa - (2*(np.inner(wi,alfa)/np.inner(wi,wi))*wi)
    print(y)

def test_householder_algorithm():
    A = np.array([[2.,-1.,1.,3.],
                  [-1.,1.,4.,2.],
                  [1.,4.,2.,-1.],
                  [3.,2.,-1.,1.]])
    householder_algorithm(A,debug=True)

if __name__ == "__main__":
    try:
        test_householder_algorithm()

    except KeyboardInterrupt:
        print("\n Better luck next time")
