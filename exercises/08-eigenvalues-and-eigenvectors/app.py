import numpy as np  

def compute_eigen(A, mode="numpy"):
    """
    Computes the eigenvalues and eigenvectors of a square matrix.

    Parameters:
    - A: list of lists or np.array -> Square matrix.
    - mode: str -> "pure" for manual calculation, "numpy" for np.linalg.eig().

    Returns:
    - List of eigenvalues (and eigenvectors if mode="numpy").
    """
   
    n = len(A)
    for row in A:
        if len(row) != n:
            return "Error: Matrix A must be square"

    if mode == "pure":
        a, b = A[0]
        c, d = A[1]
        trace = a + d
        det = a * d - b * c
        discriminant = trace ** 2 - 4 * det
        sqrt_disc = discriminant ** 0.5
        lambda1 = (trace + sqrt_disc) / 2
        lambda2 = (trace - sqrt_disc) / 2
        return [lambda1, lambda2], None
    elif mode == "numpy":
        arr = np.array(A, dtype=float)
        eigenvalues, eigenvectors = np.linalg.eig(arr)
        order = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[order]
        eigenvectors = eigenvectors[:, order]
        return eigenvalues, eigenvectors
    else:
        return f"Invalid mode: {mode}"

A = [[3, 2], [1, 4]]

print("Eigenvalues in pure Python:", compute_eigen(A, "pure"))
print("Eigenvalues and eigenvectors in NumPy:", compute_eigen(A, "numpy"))
