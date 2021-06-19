import numpy as np

## Function to get the Qk matrix for givens rotation
def Qk(k,A):
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
    pass

## Function which returns a matrix after a givens rotation
def givens_rotations(A):
    R = A
    matrix_i_size = len(A)
    Q_iteration_size = matrix_i_size - 1
    for i in range (0, Q_iteration_size,1):
        print("matriz R:", R,"\n")
        print("matriz Q:", Qk(i,R),"\n")
        R = Qk(i,R)@R
        R = np.matrix.round(R,5)
    return R
    pass

#exemple 1:
A = np.array([[2,1,0,0],
              [1,2,1,0],
              [0,1,2,1],
              [0,0,1,2]])

print(givens_rotations(A))
