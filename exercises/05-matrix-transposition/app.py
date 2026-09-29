import numpy as np  

def transpose(matrix, mode="pure"):
    """
    Computes the transpose of a matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to transpose.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The transposed matrix.
    """
   
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        return "Error: Invalid matrix - all rows must have the same length"
    if mode == "pure":
        result = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        return result
    elif mode == "numpy":
        return np.array(matrix).T
    else:
        return f"Invalid mode: {mode}"

matrix = [[1, 2, 3], [4, 5, 6]]

transpose_result_pure = transpose(matrix, "pure")
transpose_result_numpy = transpose(matrix, "numpy")

print("Transpose in pure Python:", transpose_result_pure)
print("Transpose in NumPy:", transpose_result_numpy)
