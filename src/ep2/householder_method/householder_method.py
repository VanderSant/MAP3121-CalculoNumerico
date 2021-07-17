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


def get_alfa(A):
    alfa = np.array([])
    for i in range (1,len(A),1):
        alfa = np.append(alfa,A[i,0])
    return alfa

def get_A1(A):
    len1 = len(A)
    len2 = len(A[1])
    return A[1:len1,1:len2]

def get_wi(A):

    pass

def main():
    A = np.array([[2,-1,1,3],
                  [-1,1,4,2],
                  [1,4,2,-1],
                  [3,2,-1,1]])

    print(get_A11(A))
    print(get_alfa(A))
    print(get_A1(A))
    print(get_e(3))

    pass
if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n Better luck next time")
