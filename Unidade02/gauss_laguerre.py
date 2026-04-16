def calcular_gauss_laguerre(f, n):
    # Tabela de pontos (t) e pesos (w) para Gauss-Laguerre
    match n:
        case 2:
            t = [0.585786437626905, 3.4142135623730954]
            w = [0.8535533905932737, 0.14644660940672624]
        case 3:
            t = [0.41577455678347913, 2.294280360279042, 6.289945082937478]
            w = [0.7110930099291731, 0.27851773356924076, 0.010389256501586133]
        case 4:
            t = [0.3225476896193923, 1.7457611011583467, 4.536620296921128, 9.395070912301133]
            w = [0.6031541043416333, 0.35741869243779995, 0.03888790851500541, 0.0005392947055613295]
        case _:
            raise ValueError("Número de pontos não suportado (implementado apenas para 2, 3 e 4 pontos).")
            
    soma = 0.0
    
    # Laço para calcular o somatório
    for i in range(n):
        soma += w[i] * f(t[i])
        
    return soma