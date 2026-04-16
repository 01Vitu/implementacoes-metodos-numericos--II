def calcular_newton_cotes(f, a, b, grau, tipo):
    if tipo == 'F':
        h = (b - a) / grau
        match grau:
            case 1:
                return (h/2) * (f(a) + f(b))
            case 2:
                return (h/3) * (f(a) + 4*f(a+h) + f(b))
            case 3:
                return (3*h/8) * (f(a) + 3*f(a+h) + 3*f(a+2*h) + f(b))
            case 4:
                return (2*h/45) * (7*f(a) + 32*f(a+h) + 12*f(a+2*h) + 32*f(a+3*h) + 7*f(b))
            case _:
                raise ValueError("Grau não implementado para Newton-Cotes Fechada.")
                
    elif tipo == 'A':
        h = (b - a) / (grau + 2)
        match grau:
            case 1:
                return 2 * h * f(a + h)
            case 2:
                return (3*h/2) * (f(a+h) + f(a+2*h))
            case 3:
                return (4*h/3) * (2*f(a+h) - f(a+2*h) + 2*f(a+3*h))
            case 4:
                return (5*h/24) * (11*f(a+h) + f(a+2*h) + f(a+3*h) + 11*f(a+4*h))
            case _:
                raise ValueError("Grau não implementado para Newton-Cotes Aberta.")
    else:
        raise ValueError("Tipo de fórmula inválido. Use 'A' ou 'F'.")