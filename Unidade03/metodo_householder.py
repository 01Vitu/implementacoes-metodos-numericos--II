import math

def mat_mult(A, B):
    n = len(A)
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return C

def householder_tridiagonal(A):
    """Transforma uma matriz simétrica A em uma matriz tridiagonal T similar."""
    n = len(A)
    T = [linha[:] for linha in A]
    
    if n <= 2:
        return T

    for k in range(n - 2):
        # Extrai o vetor 'x' da coluna k, abaixo da diagonal principal
        x = [T[i][k] for i in range(k + 1, n)]
        norm_x = math.sqrt(sum(v**2 for v in x))
        
        if norm_x < 1e-12:
            continue
            
        # Define o sinal de alpha para evitar cancelamento catastrófico
        alpha = norm_x if x[0] >= 0 else -norm_x
        
        v = x[:]
        v[0] += alpha
        
        norm_v = math.sqrt(sum(val**2 for val in v))
        if norm_v < 1e-12:
            continue
            
        u = [val / norm_v for val in v]
        
        # Monta a submatriz de Householder (I - 2 * u * u^T)
        dim_sub = n - (k + 1)
        H_sub = [[0.0]*dim_sub for _ in range(dim_sub)]
        for i in range(dim_sub):
            for j in range(dim_sub):
                delta = 1.0 if i == j else 0.0
                H_sub[i][j] = delta - 2.0 * u[i] * u[j]
                
        # Embutindo a submatriz na matriz Identidade de tamanho N
        H_k = [[0.0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i <= k or j <= k:
                    H_k[i][j] = 1.0 if i == j else 0.0
                else:
                    H_k[i][j] = H_sub[i - (k + 1)][j - (k + 1)]
                    
        # Aplica a similaridade: T_novo = H_k * T_antigo * H_k
        T = mat_mult(mat_mult(H_k, T), H_k)
        
        # Força zeros absolutos onde a teoria garante que há zeros
        for i in range(k + 2, n):
            T[i][k] = 0.0
            T[k][i] = 0.0

    return T