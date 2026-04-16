from math import *
from newton_cotes import calcular_newton_cotes
from gauss_legendre import calcular_gauss_legendre
from gauss_hermite import calcular_gauss_hermite
from gauss_laguerre import calcular_gauss_laguerre
from gauss_chebyshev import calcular_gauss_chebyshev

print("\nCalculadora de Integração Numérica")

while True:
    print("\nMétodos:")
    print("1 - Newton-Cotes")
    print("2 - Gauss-Legendre")
    print("3 - Gauss-Hermite")
    print("4 - Gauss-Laguerre")
    print("5 - Gauss-Chebyshev")
    print("0 - Sair")
    
    escolha = input("Escolha o método: ")

    if escolha == '0':
        print("Encerrando a calculadora.")
        break
        
    if escolha not in ['1', '2', '3', '4', '5']:
        print("Opção inválida.")
        continue

    func_str = input("Digite a função f(x): ")

    def f(x_val):
        return eval(func_str, globals(), {'x': x_val})

    # Só pedimos os limites (a e b) se o método for 1 ou 2
    if escolha in ['1', '2']:
        try:
            a = float(input("Limite inferior de integração (a): "))
            b = float(input("Limite superior de integração (b): "))
        except ValueError:
            print("Erro: Os limites devem ser números válidos.")
            continue

    if escolha == '1':
        try:
            grau = int(input("Grau do polinômio de aproximação (1 a 4): "))
        except ValueError:
            print("Erro: O grau deve ser um número inteiro.")
            continue
            
        tipo = input("Tipo: (A)berta ou (F)echada: ").strip().upper()

        try:
            resultado = calcular_newton_cotes(f, a, b, grau, tipo)
            print(f"\nResultado da Integral (Newton-Cotes): {resultado:.8f}")
        except ValueError as e:
            print(f"Erro: {e}")

    elif escolha == '2':
        try:
            n = int(input("Digite o número de pontos/nós para Gauss-Legendre (1 a 4): "))
        except ValueError:
            print("Erro: O número de pontos deve ser inteiro.")
            continue
        
        try:
            resultado = calcular_gauss_legendre(f, a, b, n)
            print(f"\nResultado da Integral (Gauss-Legendre com {n} pontos): {resultado:.8f}")
        except ValueError as e:
            print(f"Erro: {e}")
            
    elif escolha == '3':
        print("\n[Aviso] Gauss-Hermite integra de -infinito a +infinito.")
        print("A fórmula resolve a integral no formato: e^(-x^2) * f(x)")
        try:
            n = int(input("Digite o número de pontos para Gauss-Hermite (2 a 4): "))
        except ValueError:
            print("Erro: O número de pontos deve ser inteiro.")
            continue
            
        try:
            resultado = calcular_gauss_hermite(f, n)
            print(f"\nResultado da Integral (Gauss-Hermite com {n} pontos): {resultado:.8f}")
        except ValueError as e:
            print(f"Erro: {e}")

    elif escolha == '4':
        print("\n[Aviso] Gauss-Laguerre integra de 0 a +infinito.")
        print("A fórmula resolve a integral no formato: e^(-x) * f(x)")
        try:
            n = int(input("Digite o número de pontos para Gauss-Laguerre (2 a 4): "))
        except ValueError:
            print("Erro: O número de pontos deve ser inteiro.")
            continue
            
        try:
            resultado = calcular_gauss_laguerre(f, n)
            print(f"\nResultado da Integral (Gauss-Laguerre com {n} pontos): {resultado:.8f}")
        except ValueError as e:
            print(f"Erro: {e}")

    elif escolha == '5':
        print("\n[Aviso] Gauss-Chebyshev integra de -1 a 1.")
        print("A fórmula resolve a integral no formato: f(x) / sqrt(1 - x^2)")
        try:
            n = int(input("Digite o número de pontos para Gauss-Chebyshev (2 a 4): "))
        except ValueError:
            print("Erro: O número de pontos deve ser inteiro.")
            continue
            
        try:
            resultado = calcular_gauss_chebyshev(f, n)
            print(f"\nResultado da Integral (Gauss-Chebyshev com {n} pontos): {resultado:.8f}")
        except ValueError as e:
            print(f"Erro: {e}")