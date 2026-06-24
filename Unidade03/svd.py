import math
import sys

# Adiciona o diretório atual ao path para importar os métodos de potência e QR
sys.path.append(r"c:\Users\wmarq\Desktop\implementacoes-metodos-numericos--II\Unidade03")
from metodo_qr import algoritmo_qr
from potencia_desolocado import potencia_deslocada

def transpor(A):
    m = len(A)
    n = len(A[0])
    return [[A[i][j] for i in range(m)] for j in range(n)]

def mat_vec_mult(A, x):
    m = len(A)
    n = len(A[0])
    y = [0.0] * m
    for i in range(m):
        y[i] = sum(A[i][j] * x[j] for j in range(n))
    return y

def produto_escalar(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))

def norma_l2(v):
    return math.sqrt(produto_escalar(v, v))

def imprimir_matriz(A):
    for linha in A:
        print("  [" + ", ".join(f"{val:8.4f}" for val in linha) + "]")

def ortogonalizar_vetores(vetores):
    Q = []
    for v in vetores:
        v_proj = v[:]
        for q in Q:
            proj = produto_escalar(v_proj, q)
            v_proj = [vi - proj * qi for vi, qi in zip(v_proj, q)]
        norma = norma_l2(v_proj)
        if norma > 1e-9:
            Q.append([vi / norma for vi in v_proj])
    return Q

def completar_base_ortonormal(U_parcial, m):
    base = [list(u) for u in U_parcial]
    for i in range(m):
        e = [0.0] * m
        e[i] = 1.0
        base.append(e)
        
    Q = []
    for v in base:
        v_proj = v[:]
        for q in Q:
            proj = produto_escalar(v_proj, q)
            v_proj = [vi - proj * qi for vi, qi in zip(v_proj, q)]
        norma = norma_l2(v_proj)
        if norma > 1e-9:
            Q.append([vi / norma for vi in v_proj])
            if len(Q) == m:
                break
    return Q

def resolver_autovalores_autovetores(A_bar):
    # 1. Encontrar todos os autovalores aproximados via algoritmo QR
    autovalores_aprox, _ = algoritmo_qr(A_bar)[1], None  # compatibilidade: extrai apenas Lamb
    
    eigenvalues = []
    eigenvectors = []
    
    # 2. Encontrar autovetor para cada autovalor usando potência deslocada com perturbação
    for val_aprox in autovalores_aprox:
        # Pequena perturbação de 1e-3 para afastar da singularidade exata de A - lambda * I
        shift = val_aprox + 1e-3
        val, vec, it = potencia_deslocada(A_bar, shift, tol=1e-9)
        if val is not None:
            norma = norma_l2(vec)
            vec = [v / norma for v in vec]
            eigenvalues.append(val)
            eigenvectors.append(vec)
        else:
            eigenvalues.append(val_aprox)
            eigenvectors.append([0.0]*len(A_bar))
            
    # Ortogonalização de Gram-Schmidt para tratar auto-espaços de multiplicidade > 1
    eigenvectors = ortogonalizar_vetores(eigenvectors)
    
    # Completar base caso haja perda de dimensão por convergência duplicada
    if len(eigenvectors) < len(A_bar):
        eigenvectors = completar_base_ortonormal(eigenvectors, len(A_bar))
        
    return eigenvalues, eigenvectors

def calcular_svd(A):
    m = len(A)
    n = len(A[0])
    limiar = 1e-9
    
    # 3) Calcular a matriz simétrica A_bar
    if m >= n:
        AT = transpor(A)
        # A_bar = A^T * A (n x n)
        A_bar = [[sum(AT[i][k] * A[k][j] for k in range(m)) for j in range(n)] for i in range(n)]
        
        # 4) Achar autovalores e autovetores de A_bar
        eigenvalues, V_cols = resolver_autovalores_autovetores(A_bar)
        
        # Ordenar por ordem decrescente
        pares = sorted(zip(eigenvalues, V_cols), key=lambda x: x[0], reverse=True)
        eigenvalues = [p[0] for p in pares]
        V_cols = [p[1] for p in pares]
        
        # 5) Valores singulares
        valores_singulares = [math.sqrt(max(0.0, val)) for val in eigenvalues]
        
        # 6) Posto da matriz
        posto = sum(1 for sigma in valores_singulares if sigma > limiar)
        
        # 7) Montar U, Sigma, V
        # U_cols: u_i = (1 / sigma_i) * A * v_i
        U_cols = []
        for i in range(n):
            if valores_singulares[i] > limiar:
                Av = mat_vec_mult(A, V_cols[i])
                u_i = [val / valores_singulares[i] for val in Av]
                U_cols.append(u_i)
                
        U_cols = ortogonalizar_vetores(U_cols)
        U_cols = completar_base_ortonormal(U_cols, m)
        
        U = transpor(U_cols)
        V = transpor(V_cols)
        
        Sigma = [[0.0] * n for _ in range(m)]
        for i in range(min(m, n)):
            Sigma[i][i] = valores_singulares[i]
            
    else: # m < n
        # A_bar = A * A^T (m x m)
        AT = transpor(A)
        A_bar = [[sum(A[i][k] * AT[k][j] for k in range(n)) for j in range(m)] for i in range(m)]
        
        # 4) Achar autovalores e autovetores de A_bar
        eigenvalues, U_cols = resolver_autovalores_autovetores(A_bar)
        
        # Ordenar decrescente
        pares = sorted(zip(eigenvalues, U_cols), key=lambda x: x[0], reverse=True)
        eigenvalues = [p[0] for p in pares]
        U_cols = [p[1] for p in pares]
        
        # 5) Valores singulares
        valores_singulares = [math.sqrt(max(0.0, val)) for val in eigenvalues]
        
        # 6) Posto
        posto = sum(1 for sigma in valores_singulares if sigma > limiar)
        
        # 7) Montar U, Sigma, V
        # V_cols: v_i = (1 / sigma_i) * A^T * u_i
        V_cols = []
        for i in range(m):
            if valores_singulares[i] > limiar:
                ATu = mat_vec_mult(AT, U_cols[i])
                v_i = [val / valores_singulares[i] for val in ATu]
                V_cols.append(v_i)
                
        V_cols = ortogonalizar_vetores(V_cols)
        V_cols = completar_base_ortonormal(V_cols, n)
        
        U = transpor(U_cols)
        V = transpor(V_cols)
        
        Sigma = [[0.0] * n for _ in range(m)]
        for i in range(min(m, n)):
            Sigma[i][i] = valores_singulares[i]
            
    return A_bar, eigenvalues, valores_singulares, posto, U, Sigma, V

def multiplicar_u_sigma_vt(U, Sigma, V):
    m = len(U)
    n = len(V)
    VT = transpor(V)
    
    US = [[0.0] * len(Sigma[0]) for _ in range(m)]
    for i in range(m):
        for j in range(len(Sigma[0])):
            US[i][j] = sum(U[i][k] * Sigma[k][j] for k in range(len(U[0])))
            
    USVT = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            USVT[i][j] = sum(US[i][k] * VT[k][j] for k in range(len(US[0])))
            
    return USVT

def main():
    print("="*65)
    print("        DECOMPOSIÇÃO EM VALORES SINGULARES (SVD) - PYTHON PURO")
    print("="*65)
    
    # 1) Ler o número de linhas (m) e colunas (n)
    try:
        m = int(input("Digite o número de linhas (m): "))
        n = int(input("Digite o número de colunas (n): "))
    except ValueError:
        print("[Erro] O tamanho deve ser um número inteiro.")
        return

    if m < 1 or n < 1:
        print("[Erro] Dimensões devem ser positivas.")
        return

    # 2) Ler a matriz A mxn
    print(f"\nDigite a matriz A ({m}x{n}):")
    A = []
    for i in range(m):
        while True:
            try:
                linha_input = input(f"Linha {i+1}: ").strip().replace(",", ".")
                vals = [float(x) for x in linha_input.split()]
                if len(vals) != n:
                    print(f"[Erro] A linha deve ter exatamente {n} elementos. Tente novamente.")
                    continue
                A.append(vals)
                break
            except ValueError:
                print("[Erro] Entrada inválida. Use apenas números separados por espaços.")

    print("\nMatriz A inserida:")
    imprimir_matriz(A)
    
    # Executar o cálculo SVD
    A_bar, eigenvalues, valores_singulares, posto, U, Sigma, V = calcular_svd(A)
    
    # 3) Mostrar A_bar
    print("\n" + "-"*65)
    if m >= n:
        print(f"3) Matriz simétrica A_bar = A^T . A ({n}x{n}):")
    else:
        print(f"3) Matriz simétrica A_bar = A . A^T ({m}x{m}):")
    imprimir_matriz(A_bar)
    
    # 4) Autovalores e Autovetores de A_bar
    print("\n4) Autovalores de A_bar:")
    print("  [" + ", ".join(f"{v:.6f}" for v in eigenvalues) + "]")
    
    # 5) Valores singulares
    print("\n5) Valores singulares (sigma_i):")
    print("  [" + ", ".join(f"{v:.6f}" for v in valores_singulares) + "]")
    
    # 6) Posto da matriz A
    print(f"\n6) Posto da matriz A (valores singulares > 0): {posto}")
    
    # 7) Mostrar U, Sigma e V
    print("\n7) Matriz ortogonal U (m x m):")
    imprimir_matriz(U)
    
    print("\nMatriz Sigma (m x n):")
    imprimir_matriz(Sigma)
    
    print("\nMatriz ortogonal V (n x n):")
    imprimir_matriz(V)
    
    # 8) Verificar se U * Sigma * V^T = A
    reconstruida = multiplicar_u_sigma_vt(U, Sigma, V)
    print("\n" + "-"*65)
    print("8) Matriz Reconstruída (U . Sigma . V^T):")
    imprimir_matriz(reconstruida)
    
    # Calcular o erro absoluto máximo da reconstrução
    erro_max = 0.0
    for i in range(m):
        for j in range(n):
            erro_max = max(erro_max, abs(reconstruida[i][j] - A[i][j]))
            
    print(f"\nVerificação de erro absoluto máximo: {erro_max:.2e}")
    if erro_max < 1e-9:
        print(">> [Sucesso] Decomposição SVD verificada com sucesso! U . Sigma . V^T = A")
    else:
        print(">> [Alerta] Erro na reconstrução excedeu a tolerância.")

if __name__ == "__main__":
    main()
