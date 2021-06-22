# imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from QR_fatoration import QR_fatoration
from QR_algorithm import QR_algorithm









if __name__ == "__main__":
    erro = 1e-6
    for i in range (2,6):
        #n = int(input('insert matrix size n (n x n): '))
        n = 2**i
        A_matrix = 2*np.eye(n)
        for i in range (0,n-1):
            A_matrix[i,i+1] = -1
            A_matrix[i+1,i] = -1

        V,lamb,k = QR_algorithm(A_matrix,erro = erro,spectral_shift = True )
        print("V = ", V)
        print("lamb = ",lamb)
        print("k with spectral shift = ", k)
        new_A = V@lamb@np.transpose(V)
        new_A = np.matrix.round(new_A,3)
        print("\n")
        print("A = \n", A_matrix)
        print("V Λ V_transposto = \n", new_A)

        V,lamb,k = QR_algorithm(A_matrix,erro = erro,spectral_shift = False)
        print("V = ", V)
        print("lamb = ",lamb)
        print("k without spectral shift= ", k)
        new_A = V@lamb@np.transpose(V)
        new_A = np.matrix.round(new_A,3)
        print("\n")
        print("A = \n", A_matrix)
        print("V Λ V_transposto = \n", new_A)
