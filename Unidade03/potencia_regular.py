import math

def mat_vec_mult(A, x):
    n = len(A)
    y = [0.0] * n
    for i in range(n):
        y[i] = sum(A[i][j] * x[j] for j in range(n))
    return y

def produto_escalar(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))

def norma_l2(v):
    return math.sqrt(produto_escalar(v, v))

def potencia_regular(A, v0=None, tol=1e-7, max_iter=200):
    """Encontra o autovalor dominante e o autovetor correspondente 
    seguindo o Algoritmo 1 (Norma L2 e Quociente de Rayleigh)."""
    n = len(A)
    
    # Step 1 e 3: Receber vetor inicial (ou usar padrão de 1s caso seja None)
    v_novo = [1.0] * n if v0 is None else list(v0)
    lambda_novo = 0.0  # Step 2
    
    for iteracao in range(1, max_iter + 1):
        lambda_velho = lambda_novo  # Step 4
        v_velho = v_novo            # Step 5
        
        # Step 6: Normalizar v_velho com a norma Euclidiana (L2)
        norma = norma_l2(v_velho)
        if norma < 1e-12:
            return lambda_novo, v_velho, iteracao
        x_velho = [elem / norma for elem in v_velho]
        
        # Step 7: Calcular vetor não normalizado
        v_novo = mat_vec_mult(A, x_velho)
        
        # Step 8: Nova estimativa de lambda via produto escalar (Rayleigh)
        lambda_novo = produto_escalar(x_velho, v_novo)
        
        # Step 9: Verificar convergência relativa
        if abs(lambda_novo) > 1e-12:
            erro = abs((lambda_novo - lambda_velho) / lambda_novo)
        else:
            erro = abs(lambda_novo - lambda_velho)
            
        if erro < tol:
            return lambda_novo, x_velho, iteracao  # Step 10
            
    return lambda_novo, x_velho, max_iter
