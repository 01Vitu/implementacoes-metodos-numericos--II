from potencia_inverso import potencia_inversa

def potencia_deslocada(A, sigma, v0=None, tol=1e-7, max_iter=200):
    """Encontra o autovalor mais próximo de sigma seguindo o Algoritmo 2.2."""
    n = len(A)
    # Step 1: A_hat = A - sigma * I
    A_hat = [linha[:] for linha in A]
    for i in range(n):
        A_hat[i][i] -= sigma

    # Step 2: (lambda_hat, x_hat) = potenciaInverso(A_hat, v0, tol)
    lambda_hat, x_hat, it = potencia_inversa(A_hat, v0, tol, max_iter)

    if lambda_hat is None:
        return None, None, it

    # Step 3 e 4: lambda = lambda_hat + sigma
    lambda_real = lambda_hat + sigma
    return lambda_real, x_hat, it