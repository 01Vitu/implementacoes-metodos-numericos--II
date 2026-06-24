import math

def produto_escalar(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))

def norma_l2(v):
    return math.sqrt(produto_escalar(v, v))

def decomp_lu(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        L[i][i] = 1.0
        
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
            
        for j in range(i + 1, n):
            if abs(U[i][i]) < 1e-12:
                raise ValueError("Pivô nulo ou muito próximo de zero na decomposição LU.")
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
            
    return L, U

def resolver_lu(L, U, b):
    n = len(L)
    # L y = b (substituição direta)
    y = [0.0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
        
    # U x = y (retrosubstituição)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        if abs(U[i][i]) < 1e-12:
            raise ValueError("Divisão por zero na retrosubstituição LU.")
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
        
    return x

def potencia_inversa(A, v0=None, tol=1e-7, max_iter=200):
    """Encontra o autovalor de menor módulo de A seguindo o Algoritmo 2.1b."""
    n = len(A)
    try:
        L, U = decomp_lu(A)
    except ValueError:
        return None, None, 0

    # Step 1 e 4: vetor inicial v0 (padrão de 1s se for None)
    v_novo = [1.0] * n if v0 is None else list(v0)
    lambda_bar_novo = 0.0  # Step 3

    for iteracao in range(1, max_iter + 1):
        lambda_bar_velho = lambda_bar_novo  # Step 5
        v_velho = v_novo                    # Step 6

        # Step 7: Normalizar L2
        norma = norma_l2(v_velho)
        if norma < 1e-12:
            return None, v_velho, iteracao
        x_velho = [elem / norma for elem in v_velho]

        # Step 8: Resolver LU
        try:
            v_novo = resolver_lu(L, U, x_velho)
        except ValueError:
            return None, x_velho, iteracao

        # Step 9: Estimativa do autovalor da inversa (Rayleigh)
        lambda_bar_novo = produto_escalar(x_velho, v_novo)

        # Step 10: Verificar convergência relativa
        if abs(lambda_bar_novo) > 1e-12:
            erro = abs((lambda_bar_novo - lambda_bar_velho) / lambda_bar_novo)
        else:
            erro = abs(lambda_bar_novo - lambda_bar_velho)

        if erro < tol:
            lambda_real = 1.0 / lambda_bar_novo  # Step 11
            return lambda_real, x_velho, iteracao  # Step 12 e 13

    lambda_real = 1.0 / lambda_bar_novo
    return lambda_real, x_velho, max_iter