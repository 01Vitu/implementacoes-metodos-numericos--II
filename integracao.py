import math

while True:
    print("\nIntegracao Numérica - Método de Newton-Cotes")
    function = input("Digite a função a ser integrada: ")

    if function.lower() == 'sair':
        break

    def f(x):    
        # Adicionei o math e sin/cos/exp no contexto para facilitar a sua digitação
        return eval(function, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp, "sqrt": math.sqrt})

    a = float(input("Limite inferior de integração: "))
    b = float(input("Limite superior de integração: "))
    grau = int(input("Grau do polinômio de aproximação: "))
    tipo = input("Tipo: (A)berta ou (F)echada: ").strip().upper()

    resultado = 0

    if tipo == 'F':
        h = (b - a) / grau
        match grau:
            case 1:
                resultado = (h/2) * (f(a) + f(b))
            case 2:
                resultado = (h/3) * (f(a) + 4*f(a+h) + f(b))
            case 3:
                resultado = (3*h/8) * (f(a) + 3*f(a+h) + 3*f(a+2*h) + f(b))
            case 4:
                resultado = (2*h/45) * (7*f(a) + 32*f(a+h) + 12*f(a+2*h) + 32*f(a+3*h) + 7*f(b))

    elif tipo == 'A':
        h = (b - a) / (grau + 2)
        match grau:
            case 1:
                resultado = 2 * h * f(a + h)
            case 2:
                resultado = (3*h/2) * (f(a+h) + f(a+2*h))
            case 3:
                resultado = (4*h/3) * (2*f(a+h) - f(a+2*h) + 2*f(a+3*h))
            case 4:
                resultado = (5*h/24) * (11*f(a+h) + f(a+2*h) + f(a+3*h) + 11*f(a+4*h))

    print(f"\nResultado da Integral: {resultado:.8f}")