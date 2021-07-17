#!/usr/bin/env python3
# coding=utf-8

import numpy as np

def get_e(n):
    e = np.zeros((1,n))
    e[0,0] = 1
    return e

def get_A11(A):
    A11 = A[0,0]
    return A11

def get_alfa(A,j):
    alfa = np.array([])
    for i in range (1,len(A),1):
        alfa = np.append(alfa,A[i,j])
    return alfa

def get_ai(A):
    ai = np.array([])
    ai = np.append(ai,0)
    for i in range (1,len(A),1):
        ai = np.append(ai,A[i,0])
    return ai

def get_A1(A):
    len1 = len(A)
    len2 = len(A[1])
    return (A[1:len1,1:len2])

def get_delta(A):
    return (A[1,0]/abs(A[1,0]))

def get_wi(A):
    ai = np.array([])#np.zeros((1,1))
    ai = np.append(ai,get_alfa(A,0))
    n = len(ai)
    wi = ai+(get_delta(A)*np.linalg.norm(ai)*get_e(n))
    return wi

def test_wi(A):
    alfa = get_alfa(A)
    wi = get_wi(A)
    y = alfa - (2*(np.inner(wi,alfa)/np.inner(wi,wi))*wi)
    print(y)

def householder_matrix_multiply(A):
    get_hwi_x = lambda w,x: (x - (2*(np.inner(w,x)/np.inner(w,w))*w))
    n = len(A)
    new_A = np.zeros((n,n))
    #print(new_A)
    #print(A)
    for i in range(0,n-1):
        m = len(A)
        wi = get_wi(A)
        for j in range(0,m):
            A[i+1:n,j] = get_hwi_x(wi,get_alfa(A,j))
        for j in range(0,m):
            A[j,i+1:n] = get_hwi_x(wi,get_alfa(np.transpose(A),j))
        new_A[i:n,i:n] = A
        A = np.delete(A,0,0)
        A = np.delete(A,0,1)
        print("new_A = ",new_A,"\n")
        print("A = ",A,"\n")
    pass

def householder_algorithm():

    pass

def main():
    A = np.array([[2.,-1.,1.,3.],
                  [-1.,1.,4.,2.],
                  [1.,4.,2.,-1.],
                  [3.,2.,-1.,1.]])
    #print("teste get_A11 \n",get_A11(A),"\n")
    #print("teste get_alfa \n",get_alfa(A),"\n")
    #print("teste get_a \n",get_ai(A),"\n")
    #print("teste get_A1 \n",get_A1(A),"\n")
    #print("teste get_e \n",get_e(3),"\n")
    #print("teste get_delta \n",get_delta(A),"\n")
    #print("teste get_wi \n",get_wi(A),"\n")
    #test_wi(A)
    householder_matrix_multiply(A)

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n Better luck next time")
