import numpy as np
from QR_fatoration import QR_fatoration


def get_sgnd(d):
    if (d >= 0):
        return 1
    elif (d < 0):
        return -1
    pass

def wilkinson_heuristics(A,n):
    alfa_ant = A[n-2,n-2]
    alfa = A[n-1,n-1]
    beta = A[(n-2)+1,n-2]
    dk = (alfa_ant - alfa)/2
    uk = alfa + dk - get_sgnd(dk)*(np.sqrt((dk**2)+(beta**2)))
    return [uk,beta]
    pass

def get_uk(A,n,k):
    if (k <= 0):
        return 0
    elif (k>0):
        return wilkinson_heuristics(A,n)[0]

def QR_algorithm(A, erro = 1/1000000):
    V = np.eye(len(A))
    I = np.eye(len(A))
    #R,Q = QR_fatoration(A)
    #A = R@Q
    #V = V@Q
    k = 0
    for n in range(len(A),1,-1):
        beta = wilkinson_heuristics(A,n)[1]
        print(beta)
        while(abs(beta)>erro):
            uk = get_uk(A,n,k)
            #print(uk)
            R,Q = QR_fatoration(A - (uk*I))
            A = R@Q + uk*I
            V = V@Q
            k = k + 1
            beta = wilkinson_heuristics(A,n)[1]
    lamb = A
    return [V,lamb]
    pass

A = np.array([[2,1,0,0],
              [1,2,1,0],
              [0,1,2,1],
              [0,0,1,2]])

print(QR_algorithm(A)[0])
#print(QR_algorithm(A)[1])
