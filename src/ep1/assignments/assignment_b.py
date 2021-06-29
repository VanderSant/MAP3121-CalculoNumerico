#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape

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
    y = np.zeros(shape = [len(y0),1], dtype = float)
    for i in range(0,len(y0)):
        y[i] = y_t(t,i,y0,lamb)
    return y

def plot_graphic(t_array,y_array,y_label = 'frequency',x_label = 'time',label = "x"):
    quantity_graphics = len(y_array)
    fig, axs = plt.subplots(quantity_graphics)
    for i in range(0,quantity_graphics,1):
        axs[i].plot(t_array,y_array[i],label='{la}{it}'.format(it = i,la = label))
        axs[i].set_title('{la}{it}'.format(it = i,la = label))
        axs[i].set_ylabel(y_label)
        axs[i].set_xlabel(x_label)
    plt.show()


def get_points(dt,x,y,n):
    t_array = np.array([])
    time = 60 #segundos

    y_array = np.zeros(shape = [n,1], dtype = float)
    x_array = np.zeros(shape = [n,1], dtype = float)

    for t in np.arange(0,time,dt):
        t_array = np.append(t_array,t)
        y_array = np.append(y_array,y(t),axis = 1)
        x_array = np.append(x_array,x(t),axis = 1)

    y_array = np.delete(y_array,0,1)
    x_array = np.delete(x_array,0,1)

    return [t_array,x_array,y_array]


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
    t_array,x_array,y_array = get_points(dt,x_2,y_2,n)

    plot_graphic(t_array,y_array,label = "y")
    plot_graphic(t_array,x_array,y_label = 'position', x_label = 'time',label = "x")

if __name__ == "__main__":
    assignment_b()
