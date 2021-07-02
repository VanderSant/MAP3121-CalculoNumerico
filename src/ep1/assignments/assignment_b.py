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
    y = np.zeros(shape = [len(y0),1], dtype = float)
    for i in range(0,len(y0)):
        y[i] = y_t(t,i,y0,lamb)
    return y

def plot_graphics(t_array,y_array,y_label = 'frequency',x_label = 'time',label = "x"):
    color_array = np.array(["blue","green","red","cyan","magenta","yellow","black","blue","green","red","cyan","magenta","yellow","black"])
    quantity_graphics = len(y_array)
    fig, axs = plt.subplots(quantity_graphics)
    for i in range(0,quantity_graphics,1):
        axs[i].plot(t_array,y_array[i],label='{la}{it}'.format(it = i,la = label),color=color_array[i])
        axs[i].set_title('{la}{it}'.format(it = i,la = label))
        axs[i].set_ylabel(y_label)
        axs[i].set_xlabel(x_label)
    plt.show()

def print_separado(t_array,x_array):
    color_array = np.array(["blue","green","red","cyan","magenta","yellow","black","blue","green","red","cyan","magenta","yellow","black"])
    quantity_graphics = len(x_array)
    for i in range(0,quantity_graphics,1):
        plt.xlim(min(t_array), max(t_array))
        plt.ylim(min(x_array[i]), max(x_array[i]))

        plt.plot(t_array,x_array[i],label='massa {a}'.format(a=i+1),color=color_array[i])
        plt.ylabel('x(t)')
        plt.xlabel('time(s)')

        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2, frameon=False)
        plt.show()


def get_points(dt,x,y):
    t_array = np.array([])
    time = 10 #segundos

    color =  np.array([])

    n = len(y(0))
    y_array = np.zeros(shape = [n,1], dtype = float)
    x_array = np.zeros(shape = [n,1], dtype = float)

    for t in np.arange(0,time,dt):
        t_array = np.append(t_array,t)
        y_array = np.append(y_array,y(t),axis = 1)
        x_array = np.append(x_array,x(t),axis = 1)

    y_array = np.delete(y_array,0,1)
    x_array = np.delete(x_array,0,1)

    return [t_array,x_array,y_array]

def print_frequency(lamb,n):
    frequencia = (np.sqrt(np.diagonal(lamb)))/(2*np.pi)
    periodo = (1/frequencia)
    for i in range(0,n):
        print('massa {a}: frequencia: {b} periodo: {c}'.format(a=i+1,b=frequencia[i],c=periodo[i]))


def assignment_b():
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

    dt = 0.01

    print("amostra 1")
    t_array,x_array,y_array = get_points(dt,x_1,y_1)
    print_frequency(lamb,n)
    escolha = input("amostra 1: Deseja ver todos graficos juntos(1) ou sepado(2): ")
    if(escolha == "1"):
        plot_graphics(t_array,x_array,y_label = 'x(t)', x_label = 'time',label = "x")
        print("\n")
    else:
        print_separado(t_array,x_array)

    print("amostra 2")
    t_array,x_array,y_array = get_points(dt,x_2,y_2)
    print_frequency(lamb,n)
    escolha = input("amostra 2: Deseja ver todos graficos juntos(1) ou sepado(2): ")
    if(escolha == "1"):
        plot_graphics(t_array,x_array,y_label = 'x(t)', x_label = 'time',label = "x")
        print("\n")
    else:
        print_separado(t_array,x_array)



if __name__ == "__main__":
    assignment_b()
