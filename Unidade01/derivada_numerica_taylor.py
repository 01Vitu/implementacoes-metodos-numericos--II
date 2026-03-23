import numpy as np
import math

def derivada_numerica_taylor(f, x, h, filosofia, p, n):
    """
    Calcula a derivada numérica genérica de uma função.
    
    Parâmetros:
    f         : Função matemática (ex: np.sin)
    x         : Ponto onde a derivada será avaliada
    h         : Tamanho do passo
    filosofia : 'fw' (Forward), 'bw' (Backward), ou 'central'
    p         : Ordem da derivada (ex: 2 para derivada segunda)
    n         : Ordem do erro de truncamento (ex: 4 para erro O(h^4))
    
    Retorna:
        Derivada numérica
    """
    
    # 1/2. Determina a quantidade e os índices dos pontos baseado na filosofia
    match filosofia:
        case 'ct':
            num_pontos = p + n - 1
            if num_pontos % 2 == 0:
                num_pontos += 1
            m = num_pontos // 2
            pontos = np.arange(-m, m + 1)
        
        case 'fw':
            num_pontos = p + n
            pontos = np.arange(0, num_pontos)
        
        case 'bw':
            num_pontos = p + n
            pontos = np.arange(0, -num_pontos, -1)
        
        case _:
            raise ValueError("Filosofia inválida! Escolha 'fw', 'bw' ou 'ct'.")

    # 3. Monta o sistema linear (Matriz de Vandermonde)
    A = np.zeros((num_pontos, num_pontos))
    B = np.zeros(num_pontos)
    
    for k in range(num_pontos):
        A[k, :] = pontos ** k
        
    # Na série de Taylor, a derivada 'p' que queremos isolar está dividida por p!
    B[p] = math.factorial(p)
    
    # 4. Resolve o sistema para encontrar os coeficientes (A, B, C, D, E...)
    coeficientes = np.linalg.solve(A, B)
    
    # 5. Aplica a combinação linear (Multiplica os coeficientes pela função nos pontos)
    soma = 0
    for i in range(num_pontos):
        soma += coeficientes[i] * f(x + pontos[i] * h)
        
    # 6. Divide tudo por h^p 
    derivada = soma / (h ** p)
    
    return derivada
