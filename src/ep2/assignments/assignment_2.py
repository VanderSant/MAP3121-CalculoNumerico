#!/usr/bin/env python3
# coding=utf-8

import numpy as np

P = 7.8*(10**(3)) #kg/m³
A = 1/10 #m²
E = 200*(10**(9)) #Pa
L = 10 #m
D = 20 #m
NUM_TRE = 28

PATH = "src/ep2/inputs/input-c"

class Beam:
    def __init__(self,no1,no2,ang,lenght):
        self.no1 = no1
        self.no2 = no2
        self.ang = ang*np.pi/180
        self.lenght = lenght
        self.A = A
        self.E = E

        self.K = 0
        self.make_k_matrix()

    def make_k_matrix(self):
        x = (self.A*self.E)/self.lenght
        C = np.cos(self.ang)
        S = np.sin(self.ang)
        matrix = np.array([ [C**2,C*S,-(C**2),-C*S],
                            [C*S,S**2,-C*S,-S**2],
                            [-(C**2),-C*S,C**2,C*S],
                            [-C*S,-(C**2),C*S,S**2]],dtype=float)
        self.K = x*matrix

    def get_K(self):
        return self.K

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

def make_total_K_matrix(V):
    K = np.zeros(24)
    for i in range (0,len(V)):
        # Jeito completamente corno kkkkkkkk mas não encontrei nenhum padrão, da uma olhadinha no enunciado
        # Ta mais pra pseudocódigo pq n sei exatamente como acessa os valores haha
        # Vou comer aqui, aí ja volto

        #KKKKKKKKKKKKKKKKk vou olhar
        aux_k = V[i].get_K()
        K[2*(V[i].no1)-1,2*(V[i].no1)-1] += aux_k[1,1]
        K[2*(V[i].no1)-1,2*(V[i].no1)] += aux_k[1,2]
        K[2*(V[i].no1)-1,2*(V[i].no2)-1] += aux_k[1,3]
        K[2*(V[i].no1)-1,2*(V[i].no2)] += aux_k[1,4]
        K[2*(V[i].no1),2*(V[i].no1)-1] += aux_k[2,1]
        K[2*(V[i].no1),2*(V[i].no1)] += aux_k[2,2]
        K[2*(V[i].no1),2*(V[i].no2)-1] += aux_k[2,3]
        K[[2*(V[i].no1),2*(V[i].noj)]] += aux_k[2,4]
        K[2*(V[i].no2)-1,2*(V[i].no1)-1] += aux_k[3,1]
        K[2*(V[i].no2)-1,2*(V[i].no1)] += aux_k[3,2]
        K[2*(V[i].no2)-1,2*(V[i].no2)-1] += aux_k[3,3]
        K[2*(V[i].no2)-1,2*(V[i].no2)] += aux_k[3,4]
        K[2*(V[i].no2),2*(V[i].no1)-1] += aux_k[4,1]
        K[2*(V[i].no2),2*(V[i].no1)] += aux_k[4,2]
        K[2*(V[i].no2),2*(V[i].no2)-1] += aux_k[4,3]
        K[2*(V[i].no2),2*(V[i].no2)] += aux_k[4,4]

def assignment_2():
    file_info = read_input_c()
    print(file_info)
    beams = np.array([])
    for i in range(0,NUM_TRE):
        info = file_info[i]
        beams = np.append(beams,Beam(info[0],info[1],info[2],info[3]))
    print(beams[0].get_K())

if __name__ == "__main__":
    try:
        assignment_2()

    except KeyboardInterrupt:
        print("\n Better luck next time")
