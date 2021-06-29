#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from QR_method.QR_algorithm import QR_algorithm
from assignments.assignment_b import make_A_matrix,get_points,solve_edo,plot_graphic

def assignment_c():
    erro = 1e-6
    # dates
    m = 2 # kg
    n = 10 # numbers of mass
    k = lambda i: 40 + 2*((-1)**i) # k mola
    x_0_1 = np.array([[-2],[-3],[-1],[-3],[-1],[-2],[-3],[-1],[-3],[-1]])
    x_0_2 = np.array([[1],[10],[-4],[3],[-2],[1],[10],[-4],[3],[-2]])

    A = make_A_matrix(n,k,m)
    Q,lamb = QR_algorithm(A,erro = erro,spectral_shift = True)[0:2]
    y_0_1 = np.transpose(Q)@x_0_1
    y_0_2 = np.transpose(Q)@x_0_2

    y_1 = lambda t: solve_edo(t,y_0_1,lamb)
    x_1 = lambda t: Q@solve_edo(t,y_0_1,lamb)

    y_2 = lambda t: solve_edo(t,y_0_2,lamb)
    x_2 = lambda t: Q@solve_edo(t,y_0_2,lamb)

    dt = 0.01
    t_array,x_array,y_array = get_points(dt,x_1,y_1)

    plot_graphic(t_array,y_array,label = "y")
    plot_graphic(t_array,x_array,y_label = 'position', x_label = 'time',label = "x")

if __name__ == "__main__":
    assignment_c()
