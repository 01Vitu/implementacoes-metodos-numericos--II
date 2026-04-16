def calcular_gauss_hermite(f, n):
    # Tabela de pontos (t) e pesos (w) para Gauss-Hermite
    match n:
        case 2:
            t = [-0.7071067811865475, 0.7071067811865475]
            w = [0.8862269254527579, 0.8862269254527579]
        case 3:
            t = [-1.224744871391589, 0.0, 1.224744871391589]
            w = [0.2954089751509192, 1.1816359006036774, 0.2954089751509192]
        case 4:
            t = [-1.6506801238857842, -0.5246476232752904, 0.5246476232752904, 1.6506801238857842]
            w = [0.08131283544724505, 0.804914090005513, 0.804914090005513, 0.08131283544724505]
        case _:
            raise ValueError("Número de pontos não suportado (implementado apenas para 2, 3 e 4 pontos).")
            
    soma = 0.0
    
    # Laço para calcular o somatório
    for i in range(n):
        soma += w[i] * f(t[i])
        
    return soma