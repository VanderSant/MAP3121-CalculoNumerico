#!/usr/bin/env python3
# coding=utf-8

import numpy as np

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
        return 'no1 ={no_1}, no2 ={no_2}, ang ={ang}, lenght ={lenght}\n'.format(no_1=self.no1,no_2=self.no2,ang=self.ang,lenght=self.lenght)

    def make_k_matrix(self):
        x = (self.A*self.E)/self.lenght
        C = np.cos(self.ang)
        S = np.sin(self.ang)
        matrix = np.array([ [C**2,C*S,-(C**2),-C*S],
                            [C*S,S**2,-C*S,-S**2  ],
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
    k_matrix = np.zeros((28,28),dtype=float)
    for i in range (0,len(V)):
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
    return k_matrix

def assignment_2():
    file_info = read_input_c()
    print(file_info,"\n")
    beams = np.array([])
    for i in range(0,NUM_TRE):
        info = file_info[i]
        beams = np.append(beams,Beam(info[0],info[1],info[2],info[3]))
    K = make_total_k_matrix(beams)
    print(K)

def test_class_beam():
    file_info = read_input_c()
    beams = np.array([])
    for i in range(0,NUM_TRE):
        info = file_info[i]
        beams = np.append(beams,Beam(info[0],info[1],info[2],info[3]))
    print(beams[0],"\n","massa =",beams[0].get_mass(),"\n",beams[0].get_K())

if __name__ == "__main__":
    try:
        assignment_2()

    except KeyboardInterrupt:
        print("\n Better luck next time")
