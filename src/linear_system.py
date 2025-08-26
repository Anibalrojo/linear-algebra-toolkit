import numpy as np
from numpy.typing import NDArray

def solve_linear_system(A: NDArray[np.float64], b: NDArray[np.float64]) -> tuple[NDArray[np.float64] | None, NDArray[np.float64]]:
    """Solves a linear system Ax = b using two different methods.

    This function compares the exact solution from `np.linalg.solve` with the 
    least-squares solution from `np.linalg.lstsq`.

    Args:
        A: The coefficient matrix of the system, shape (n, n).
        b: The result vector of the system, shape (n,).

    Returns:
        A tuple containing:
            - The exact solution if one exists, otherwise None.
            - The least-squares solution.
    """
    print("Coefficient Matrix A:\n", A)
    print("Vector b:\n", b)

    x_solve: NDArray[np.float64] | None = None
    try:
        x_solve = np.linalg.solve(A, b)
        print("\nSolution with np.linalg.solve:")
        print(x_solve)
    except np.linalg.LinAlgError as e:
        print("\nnp.linalg.solve failed:", e)

    # Least squares solution
    x_lstsq = np.linalg.lstsq(A, b, rcond=None)[0]
    print("\nSolution with np.linalg.lstsq (least squares):")
    print(x_lstsq)

    # Comparison
    if x_solve is not None:
        are_equal = np.allclose(x_solve, x_lstsq)
        print("\nAre both solutions equal?", "Yes" if are_equal else "No")
    else:
        print("\nOnly the least squares solution could be obtained.")

    return x_solve, x_lstsq
