from potencia_regular import potencia_regular
from potencia_inverso import potencia_inversa
from potencia_desolocado import potencia_deslocada
from metodo_householder import householder_tridiagonal
from metodo_qr import algoritmo_qr

def eh_simetrica(A):
    """Verifica matematicamente se A = A^T (com tolerância para erro de float)."""
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i][j] - A[j][i]) > 1e-9:
                return False
    return True

def imprimir_matriz(A):
    for linha in A:
        print("  [" + ", ".join(f"{val:8.4f}" for val in linha) + "]")

def ler_matriz_inteligente():
    """Lê a matriz permitindo digitação manual OU colagem direta de um bloco de texto."""
    print("\n" + "="*65)
    print("               INSERÇÃO DE MATRIZ PERSONALIZADA")
    print("="*65)
    print(" Instruções:")
    print(" 1. Digite os números da Linha 1 separados por espaço e dê Enter.")
    print(" 2. O sistema detectará o tamanho (N) da matriz automaticamente.")
    print(" 3. (DICA): Se você já tem a matriz copiada de um TXT ou Excel,")
    print("    basta dar Ctrl+V aqui na Linha 1 e apertar Enter uma única vez!\n")
    
    while True:
        try:
            entrada_l1 = input("Linha 1: ").strip()
            if not entrada_l1:
                continue
                
            # Aceita tanto ponto quanto vírgula decimal
            entrada_l1 = entrada_l1.replace(",", ".")
            linha1 = [float(x) for x in entrada_l1.split()]
            n = len(linha1)
            
            if n < 2:
                print("[Erro] Matrizes precisam ser no mínimo 2x2. Tente de novo.")
                continue
                
            matriz = [linha1]
            print(f" --> Tamanho {n}x{n} detectado. Aguardando as {n-1} linhas restantes...")
            
            for i in range(1, n):
                ent_linha = input(f"Linha {i+1}: ").strip().replace(",", ".")
                vals = [float(x) for x in ent_linha.split()]
                
                if len(vals) != n:
                    print(f"\n[ERRO] A Linha {i+1} precisava ter {n} elementos, mas veio com {len(vals)}.")
                    print("Inserção cancelada. Vamos recomeçar do zero.\n")
                    break
                matriz.append(vals)
            else:
                print(f"\n[Sucesso] Matriz {n}x{n} carregada perfeitamente!")
                return matriz
                
        except ValueError:
            print("\n[Erro] Digitação inválida. Use apenas números, pontos e espaços.\n")

def pausa():
    input("\nPressione [ ENTER ] para voltar ao menu...")

def carregar_matriz_teste(opcao):
    if opcao == "1": # Simétrica 4x4 (Autovalores: 4, 3, 2, 1)
        return [[2.5, 1.0, 0.5, 0.0], [1.0, 2.5, 0.0, 0.5], [0.5, 0.0, 2.5, 1.0], [0.0, 0.5, 1.0, 2.5]]
    else:            # Poisson 3x3
        return [[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 4.0]]


def main():
    # Pergunta inicial clara
    print("="*65)
    print("    SUÍTE DE ÁLGEBRA LINEAR COMPUTACIONAL (100% Python Puro)")
    print("="*65)
    print("Escolha a matriz de partida:")
    print(" [ 1 ] Quero digitar ou COLAR minha própria matriz agora")
    print(" [ 2 ] Usar Matriz Simétrica 4x4 de teste (Autovalores: 4, 3, 2, 1)")
    print(" [ 3 ] Usar Matriz de Poisson 3x3")
    
    escolha = input("\nOpção: ").strip()
    if escolha == "1":
        A = ler_matriz_inteligente()
    elif escolha == "2":
        A = carregar_matriz_teste("1")
    else:
        A = carregar_matriz_teste("2")

    while True:
        status_simetria = "SIMÉTRICA" if eh_simetrica(A) else "NÃO-SIMÉTRICA"
        n = len(A)
        
        print("\n" + "="*65)
        print(f" MATRIZ ATIVA EM MEMÓRIA ({n}x{n})               Status: [{status_simetria}]")
        print("="*65)
        imprimir_matriz(A)
        print("-" * 65)
        print(" ESCOLHA O MÉTODO DE CÁLCULO:")
        print("  [ 1 ] Método da Potência Regular     (Maior Autovalor)")
        print("  [ 2 ] Método da Potência Inversa     (Menor Autovalor)")
        print("  [ 3 ] Método da Potência c/ Desloc.  (Autovalor próximo a X)")
        print("  [ 4 ] Caixa Preta 1: Householder     (Tridiagonalizar)")
        print("  [ 5 ] Caixa Preta 2: Algoritmo QR    (Espectro via QR puro)")
        print("  [ 6 ] PIPELINE: Householder + QR     (Sequência Otimizada)")
        print("\n TROCAR A MATRIZ:")
        print("  [ M ] Colar / Digitar uma nova matriz")
        print("  [ T ] Carregar uma matriz de teste do sistema")
        print("  [ 0 ] Sair")
        print("-" * 65)
        
        op = input("Opção escolhida: ").strip().upper()

        if op == "0":
            print("\nEncerrando...")
            break

        elif op == "1":
            val, vec, it = potencia_regular(A)
            print(f"\n[Dominante] Maior Autovalor: {val:.6f} (em {it} iterações)")
            print(f"Autovetor associado: {[round(v, 4) for v in vec]}")
            pausa()

        elif op == "2":
            val, vec, it = potencia_inversa(A)
            if val is not None:
                print(f"\n[Mínimo] Menor Autovalor: {val:.6f} (em {it} iterações)")
                print(f"Autovetor associado: {[round(v, 4) for v in vec]}")
            else:
                print("\n[Erro] Matriz estritamente singular.")
            pausa()

        elif op == "3":
            try:
                alvo = float(input("\nDigite o valor alvo de busca (deslocamento): ").replace(",", "."))
                val, vec, it = potencia_deslocada(A, alvo)
                print(f"\n[Resultado] Autovalor mais próximo de {alvo}: {val:.6f} (em {it} iterações)")
            except ValueError:
                print("\n[Erro] Número inválido.")
            pausa()

        elif op == "4":
            if not eh_simetrica(A):
                print("\n[CUIDADO] A matriz não é simétrica. O resultado de Householder será matematicamente falso.")
                if input("Deseja forçar o cálculo mesmo assim? (S/N): ").strip().upper() != "S":
                    continue
            print("\nTransformando em Tridiagonal (Householder)...")
            T = householder_tridiagonal(A)
            imprimir_matriz(T)
            pausa()

        elif op == "5":
            print("\nRodando Algoritmo QR Bruto (pode demorar em matrizes grandes)...")
            vals, it = algoritmo_qr(A)
            print(f"\nAutovalores encontrados ({it} iterações):")
            print("  [" + ", ".join(f"{v:.4f}" for v in vals) + "]")
            pausa()

        elif op == "6":
            if not eh_simetrica(A):
                print("\n[ERRO] O Pipeline Householder+QR exige estritamente uma matriz Simétrica.")
                pausa()
                continue
                
            print("\n" + "."*50)
            print(" >> [Passo 1] Aplicando Reflexões de Householder...")
            T = householder_tridiagonal(A)
            
            print(" >> [Passo 2] Injetando Tridiagonal no Algoritmo QR...")
            vals, it = algoritmo_qr(T)
            
            print("."*50)
            print(f"\n ESTABILIDADE ATINGIDA EM APENAS {it} ITERAÇÕES.")
            print("\n ESPECTRO COMPLETO DE AUTOVALORES:")
            print("   " + "  |  ".join(f"λ = {v:.5f}" for v in vals))
            pausa()

        elif op == "M":
            nova = ler_matriz_inteligente()
            if nova: A = nova
            pausa()

        elif op == "T":
            print("\n [1] Simétrica 4x4  |  [2] Poisson 3x3")
            A = carregar_matriz_teste(input("Escolha: ").strip())

        else:
            print("\nOpção inexistente.")
            pausa()

if __name__ == "__main__":
    main()