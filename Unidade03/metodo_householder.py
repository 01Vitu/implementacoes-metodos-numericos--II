import math

def mat_mult(A, B):
    n = len(A)
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return C

def householder_tridiagonal(A):
    """
    Transforma uma matriz simétrica A em uma matriz tridiagonal T similar.
    Retorna (T, H), onde H é a matriz acumulada H = H_1 * H_2 * ... * H_{n-2}.
    Seguindo o algoritmo 3.1.1 e 3.1.3.4 com vetores w, w', N, n.
    """
    n = len(A)
    T = [linha[:] for linha in A]
    
    # Inicializa H como a matriz Identidade (Step 3.1.1)
    H = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    
    if n <= 2:
        return T, H

    for k in range(n - 2):
        # --- Algoritmo 3.1.3.4 (Construção de H_k) ---
        w = [0.0] * n
        w_prime = [0.0] * n
        
        # Copiar elementos abaixo da diagonal da coluna k
        for i in range(k + 1, n):
            w[i] = T[i][k]
            
        # Lw = ||w||
        norm_w = math.sqrt(sum(val**2 for val in w))
        if norm_w < 1e-12:
            continue
            
        # Para evitar cancelamento catastrófico, ajustamos o sinal de w_prime[k+1]
        sinal_estavel = 1.0 if w[k + 1] >= 0 else -1.0
        w_prime[k + 1] = -sinal_estavel * norm_w
        
        # N = w - w'
        N = [w[i] - w_prime[i] for i in range(n)]
        
        # Normalizar N para obter n_vetor
        norm_N = math.sqrt(sum(val**2 for val in N))
        if norm_N < 1e-12:
            continue
        n_vetor = [val / norm_N for val in N]
        
        # Montar a matriz H_k = I - 2 * n_vetor * n_vetor^T
        H_k = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                delta = 1.0 if i == j else 0.0
                H_k[i][j] = delta - 2.0 * n_vetor[i] * n_vetor[j]
                
        # Transformação de similaridade: T = H_k * T * H_k
        T = mat_mult(mat_mult(H_k, T), H_k)
        
        # Acumular o produto das matrizes H: H = H * H_k
        H = mat_mult(H, H_k)

    # Forçar zeros absolutos na tridiagonal onde a teoria garante
    for k in range(n - 2):
        for i in range(k + 2, n):
            T[i][k] = 0.0
            T[k][i] = 0.0

    return T, H