import numpy as np

def refinement(A,L,U,b,x0,alg_sig,print_res=False):
    r = []
    r.append(b - np.matmul(A,x))
    a = np.round(np.matmul(L,U),1)
    m_len = len(A)
    P_array = np.full((m_len,m_len), 0, dtype=int)
    for i in range(0, m_len):
        for j in range(0, m_len):
            if (np.all(A[j] == a[i])):
                P_array[j,i] = 1
    y = np.linalg.solve(L,np.matmul(P_array,r[0]))
    c = np.linalg.solve(U,y)
    c = np.round(c ,alg_sig)
    x_1 = x0 + c
    if (print_res == True):
        print (x_1)
    return x_1

#exemple 1:
A = np.array([[3,-1,1],[-1,3,1],[1,3,3]])
L = np.array([[1,0,0],[0.33,1,0],[-0.33,0.82,1]])
U = np.array([[3,-1,1],[0,3.3,2.7],[0,0,-0.9]])
b = np.array([1,2,1])
x = np.array([1.6,1.8,-2])
refinement(A,L,U,b,x,2, True)

#exemple 2:
A = np.array([[-5.9,9.6,-8.4],[-9.9,-2.1,5.6],[5.1,-6.6,6.0]])
L = np.array([[1,0,0],[0.596,1,0],[-0.515,-0.705,1]])
U = np.array([[-9.9,-2.1,5.6],[0,10.9,-11.7],[0,0,0.63]])
b = np.array([-84.4,-38.7,68])
x = np.array([7.74,2.72,7.78])
refinement(A,L,U,b,x,3,True)
