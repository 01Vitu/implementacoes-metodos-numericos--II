def calcular_gauss_chebyshev(f, n):
    # Tabela de pontos (t) e pesos (w) para Gauss-Chebyshev
    match n:
        case 2:
            t = [-0.7071067811865475, 0.7071067811865476]
            # Os pesos em Chebyshev são sempre iguais a pi/n
            w = [1.5707963267948966, 1.5707963267948966]
        case 3:
            # 0.0 explícito no meio
            t = [-0.8660254037844387, 0.0, 0.8660254037844387]
            w = [1.0471975511965976, 1.0471975511965976, 1.0471975511965976]
        case 4:
            t = [-0.9238795325112867, -0.3826834323650897, 0.38268343236508984, 0.9238795325112867]
            w = [0.7853981633974483, 0.7853981633974483, 0.7853981633974483, 0.7853981633974483]
        case _:
            raise ValueError("Número de pontos não suportado (implementado apenas para 2, 3 e 4 pontos).")
            
    soma = 0.0
    
    # Laço para calcular o somatório
    for i in range(n):
        soma += w[i] * f(t[i])
        
    return soma