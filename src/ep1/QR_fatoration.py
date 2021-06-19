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
    pass

## Function which returns a matrix after a givens rotation
def QR_fatoration(A):
    R = A
    matrix_i_size = len(A)
    Q =np.eye(matrix_i_size)
    Q_iteration_size = matrix_i_size - 1
    for i in range (0, Q_iteration_size,1):
        Q = Q@np.transpose(givens_rotation_Qk(i,R))
        R = givens_rotation_Qk(i,R)@R
        R = np.matrix.round(R,5)
    return [R,Q]
    pass

#exemple 1:
A = np.array([[2,1,0,0],
              [1,2,1,0],
              [0,1,2,1],
              [0,0,1,2]])
R = QR_fatoration(A)[0]
Q = QR_fatoration(A)[1]
print("R = ", R)
print("Q = ", Q)
