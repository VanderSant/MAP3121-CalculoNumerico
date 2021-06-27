#!/usr/bin/env python3
#coding=utf-8

# imports
import numpy as np
import matplotlib.pyplot as plt

from QR_method.QR_algorithm import QR_algorithm

def make_tridiagonal_matrix(n,alfa,beta):
    A = alfa*np.eye(n)
    for i in range (0,n-1):
        A[i,i+1] = beta
        A[i+1,i] = beta
    return A

def test_matrix_values(A,V,lamb):
    print("V = ", V)
    print("lamb = ",lamb)
    new_A = V@lamb@np.transpose(V)
    new_A = np.matrix.round(new_A,3)
    print("\n")
    print("A = \n", A)
    print("V Λ V_transposto = \n", new_A)


def assignment_a():
    erro = 1e-6
    alfa = 2
    beta = -1

    k_with_spectral_shift_list = np.array([])
    k_without_spectral_shift_list = np.array([])
    print("Assignment A: Example of using the QR algorithm in a tridiagonal matrix")
    print("For this assignment we used: \n 'n' as size of the matirx \n 'k' as number of iterations")
    n_list = np.array([])
    for i in range (2,6):
        n = 2**i
        print("For n = ", n)
        n_list = np.append(n_list,n)
        A_matrix = make_tridiagonal_matrix(n,alfa,beta)

        V,lamb,k = QR_algorithm(A_matrix,erro = erro,spectral_shift = True)
        k_with_spectral_shift_list = np.append(k_with_spectral_shift_list,k)
        print("k with spectral shift = ", k)
        #test_matrix_values(A_matrix,V,lamb)

        V,lamb,k = QR_algorithm(A_matrix,erro = erro,spectral_shift = False)
        k_without_spectral_shift_list = np.append(k_without_spectral_shift_list,k)
        print("k without spectral shift = ", k)
        #test_matrix_values(A_matrix,V,lamb)

    plt.xlim(min(n_list), max(n_list))
    plt.ylim(0, 2000)

    plt.plot(n_list,k_with_spectral_shift_list,label='k_with_spectral_shift')
    plt.plot(n_list,k_without_spectral_shift_list,label='k_without_spectral_shift')
    plt.ylabel('number of iterations')
    plt.xlabel('matrix (nxn)')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2, frameon=False)
    plt.show()

if __name__ == "__main__":
    assignment_a()
