import math
import sys
from utils import gerar_malha
import euler_explicito
import euler_implicito
import rk4
import preditor_corretor

def compilar_funcao(expressao_str):
    escopo = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    escopo['math'] = math

    def f(t, y):
        try:
            return eval(expressao_str, escopo, {'t': t, 'y': y})
        except Exception as e:
            raise ValueError(f"Falha de sintaxe matemática: {e}")
    return f

def ler_float(prompt, padrao):
    entrada = input(f"{prompt} [{padrao}]: ").strip()
    if not entrada: return padrao
    try: return float(entrada)
    except: return padrao

def desenhar_tabela(dados):
    colunas = list(dados.keys())
    largura = 15
    cabecalho = " | ".join([f"{c:^{largura}}" for c in colunas])
    traco = "-" * len(cabecalho)
    
    print(f"\n{traco}\n{cabecalho}\n{traco}")
    for i in range(len(dados['Tempo (t)'])):
        linha = [f"{dados[c][i]:^{largura}.4f}" if c=='Tempo (t)' else f"{dados[c][i]:^{largura}.6f}" for c in colunas]
        print(" | ".join(linha))
    print(traco)

def iniciar():
    solucionadores = {
        '1': ('Euler Exp.', euler_explicito.calcular),
        '2': ('Euler Imp.', euler_implicito.calcular),
        '3': ('RK4', rk4.calcular),
        '4': ('Pred-Corr', preditor_corretor.calcular)
    }

    while True:
        print("\n" + "="*50)
        print("         METODOS EDOs")
        print("="*50)

        expr = input("Digite f(t, y) [Padrão: -2*y + t]: ").strip() or "-2*y + t"
        try:
            f_edo = compilar_funcao(expr)
            f_edo(0, 0)
        except Exception as e:
            print(f"\n[!] Erro: {e}")
            continue

        print("\n--- Condições Iniciais ---")
        t0 = ler_float("t0", 0.0)
        y0 = ler_float("y0", 1.0)
        tf = ler_float("tf", 2.0)
        h  = ler_float("Passo h", 0.2)

        if h <= 0 or tf <= t0:
            print("\n[!] Parâmetros de malha impossíveis.")
            continue

        print("\n--- Escolha o Método ---")
        print("1. Euler Explícito\n2. Euler Implícito\n3. Runge-Kutta 4\n4. Preditor-Corretor (ABM4)\n5. Todos (Comparativo)")
        op = input("\nOpção [5]: ").strip() or '5'

        t_base = gerar_malha(t0, tf, h)
        tabela = {'Tempo (t)': t_base}

        metodos_a_rodar = solucionadores.keys() if op == '5' else [op]

        for chave in metodos_a_rodar:
            if chave in solucionadores:
                nome_coluna, funcao_calculo = solucionadores[chave]
                _, valores_y = funcao_calculo(f_edo, t0, y0, tf, h)
                tabela[nome_coluna] = valores_y

        desenhar_tabela(tabela)

        if input("\nNova simulação? (s/n) [s]: ").strip().lower() == 'n':
            break

if __name__ == "__main__":
    iniciar()