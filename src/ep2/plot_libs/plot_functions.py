#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
color_array = np.array(["blue","green","red","cyan","magenta","yellow","black","blue","green","red","cyan","magenta","yellow","black"])

def plot_all_together(t_array,x_array):
    quantity_graphics = len(x_array)

    plt.xlim(min(t_array), max(t_array))
    #plt.ylim(min(x_array[i]), max(x_array[i]))
    for i in range(0,quantity_graphics,1):
        plt.plot(t_array,x_array[i],label='nó {a}'.format(a=i+1),color=color_array[i])
    plt.ylabel('x(t)')
    plt.xlabel('time(s)')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2, frameon=False)
    plt.show()
    pass

def plot_graphics(t_array,y_array,y_label = 'frequency',x_label = 'time',label = "x"):
    quantity_graphics = len(y_array)
    fig, axs = plt.subplots(quantity_graphics)
    for i in range(0,quantity_graphics,1):
        axs[i].plot(t_array,y_array[i],label='{la}{it}'.format(it = i,la = label),color=color_array[i])
        axs[i].set_title('{la}{it}'.format(it = i,la = label))
        axs[i].set_ylabel(y_label)
        axs[i].set_xlabel(x_label)
    plt.show()

def print_separado(t_array,x_array):
    quantity_graphics = len(x_array)
    for i in range(0,quantity_graphics,1):
        plt.xlim(min(t_array), max(t_array))
        plt.ylim(min(x_array[i]), max(x_array[i]))

        plt.plot(t_array,x_array[i],label='nó {a}'.format(a=i+1),color=color_array[i])
        plt.ylabel('x(t)')
        plt.xlabel('time(s)')

        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2, frameon=False)
        plt.show()

def get_points(dt,y,pos,time=10):
    t_array = np.array([])

    n = len(y(0,pos))
    y_array = np.zeros(shape = [n,1], dtype = float)

    for t in np.arange(0,time,dt):
        t_array = np.append(t_array,t)
        y_array = np.append(y_array,y(t,pos),axis = 1)

    y_array = np.delete(y_array,0,1)
    #print(y_array)
    #print(y(t,pos))
    return [t_array,y_array]

def test_matrix_values(K):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect('equal')
    plt.imshow(K)
    plt.colorbar()
    plt.show()
