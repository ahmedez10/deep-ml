import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    np_array = np.array(a)
    transposed_array = np_array.transpose()
    return transposed_array.tolist()
