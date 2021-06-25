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
    ## Determine as frequências e seus respectivos modos de vibração.

    # Os auto-vetores representam os modos naturais de vibração
    # Os auto-valores determinam as frequências de vibração

    # Q é a matriz ortogonal cujas colunas são os auto-vetores de A
    # Λ é a matriz diagonal composta pelos auto-valores de A

    # Y -> frequência determinada por um auto-valor de A
    # X -> posição da massa
    erro = 1e-6

    # dates
    m = 2 # kg
    n = 5 # numbers of mass
    k = lambda i: 40 + 2*i # k mola
    x_1 = np.array([[-2],[-3],[-1],[-3],[-1]])
    x_2 = np.array([[1],[10],[-4],[3],[-2]])

    A = make_A_matrix(n,k,m)
    Q,Λ = QR_algorithm(A,erro = erro,spectral_shift = True)[0:2]

    y_1 = np.transpose(Q)@x_1
    y_2 = np.transpose(Q)@x_2

    t_array = np.array([])
    x_array = np.array([])
    y_array = np.array([])

    dt = 0.01
    for t in np.arange(0,60,dt):
        t_array = np.append(t_array,t)
        x_array = np.append(x_array,x_1[0])
        y_array = np.append(y_array,y_1[0])



    #plt.plot(t_array,x_array)
    #plt.show()
    pass
