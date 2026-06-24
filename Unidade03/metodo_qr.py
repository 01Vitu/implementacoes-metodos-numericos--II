import math

def transpor(A):
    n = len(A)
    return [[A[j][i] for j in range(n)] for i in range(n)]

def mat_mult(A, B):
    n = len(A)
    C = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return C

def construir_Jij(n, i, j, c, s):
    """Monta a matriz de rotação de Givens Jij (n x n)."""
    J = [[1.0 if k == l else 0.0 for l in range(n)] for k in range(n)]
    J[i][i] =  c;  J[i][j] = s
    J[j][i] = -s;  J[j][j] = c
    return J

def decomposicao_qr(A):
    """
    Decomposição A = Q * R via Rotações de Givens (Jacobi).
    Segue o algoritmo do slide 3.1.1:
      - QT = I (acumula J_(n(n-1)) ... J_31 J_21)
      - A cada passo: R_nova = Jij * R_velha, QT = Jij * QT
      - Ao final: Q = Transposta(QT), R = R_nova
    """
    n = len(A)
    R_velha = [linha[:] for linha in A]
    QT = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for j in range(n - 1):           # loop das colunas (j = 1 ... n-1)
        for i in range(j + 1, n):   # loop das linhas (i = j+1 ... n)
            a = R_velha[j][j]
            b = R_velha[i][j]
            r = math.sqrt(a**2 + b**2)
            if r < 1e-12:
                continue
            c = a / r
            s = b / r
            Jij = construir_Jij(n, j, i, c, s)
            R_velha = mat_mult(Jij, R_velha)    # R_nova = Jij * R_velha
            QT     = mat_mult(Jij, QT)           # QT = Jij * QT

    Q = transpor(QT)    # Q = Transposta(QT)
    R = R_velha
    return Q, R

def algoritmo_qr(A, tol=1e-7, max_iter=1000):
    """
    Aplica iterações A_nova = R * Q (= Q^T A_velha Q) até a matriz se diagonalizar.
    Segue o algoritmo 3.1.1:
      - Inicializa P = I
      - A cada iteração: (Q,R) = decomposicaoQR(A_velha); A_nova = R*Q; P = P*Q
      - Convergência: val = soma dos quadrados dos termos ABAIXO da diagonal principal
    Retorna: (P, Lamb, iteracao) onde
      - P: matriz cujas colunas são os autovetores (P = Q1*Q2*...*Qk)
      - Lamb: lista com os autovalores (diagonal de A_nova)
      - iteracao: número de iterações realizadas
    """
    n = len(A)
    A_velha = [linha[:] for linha in A]
    P = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for iteracao in range(1, max_iter + 1):
        Q, R = decomposicao_qr(A_velha)
        A_nova = mat_mult(R, Q)         # A_nova = R * Q
        A_velha = A_nova
        P = mat_mult(P, Q)              # P = P * Q (acumula autovetores)

        # Convergência: soma dos QUADRADOS dos termos ABAIXO da diagonal
        val = sum(A_nova[i][j]**2 for i in range(n) for j in range(i))
        if val < tol:
            break

    Lamb = [A_velha[i][i] for i in range(n)]
    return P, Lamb, iteracao