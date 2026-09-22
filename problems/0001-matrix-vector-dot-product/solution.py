import  numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
 if len(a[0]) != len(b):
        return -1
 else:    
    matrix_dot_vector=np.dot(a, b) #[14, 25, 49]

 return matrix_dot_vector
matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3])