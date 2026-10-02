import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    if np.prod(new_shape) != np.size(a):
        return []

    return np.reshape(a, new_shape).tolist()