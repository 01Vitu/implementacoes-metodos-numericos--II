import numpy as np
import math

def derivada_numerica_newton(f, x_alvo, h, filosofia, p, n):
    """
    Calcula a derivada numérica usando o Polinômio Interpolador de Newton.
    
    Parâmetros:
        f: Função a ser derivada
        x_alvo: Ponto onde a derivada será calculada
        h: Passo de aproximação
        filosofia: 'fw', 'bw' ou 'ct'
        p: Ordem da derivada
        n: Ordem do erro
    
    Retorna:
        Derivada numérica
    """
    
    # 1. Determina a quantidade e índices baseados na filosofia
    match filosofia:
        case 'ct':
            num_pontos = p + n - 1
            if num_pontos % 2 == 0:
                num_pontos += 1
            m = num_pontos // 2
            indices = np.arange(-m, m + 1)
            num_pontos = len(indices) # Atualizando o real num de pontos
        
        case 'fw':
            num_pontos = p + n
            indices = np.arange(0, num_pontos)
        
        case 'bw':
            num_pontos = p + n
            indices = np.arange(0, -num_pontos, -1)
        
        case _:
            raise ValueError("Filosofia inválida! Escolha 'fw', 'bw' ou 'ct'.")

    # 2. Obtém as coordenadas reais de X e Y para os nossos pontos
    X = x_alvo + indices * h
    Y = np.array([f(xi) for xi in X])
    
    # 3. Constrói a Tabela de Diferenças Divididas de Newton
    # DD é uma matriz onde a coluna 0 são os Ys, e as outras são as diferenças
    DD = np.zeros((num_pontos, num_pontos))
    DD[:, 0] = Y 
    
    for j in range(1, num_pontos):
        for i in range(num_pontos - j):
            # Fórmula da diferença dividida: f[x_i, ..., x_{i+j}]
            DD[i, j] = (DD[i+1, j-1] - DD[i, j-1]) / (X[i+j] - X[i])
            
    # Os coeficientes do Polinômio de Newton (c0, c1, c2...) ficam na primeira linha da matriz
    coeficientes = DD[0, :]
    
    # 4. Monta o polinômio P(x) = c0 + c1(x-x0) + c2(x-x0)(x-x1) + ...
    P_x = np.poly1d([0.0]) # Polinômio inicial P(x) = 0
    N_k = np.poly1d([1.0]) # Termo base N(x) = 1
    
    for k in range(num_pontos):
        # Adiciona o termo atual ( coef * N_k(x) ) ao polinômio final
        P_x = np.polyadd(P_x, coeficientes[k] * N_k)
        
        # Prepara o N_k para a próxima rodada multiplicando por (x - x_k)
        if k < num_pontos - 1:
            termo_raiz = np.poly1d([1.0, -X[k]]) # Representa o binômio (1*x - X[k])
            N_k = np.polymul(N_k, termo_raiz)
            
    # 5. Derivar o polinômio analiticamente 'p' vezes
    for _ in range(p):
        P_x = np.polyder(P_x)
        
    # 6. Avalia o polinômio derivado no ponto x_alvo
    derivada = P_x(x_alvo)
    
    return derivada