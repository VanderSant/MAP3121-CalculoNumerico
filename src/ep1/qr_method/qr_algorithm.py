#!/usr/bin/env python3
# coding=utf-8

import numpy as np

## Function to get the givens_rotation_Qk matrix for givens rotation
def givens_rotation_Qk(k,A):
    Q = np.eye(len(A))
    alfa_k = A[k,k]
    beta_k = A[k+1,k]
    ck = alfa_k/(np.sqrt((alfa_k**2)+(beta_k**2)))
    sk = -(beta_k)/(np.sqrt((alfa_k**2)+(beta_k**2)))
    Q[k,k] = ck
    Q[k,k+1] = -sk
    Q[k+1,k] = sk
    Q[k+1,k+1] = ck
    return Q

## Function which returns a matrix after a givens rotation
def QR_fatoration(A):
    R = A
    matrix_i_size = len(A)
    Q =np.eye(matrix_i_size)
    Q_iteration_size = matrix_i_size - 1
    for i in range (0, Q_iteration_size,1):
        Q = Q@np.transpose(givens_rotation_Qk(i,R))
        R = givens_rotation_Qk(i,R)@R
    return [R,Q]

def wilkinson_heuristics(A,n):
    get_sgnd = lambda d: 1 if d >= 0 else -1
    alfa_ant = A[n-2,n-2]
    alfa = A[n-1,n-1]
    beta = A[(n-2)+1,n-2]
    dk = (alfa_ant - alfa)/2
    uk = alfa + dk - get_sgnd(dk)*(np.sqrt((dk**2)+(beta**2)))
    return [uk,beta]

def QR_algorithm(A, erro = 1/1000000, spectral_shift = True):
    round_parameter = len(str(int(1/erro)))
    get_uk = lambda A,n,k,spectral_shift: wilkinson_heuristics(A,n)[0] if ((k > 0) and (spectral_shift == True)) else 0
    V = I = np.eye(len(A))
    k = 0
    for m in range(len(A),1,-1):
        beta = wilkinson_heuristics(A,m)[1]
        while(abs(beta)>erro):
            uk = get_uk(A,m,k,spectral_shift)
            R,Q = QR_fatoration(A - (uk*I))
            A = R@Q + uk*I
            V = V@Q
            k = k + 1
            beta = wilkinson_heuristics(A,m)[1]
        A = np.matrix.round(A,round_parameter - 1)

    lamb = A
    return [V,lamb,k]

def test_qr_fatoration():
    #exemple 1:
    A = np.array([[2,1,0,0],
                [1,2,1,0],
                [0,1,2,1],
                [0,0,1,2]])

    R = QR_fatoration(A)[0]
    Q = QR_fatoration(A)[1]
    print("R = ", R)
    print("Q = ", Q)

def test_qr_algorithm():
    #exemple 1:
    A = np.array([[2,1,0,0],
                [1,2,1,0],
                [0,1,2,1],
                [0,0,1,2]])
    print("test QR_algorithm with spectral_shift")
    V,lamb,k = QR_algorithm(A)
    print("V = \n", V)
    print("lamb = \n",lamb)
    print("k shift = ", k)
    new_A = V@lamb@np.transpose(V)
    new_A = np.matrix.round(new_A,6)
    print("\n")
    print("A = \n", A)
    print("V Λ V_transposto = \n", new_A)

    print("\n\n")

    print("test QR_algorithm without spectral_shift")
    V,lamb,k = QR_algorithm(A,spectral_shift = False)
    print("V = \n", V)
    print("lamb = \n",lamb)
    print("k = ", k)
    new_A = V@lamb@np.transpose(V)
    new_A = np.matrix.round(new_A,6)
    print("\n")
    print("A = \n", A)
    print("V Λ V_transposto = \n", new_A)

if __name__ == "__main__":
    try:
        while True:
            test = input("Do you want to test the QR_algorithm(1) or QR_fatoration(0): ")
            if (test == "1"):
                test_qr_algorithm()
                print("\n")
            elif (test == "0"):
                test_qr_fatoration()
                print("\n")
            else:
                print("your input isn't valid \nplease, try again\n")

    except KeyboardInterrupt:
        print("\nBetter luck next time")
