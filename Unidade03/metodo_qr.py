import math

def mat_mult(A, B):
    n = len(A)
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return C

def decomposicao_qr_mgs(A):
    """Decomposição A = Q*R usando Gram-Schmidt Modificado (estável)."""
    n = len(A)
    Q = [[0.0]*n for _ in range(n)]
    R = [[0.0]*n for _ in range(n)]
    
    # Trabalhar com colunas é mais fácil: V[j] é a j-ésima coluna de A
    V = [[A[i][j] for i in range(n)] for j in range(n)]
    U = [[0.0]*n for _ in range(n)]
    
    for i in range(n):
        u_i = V[i][:]
        for j in range(i):
            r_ji = sum(V[i][k] * U[j][k] for k in range(n))
            R[j][i] = r_ji
            for k in range(n):
                u_i[k] -= r_ji * U[j][k]
                
        norm_ui = math.sqrt(sum(x*x for x in u_i))
        R[i][i] = norm_ui
        
        if norm_ui > 1e-12:
            U[i] = [x / norm_ui for x in u_i]
        else:
            U[i] = [0.0]*n
            
    for i in range(n):
        for j in range(n):
            Q[i][j] = U[j][i]
            
    return Q, R

def algoritmo_qr(A, tol=1e-7, max_iter=1000):
    """Aplica iterações Ak+1 = Rk * Qk até a matriz virar triangular superior."""
    n = len(A)
    Ak = [linha[:] for linha in A]
    
    for iteracao in range(1, max_iter + 1):
        Q, R = decomposicao_qr_mgs(Ak)
        Ak = mat_mult(R, Q)  # O milagre matemático acontece nessa inversão
        
        # Soma de todos os elementos fora da diagonal principal
        erro = sum(abs(Ak[i][j]) for i in range(n) for j in range(n) if i != j)
        if erro < tol:
            break
            
    # Os autovalores repousam na diagonal principal
    autovalores = sorted([Ak[i][i] for i in range(n)], reverse=True)
    return autovalores, iteracao