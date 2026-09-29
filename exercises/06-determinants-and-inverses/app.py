import numpy as np

def determinant(matrix, mode="pure"):
    """
    Computes the determinant of a square matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to compute determinant.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The determinant value.
    """

    def _det(m):
        n = len(m)
        if n == 1:
            return m[0][0]
        if n == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        total = 0
        for col in range(n):
            minor = [row[:col] + row[col + 1:] for row in m[1:]]
            total += ((-1) ** col) * m[0][col] * _det(minor)
        return total

    if mode == "pure":
        return _det(matrix)
    elif mode == "numpy":
        return np.linalg.det(np.array(matrix))
    else:
        return f"Invalid mode: {mode}"

def inverse_matrix(matrix, mode="pure"):
    """
    Computes the inverse of a square matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to compute inverse.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The inverse matrix or a message if it doesn't exist.
    """

    def _det(m):
        n = len(m)
        if n == 1:
            return m[0][0]
        if n == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        total = 0
        for col in range(n):
            minor = [row[:col] + row[col + 1:] for row in m[1:]]
            total += ((-1) ** col) * m[0][col] * _det(minor)
        return total

    if mode == "pure":
        det = _det(matrix)
        if det == 0:
            return "Error: Matrix is not invertible (determinant is 0)"
        n = len(matrix)
        if n == 1:
            return [[1 / matrix[0][0]]]
        cofactors = []
        for i in range(n):
            cofactor_row = []
            for j in range(n):
                minor = [row[:j] + row[j + 1:] for k, row in enumerate(matrix) if k != i]
                cofactor_row.append(((-1) ** (i + j)) * _det(minor))
            cofactors.append(cofactor_row)
        adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
        return [[val / det for val in row] for row in adjugate]
    elif mode == "numpy":
        arr = np.array(matrix)
        det = np.linalg.det(arr)
        if abs(det) < 1e-10:
            return "Error: Matrix is not invertible (determinant is 0)"
        return np.linalg.inv(arr)
    else:
        return f"Invalid mode: {mode}"

matrix = [[1, 2], [3, 4]]

print("Determinant in pure Python:", determinant(matrix, "pure"))
print("Determinant in NumPy:", determinant(matrix, "numpy"))
print("Inverse matrix in pure Python:", inverse_matrix(matrix, "pure"))
print("Inverse matrix in NumPy:", inverse_matrix(matrix, "numpy"))
