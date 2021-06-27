#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from QR_method.QR_algorithm import QR_algorithm

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

def solve_edo(t,y0,lamb):
    y_t = lambda t,i,y0,lamb,: y0[i]*np.cos(np.sqrt(lamb[i,i])*t)
    y = np.array([])
    for i in range(0,len(y0)):
        y = np.append(y,y_t(t,i,y0,lamb))
    return y

def get_points_and_plot(dt,x,y):
    t_array = np.array([])

    y_array_0 = np.array([])
    y_array_1 = np.array([])
    y_array_2 = np.array([])
    y_array_3 = np.array([])
    y_array_4 = np.array([])

    x_array_0 = np.array([])
    x_array_1 = np.array([])
    x_array_2 = np.array([])
    x_array_3 = np.array([])
    x_array_4 = np.array([])

    for t in np.arange(0,60,dt):
        t_array = np.append(t_array,t)
        #x_array = np.append(x_array,x(t)[0])
        y_array_0 = np.append(y_array_0,y(t)[0])
        y_array_1 = np.append(y_array_1,y(t)[1])
        y_array_2 = np.append(y_array_2,y(t)[2])
        y_array_3 = np.append(y_array_3,y(t)[3])
        y_array_4 = np.append(y_array_4,y(t)[4])

        x_array_0 = np.append(x_array_0,x(t)[0])
        x_array_1 = np.append(x_array_1,x(t)[1])
        x_array_2 = np.append(x_array_2,x(t)[2])
        x_array_3 = np.append(x_array_3,x(t)[3])
        x_array_4 = np.append(x_array_4,x(t)[4])

    plt.plot(t_array,y_array_0)
    plt.plot(t_array,y_array_1)
    plt.plot(t_array,y_array_2)
    plt.plot(t_array,y_array_3)
    plt.plot(t_array,y_array_4)
    plt.show()

    plt.plot(t_array,x_array_0)
    plt.plot(t_array,x_array_1)
    plt.plot(t_array,x_array_2)
    plt.plot(t_array,x_array_3)
    plt.plot(t_array,x_array_4)
    plt.show()

def assignment_b():
    ## Determine as frequências e seus respectivos modos de vibração.

    # Os auto-vetores representam os modos naturais de vibração
    # Os auto-valores determinam as frequências de vibração

    # Q é a matriz ortogonal cujas colunas são os auto-vetores de A
    # lamb é a matriz diagonal composta pelos auto-valores de A

    # Y -> frequência determinada por um auto-valor de A
    # X -> posição da massa
    erro = 1e-6
    # dates
    m = 2 # kg
    n = 5 # numbers of mass
    k = lambda i: 40 + 2*i # k mola
    x_0_1 = np.array([[-2],[-3],[-1],[-3],[-1]])
    x_0_2 = np.array([[1],[10],[-4],[3],[-2]])

    A = make_A_matrix(n,k,m)
    Q,lamb = QR_algorithm(A,erro = erro,spectral_shift = True)[0:2]
    y_0_1 = np.transpose(Q)@x_0_1
    y_0_2 = np.transpose(Q)@x_0_2

    y_1 = lambda t: solve_edo(t,y_0_1,lamb)
    x_1 = lambda t: Q@solve_edo(t,y_0_1,lamb)

    y_2 = lambda t: solve_edo(t,y_0_2,lamb)
    x_2 = lambda t: Q@solve_edo(t,y_0_2,lamb)

    dt = 0.1

    get_points_and_plot(dt,x_2,y_2)


if __name__ == "__main__":
    assignment_b()
