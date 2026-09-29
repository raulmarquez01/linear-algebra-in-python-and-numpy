import numpy as np  

def solve_system(A, b, mode="numpy"):
    """
    Solves the linear system Ax = b.

    Parameters:
    - A: list of lists or np.array -> Coefficient matrix.
    - b: list or np.array -> Result vector.
    - mode: str -> "pure" for manual computation, "numpy" for np.linalg.solve().

    Returns:
    - The solution vector x.
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
        det = _det(A)
        if det == 0:
            return "Error: Matrix A is not invertible (determinant is 0)"
        n = len(A)
        if n == 1:
            return [b[0] / A[0][0]]
        cofactors = []
        for i in range(n):
            cofactor_row = []
            for j in range(n):
                minor = [row[:j] + row[j + 1:] for k, row in enumerate(A) if k != i]
                cofactor_row.append(((-1) ** (i + j)) * _det(minor))
            cofactors.append(cofactor_row)
        adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
        inverse = [[val / det for val in row] for row in adjugate]
        x = [sum(inverse[i][k] * b[k] for k in range(n)) for i in range(n)]
        return x
    elif mode == "numpy":
        arr = np.array(A, dtype=float)
        det = np.linalg.det(arr)
        if abs(det) < 1e-10:
            return "Error: Matrix A is not invertible (determinant is 0)"
        return np.linalg.solve(arr, b)
    else:
        return f"Invalid mode: {mode}"

A = [[2, 3], [4, -1]]
b = [5, 1]

print("Solution in pure Python:", solve_system(A, b, "pure"))
print("Solution in NumPy:", solve_system(A, b, "numpy"))
