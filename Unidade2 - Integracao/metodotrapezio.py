def metodo_trapezio(funcao, a, b, n, epsilon):
    h = (b - a) / n
    soma = 0.5 * (funcao(a) + funcao(b))
    for i in range(1, n):
        soma += funcao(a + i * h)
    resultado_anterior = soma * h
    
    while True:
        n *= 2 
        h = (b - a) / n
        soma = 0.5 * (funcao(a) + funcao(b))

        for i in range(1, n):
            soma += funcao(a + i * h)
        resultado_atual = soma * h

        if abs(resultado_atual - resultado_anterior) < epsilon:
            return resultado_atual, resultado_anterior, n
        
        resultado_anterior = resultado_atual


def f_primeiro_grau(x):
    return 2 * x + 3

atual, anterior, n_final = metodo_trapezio(f_primeiro_grau, 0, 3, 2, 0.001)

print(f"Resultado final: {atual:.6f}")
