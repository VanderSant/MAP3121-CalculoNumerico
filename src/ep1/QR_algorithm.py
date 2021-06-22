import numpy as np
from QR_fatoration import QR_fatoration


def wilkinson_heuristics(A,n):
    get_sgnd = lambda d: 1 if d >= 0 else -1
    alfa_ant = A[n-2,n-2]
    alfa = A[n-1,n-1]
    beta = A[(n-2)+1,n-2]
    dk = (alfa_ant - alfa)/2
    uk = alfa + dk - get_sgnd(dk)*(np.sqrt((dk**2)+(beta**2)))
    return [uk,beta]
    pass

def QR_algorithm(A, erro = 1/1000000, spectral_shift = True):
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
    lamb = A
    return [V,lamb,k]
    pass


if __name__ == "__main__":
    #exemple 1:
    A = np.array([[2,1,0,0],
                [1,2,1,0],
                [0,1,2,1],
                [0,0,1,2]])
    print("test QR_algorithm with spectral_shift")
    V,lamb,k = QR_algorithm(A)
    print("V = ", V)
    print("lamb = ",lamb)
    print("k shift = ", k)
    new_A = V@lamb@np.transpose(V)
    new_A = np.matrix.round(new_A,3)
    print("\n")
    print("A = \n", A)
    print("V Λ V_transposto = \n", new_A)

    print("\n\n")

    print("test QR_algorithm without spectral_shift")
    V,lamb,k = QR_algorithm(A,spectral_shift = False)
    print("V = ", V)
    print("lamb = ",lamb)
    print("k = ", k)
    new_A = V@lamb@np.transpose(V)
    new_A = np.matrix.round(new_A,3)
    print("\n")
    print("A = \n", A)
    print("V Λ V_transposto = \n", new_A)
