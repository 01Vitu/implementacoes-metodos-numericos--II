def mat_vec_mult(A, x):
    n = len(A)
    y = [0.0] * n
    for i in range(n):
        y[i] = sum(A[i][j] * x[j] for j in range(n))
    return y

def max_abs_vetor(v):
    return max(v, key=abs)

def potencia_regular(A, tol=1e-7, max_iter=200):
    """Encontra o autovalor de MAIOR módulo."""
    n = len(A)
    x = [1.0] * n
    lambda_old = 0.0

    for iteracao in range(1, max_iter + 1):
        y = mat_vec_mult(A, x)
        lambda_new = max_abs_vetor(y)
        
        if abs(lambda_new) < 1e-12:
            return 0.0, x, iteracao

        x = [elem / lambda_new for elem in y]

        if abs(lambda_new - lambda_old) / abs(lambda_new) < tol:
            return lambda_new, x, iteracao
        
        lambda_old = lambda_new

    return lambda_new, x, max_iter