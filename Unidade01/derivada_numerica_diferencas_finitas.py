import math

def derivada_numerica_diferencas_finitas(f, x, h, ordem_derivada, ordem_erro, filosofia):
    """
    Calcula a derivada numérica de uma função usando diferenças finitas.
    
    Parâmetros:
    f              : Função a ser derivada (callable)
    x              : Ponto onde a derivada será avaliada (float)
    h              : Tamanho do passo (float)
    ordem_derivada : 1 (Primeira derivada), 2 (Segunda derivada), 3 (Terceira derivada) ou 4 (Quarta derivada)
    ordem_erro     : 1 (O(h)), 2 (O(h²)), 3 (O(h³)) ou 4 (O(h⁴))
    filosofia : 'progressiva', 'regressiva' ou 'central'
    
    Retorna:
    float: O valor numérico da derivada.
    """
    
    match ordem_derivada:
        # ================================================================
        # 1ª DERIVADA
        # ================================================================
        case 1:
            match filosofia:
                case 'fw':
                    match ordem_erro:
                        case 1:
                            return (-f(x) + f(x + h)) / h
                        case 2:
                            return (-3*f(x) + 4*f(x + h) - f(x + 2*h)) / (2*h)
                        case 3:
                            return (-11*f(x) + 18*f(x + h) - 9*f(x + 2*h) + 2*f(x + 3*h)) / (6*h)
                        case 4:
                            return (-25*f(x) + 48*f(x + h) - 36*f(x + 2*h) + 16*f(x + 3*h) - 3*f(x + 4*h)) / (12*h)

                case 'bw':
                    match ordem_erro:
                        case 1:
                            return (f(x) - f(x - h)) / h
                        case 2:
                            return (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2*h)
                        case 3:
                            return (11*f(x) - 18*f(x - h) + 9*f(x - 2*h) - 2*f(x - 3*h)) / (6*h)
                        case 4:
                            return (25*f(x) - 48*f(x - h) + 36*f(x - 2*h) - 16*f(x - 3*h) + 3*f(x - 4*h)) / (12*h)

                case 'ct':
                    match ordem_erro:
                        case 1:
                            return (f(x + h) - f(x - h)) / (2*h)
                        case 2:
                            return (f(x + h) - f(x - h)) / (2*h)
                        case 3:
                            return (f(x - 2*h) - 8*f(x - h) + 8*f(x + h) - f(x + 2*h)) / (12*h)
                        case 4:
                            return (f(x - 2*h) - 8*f(x - h) + 8*f(x + h) - f(x + 2*h)) / (12*h)

        # ================================================================
        # 2ª DERIVADA
        # ================================================================
        case 2:
            match filosofia:
                case 'fw':
                    match ordem_erro:
                        case 1:
                            return (f(x) - 2*f(x + h) + f(x + 2*h)) / (h**2)
                        case 2:
                            return (2*f(x) - 5*f(x + h) + 4*f(x + 2*h) - f(x + 3*h)) / (h**2)
                        case 3:
                            return (35*f(x) - 104*f(x + h) + 114*f(x + 2*h) - 56*f(x + 3*h) + 11*f(x + 4*h)) / (12 * h**2)
                        case 4:
                            return (45*f(x) - 154*f(x + h) + 214*f(x + 2*h) - 156*f(x + 3*h) + 61*f(x + 4*h) - 10*f(x + 5*h)) / (12 * h**2)

                case 'bw':
                    match ordem_erro:
                        case 1:
                            return (f(x) - 2*f(x - h) + f(x - 2*h)) / (h**2)
                        case 2:
                            return (2*f(x) - 5*f(x - h) + 4*f(x - 2*h) - f(x - 3*h)) / (h**2)
                        case 3:
                            return (35*f(x) - 104*f(x - h) + 114*f(x - 2*h) - 56*f(x - 3*h) + 11*f(x - 4*h)) / (12 * h**2)
                        case 4:
                            return (45*f(x) - 154*f(x - h) + 214*f(x - 2*h) - 156*f(x - 3*h) + 61*f(x - 4*h) - 10*f(x - 5*h)) / (12 * h**2)

                case 'ct':
                    match ordem_erro:
                        case 1:
                            return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)
                        case 2:
                            return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)
                        case 3:
                            return (-f(x + 2*h) + 16*f(x + h) - 30*f(x) + 16*f(x - h) - f(x - 2*h)) / (12 * h**2)
                        case 4:
                            return (-f(x + 2*h) + 16*f(x + h) - 30*f(x) + 16*f(x - h) - f(x - 2*h)) / (12 * h**2)

        # ================================================================
        # 3ª DERIVADA
        # ================================================================
        case 3:
            match filosofia:
                case 'fw':
                    match ordem_erro:
                        case 1:
                            return (-f(x) + 3*f(x + h) - 3*f(x + 2*h) + f(x + 3*h)) / (h**3)
                        case 2:
                            return (-5*f(x) + 18*f(x + h) - 24*f(x + 2*h) + 14*f(x + 3*h) - 3*f(x + 4*h)) / (2 * h**3)
                        case 3:
                            return (-17*f(x) + 71*f(x + h) - 118*f(x + 2*h) + 98*f(x + 3*h) - 41*f(x + 4*h) + 7*f(x + 5*h)) / (4 * h**3)
                        case 4:
                            return (-49*f(x) + 232*f(x + h) - 461*f(x + 2*h) + 496*f(x + 3*h) - 307*f(x + 4*h) + 104*f(x + 5*h) - 15*f(x + 6*h)) / (8 * h**3)

                case 'bw':
                    match ordem_erro:
                        case 1:
                            return (f(x) - 3*f(x - h) + 3*f(x - 2*h) - f(x - 3*h)) / (h**3)
                        case 2:
                            return (5*f(x) - 18*f(x - h) + 24*f(x - 2*h) - 14*f(x - 3*h) + 3*f(x - 4*h)) / (2 * h**3)
                        case 3:
                            return (17*f(x) - 71*f(x - h) + 118*f(x - 2*h) - 98*f(x - 3*h) + 41*f(x - 4*h) - 7*f(x - 5*h)) / (4 * h**3)
                        case 4:
                            return (49*f(x) - 232*f(x - h) + 461*f(x - 2*h) - 496*f(x - 3*h) + 307*f(x - 4*h) - 104*f(x - 5*h) + 15*f(x - 6*h)) / (8 * h**3)

                case 'ct':
                    match ordem_erro:
                        case 1:
                            return (-f(x - 2*h) + 2*f(x - h) - 2*f(x + h) + f(x + 2*h)) / (2 * h**3)
                        case 2:
                            return (-f(x - 2*h) + 2*f(x - h) - 2*f(x + h) + f(x + 2*h)) / (2 * h**3)
                        case 3:
                            return (f(x - 3*h) - 8*f(x - 2*h) + 13*f(x - h) - 13*f(x + h) + 8*f(x + 2*h) - f(x + 3*h)) / (8 * h**3)
                        case 4:
                            return (f(x - 3*h) - 8*f(x - 2*h) + 13*f(x - h) - 13*f(x + h) + 8*f(x + 2*h) - f(x + 3*h)) / (8 * h**3)

        # ================================================================
        # 4ª DERIVADA
        # ================================================================
        case 4:
            match filosofia:
                case 'fw':
                    match ordem_erro:
                        case 1:
                            return (f(x) - 4*f(x + h) + 6*f(x + 2*h) - 4*f(x + 3*h) + f(x + 4*h)) / (h**4)
                        case 2:
                            return (3*f(x) - 14*f(x + h) + 26*f(x + 2*h) - 24*f(x + 3*h) + 11*f(x + 4*h) - 2*f(x + 5*h)) / (h**4)
                        case 3:
                            return (35*f(x) - 186*f(x + h) + 411*f(x + 2*h) - 484*f(x + 3*h) + 321*f(x + 4*h) - 114*f(x + 5*h) + 17*f(x + 6*h)) / (6 * h**4)
                        case 4:
                            return (56*f(x) - 333*f(x + h) + 852*f(x + 2*h) - 1219*f(x + 3*h) + 1056*f(x + 4*h) - 555*f(x + 5*h) + 164*f(x + 6*h) - 21*f(x + 7*h)) / (6 * h**4)

                case 'bw':
                    match ordem_erro:
                        case 1:
                            return (f(x) - 4*f(x - h) + 6*f(x - 2*h) - 4*f(x - 3*h) + f(x - 4*h)) / (h**4)
                        case 2:
                            return (3*f(x) - 14*f(x - h) + 26*f(x - 2*h) - 24*f(x - 3*h) + 11*f(x - 4*h) - 2*f(x - 5*h)) / (h**4)
                        case 3:
                            return (35*f(x) - 186*f(x - h) + 411*f(x - 2*h) - 484*f(x - 3*h) + 321*f(x - 4*h) - 114*f(x - 5*h) + 17*f(x - 6*h)) / (6 * h**4)
                        case 4:
                            return (56*f(x) - 333*f(x - h) + 852*f(x - 2*h) - 1219*f(x - 3*h) + 1056*f(x - 4*h) - 555*f(x - 5*h) + 164*f(x - 6*h) - 21*f(x - 7*h)) / (6 * h**4)

                case 'ct':
                    match ordem_erro:
                        case 1:
                            return (f(x + 2*h) - 4*f(x + h) + 6*f(x) - 4*f(x - h) + f(x - 2*h)) / (h**4)
                        case 2:
                            return (f(x + 2*h) - 4*f(x + h) + 6*f(x) - 4*f(x - h) + f(x - 2*h)) / (h**4)
                        case 3:
                            return (-f(x + 3*h) + 12*f(x + 2*h) - 39*f(x + h) + 56*f(x) - 39*f(x - h) + 12*f(x - 2*h) - f(x - 3*h)) / (6 * h**4)
                        case 4:
                            return (-f(x + 3*h) + 12*f(x + 2*h) - 39*f(x + h) + 56*f(x) - 39*f(x - h) + 12*f(x - 2*h) - f(x - 3*h)) / (6 * h**4)

    # Caso a combinação não esteja mapeada
    raise ValueError(f"Combinação não suportada: Derivada {ordem_derivada}ª, Erro O(h^{ordem_erro}), Tipo {filosofia}")
