def max_abs_vetor(v):
    return max(v, key=abs)

def resolver_sistema_gauss(A_orig, b_orig):
    n = len(A_orig)
    A = [linha[:] for linha in A_orig]
    b = b_orig[:]

    for i in range(n):
        pivo_max = abs(A[i][i])
        linha_pivo = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > pivo_max:
                pivo_max = abs(A[k][i])
                linha_pivo = k
        
        if pivo_max < 1e-12:
            raise ValueError("Matriz singular ou mal condicionada.")

        A[i], A[linha_pivo] = A[linha_pivo], A[i]
        b[i], b[linha_pivo] = b[linha_pivo], b[i]

        for k in range(i + 1, n):
            fator = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= fator * A[i][j]
            b[k] -= fator * b[i]

    y = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(A[i][j] * y[j] for j in range(i + 1, n))
        y[i] = (b[i] - soma) / A[i][i]
    return y

def potencia_inversa(A, tol=1e-7, max_iter=200):
    """Encontra o autovalor de MENOR módulo."""
    n = len(A)
    x = [1.0] * n
    mu_old = 0.0

    for iteracao in range(1, max_iter + 1):
        try:
            y = resolver_sistema_gauss(A, x)
        except ValueError:
            return None, None, iteracao

        mu_new = max_abs_vetor(y)
        x = [elem / mu_new for elem in y]

        if abs(mu_new - mu_old) / abs(mu_new) < tol:
            lambda_real = 1.0 / mu_new
            return lambda_real, x, iteracao
        
        mu_old = mu_new

    return 1.0 / mu_new, x, max_iter