#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

from householder_method.householder_algorithm import householder_algorithm
from QR_method.QR_algorithm import QR_algorithm

A = 1/10 #m²
E = 200*(10**(9)) #Pa
NUM_TRE = 28
DENSIDADE = 7.8*(10**(3)) #kg/m³

PATH = "src/ep2/inputs/input-c"

class Beam:
    def __init__(self,no1,no2,ang,lenght):
        self.no1 = no1
        self.no2 = no2
        self.ang = ang*np.pi/180
        self.lenght = lenght
        self.A = A
        self.E = E
        self.dens = DENSIDADE

        self.massa = 0
        self.K = 0

        self.make_k_matrix()
        self.find_mass()

    def __str__(self):
        return 'no1 ={no_1}, no2 ={no_2}, ang ={ang}, lenght ={lenght}'.format(no_1=self.no1,no_2=self.no2,ang=self.ang,lenght=self.lenght)

    def make_k_matrix(self):
        x = (self.A*self.E)/self.lenght
        C = np.cos(self.ang)
        S = np.sin(self.ang)
        matrix = np.array([ [C**2,C*S,-(C**2),-C*S],
                            [C*S,S**2,-C*S,-(S**2)  ],
                            [-(C**2),-C*S,C**2,C*S],
                            [-C*S,-(S**2),C*S,S**2]],dtype=float)
        self.K = x*matrix

    def find_mass(self):
        self.mass = self.A*self.lenght*self.dens
        pass

    def get_K(self):
        return self.K

    def get_mass(self):
        return self.mass

def read_input_c():
    file_information = open(PATH,"r").read()
    file_information = file_information.split("\n")
    for i in range(0,2):
        file_information.pop(0) #pop main information
    matrix_len = len(file_information)
    for i in range(0,matrix_len):
        file_information[i] = file_information[i].split(" ")
        m = len(file_information[i])
        for j in range(0,m):
            if ((file_information[i])[j] != ""):
                (file_information[i])[j] = float((file_information[i])[j])
    return file_information

def make_total_k_matrix(V):
    m = len(V)
    k_matrix = np.zeros((m,m),dtype=float)
    for i in range (0,m):
        aux_k = V[i].get_K()
        i_pos = int(2*(V[i].no1) - 1)
        j_pos = int(2*(V[i].no2) - 1)
        k_matrix[(i_pos-1),(i_pos-1)] += aux_k[0,0]
        k_matrix[(i_pos-1),(i_pos)]   += aux_k[0,1]
        k_matrix[(i_pos-1),(j_pos-1)] += aux_k[0,2]
        k_matrix[(i_pos-1),(j_pos)]   += aux_k[0,3]
        k_matrix[(i_pos),  (i_pos-1)] += aux_k[1,0]
        k_matrix[(i_pos),  (i_pos)]   += aux_k[1,1]
        k_matrix[(i_pos),  (j_pos-1)] += aux_k[1,2]
        k_matrix[(i_pos),  (j_pos)]   += aux_k[1,3]
        k_matrix[(j_pos-1),(i_pos-1)] += aux_k[2,0]
        k_matrix[(j_pos-1),(i_pos)]   += aux_k[2,1]
        k_matrix[(j_pos-1),(j_pos-1)] += aux_k[2,2]
        k_matrix[(j_pos-1),(j_pos)]   += aux_k[2,3]
        k_matrix[(j_pos),  (i_pos-1)] += aux_k[3,0]
        k_matrix[(j_pos),  (i_pos)]   += aux_k[3,1]
        k_matrix[(j_pos),  (j_pos-1)] += aux_k[3,2]
        k_matrix[(j_pos),  (j_pos)]   += aux_k[3,3]
    for i in range(m-1,m-5,-1):
        k_matrix = np.delete(k_matrix,i,0)
        k_matrix = np.delete(k_matrix,i,1)
    return k_matrix

def make_M_matrix(V):
    n = len(V)
    m_matrix = np.zeros((n,n),dtype=float)
    for i in range(0,n):
        pos1 = int(2*(V[i].no1) - 1)
        pos2 = int(2*(V[i].no2) - 1)
        massa = V[i].get_mass()

        m_matrix[pos1 - 1,pos1 - 1] += massa/2
        m_matrix[pos1,pos1] += massa/2
        m_matrix[pos2 - 1,pos2 - 1] += massa/2
        m_matrix[pos2,pos2] += massa/2

    for i in range(n-1,n-5,-1):
        m_matrix = np.delete(m_matrix,i,0)
        m_matrix = np.delete(m_matrix,i,1)
    return m_matrix

def inv_diagonal_matrix(matrix):
    diagonal = np.diagonal(matrix)
    if (len(np.where(diagonal == 0)[0]) == 0):
        diagonal = 1/diagonal
        matrix_inv = np.diag(diagonal)
        return matrix_inv
    else:
        print("erro inv_diagonal_matrix")

def assignment_2():
    np.set_printoptions(precision=6,threshold=5) #print options

    info = read_input_c() #read file and get the informations
    beams = np.array([])

    beams = np.array([Beam(info[i][0],info[i][1],info[i][2],info[i][3]) for i in range(0,NUM_TRE)]) #create beams objects

    K = make_total_k_matrix(beams)
    M = make_M_matrix(beams)
    inv_sqrt_m = inv_diagonal_matrix(np.sqrt(M))
    K_til = inv_sqrt_m@K@inv_sqrt_m

    build_diagonal_matrix = lambda matrix: QR_algorithm(householder_algorithm(matrix))
    y_vector,w_vector,ite = build_diagonal_matrix(K_til)

    w_vector = np.sqrt(np.diagonal(w_vector))
    z_vector = inv_sqrt_m@y_vector

    f_vector = (w_vector)/(2*np.pi)
    x_vector = lambda t: z_vector*np.cos(w_vector*t)

    #print("y_vector = \n",y_vector,"\n")
    #print("f_vector = \n",f_vector,"\n")
    #print("z_vector = \n",z_vector,"\n")
    #print("x_vector(0) = \n",x_vector(0),"\n")
    #test_matrix_values(np.diag(f_vector))
    len_f = len(f_vector)
    len_w = len(w_vector)
    print("menores frequencias = ", f_vector[len_f-5:len_f])
    print("menores frequencias angulares = ", w_vector[len_w-5:len_w])

def test_class_beam():
    info = read_input_c()
    beams = np.array([Beam(info[i][0],info[i][1],info[i][2],info[i][3]) for i in range(0,NUM_TRE)])
    for i in range(0,NUM_TRE):
        print(beams[i]," massa =",beams[i].get_mass())

def test_matrix_values(K):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect('equal')
    plt.imshow(K)
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    try:
        assignment_2()

    except KeyboardInterrupt:
        print("\n Better luck next time")
