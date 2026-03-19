import math
import numpy as np
from Unidade01.derivada_numerica_taylor import derivada_numerica_taylor as derivada_numerica
from .tabela_convergencia import TabelaConvergencia

# ==========================================
# INTERFACE
# ==========================================

def criar_funcao(expr):
    def f(x):
        return eval(expr, {"__builtins__": {}}, {"x": x, "math": math, "np": np})
    return f

while True:
    try: 
        f_x = criar_funcao(input("Digite a função: "))
        x_alvo = float(input("Digite o ponto onde a derivada será avaliada: "))
        delta = float(input("Digite o tamanho do passo inicial: "))
        filosofia = input("Digite a filosofia (fw, bw, ct): ")
        p = int(input("Digite a ordem da derivada: "))
        n = int(input("Digite a ordem do erro de truncamento: "))
        tolerancia = float(input("Digite a tolerância: "))

        tabela_convergencia = TabelaConvergencia(derivada_numerica, f_x, x_alvo, delta, filosofia, p, n, tolerancia)

        tabela_convergencia.print_resultados()

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        print(f"\nPressione 'Enter' para continuar ou '0' para sair ...")
   
    if input() == '0':
        break
