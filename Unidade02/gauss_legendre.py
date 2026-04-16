from math import sqrt

def calcular_gauss_legendre(f, a, b, n):
    # Tabela de pontos e pesos para Gauss-Legendre (n=1 a 4)
    match n:
        case 1:
            t = [0.0]
            w = [2.0]
        case 2:
            t = [-1/sqrt(3), 1/sqrt(3)]
            w = [1.0, 1.0]
        case 3:
            t = [-sqrt(3/5), 0.0, sqrt(3/5)]
            w = [5/9, 8/9, 5/9]
        case 4:
            # Valores aproximados para n=4
            t = [-0.8611363115940526, -0.3399810435848563, 0.3399810435848563, 0.8611363115940526]
            w = [0.3478548451374538, 0.6521451548625461, 0.6521451548625461, 0.3478548451374538]
        case _:
            raise ValueError("Número de pontos não suportado nesta versão (implementado apenas de 1 a 4).")
    
    dx = 0.5 * (b - a)
    soma = 0.0
    
    # Laço for para percorrer cada ponto e calcular o somatório da área
    for i in range(n):
        x_mapped = 0.5 * (b - a) * t[i] + 0.5 * (b + a)
        soma += w[i] * f(x_mapped)
        
    return soma * dx