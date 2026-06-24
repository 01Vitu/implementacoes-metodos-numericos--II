def algoritmo_de_thomas(sub, principal, sup, rhs):
    """Resolve um sistema linear tridiagonal [A]{x} = {rhs}."""
    n = len(rhs)
    c_linha = [0.0] * n
    d_linha = [0.0] * n

    # Forward sweep
    c_linha[0] = sup[0] / principal[0]
    d_linha[0] = rhs[0] / principal[0]

    for i in range(1, n):
        m = principal[i] - sub[i - 1] * c_linha[i - 1]
        
        # CORREÇÃO: Verifica se não é a última linha antes de acessar sup[i]
        if i < n - 1:
            c_linha[i] = sup[i] / m
            
        d_linha[i] = (rhs[i] - sub[i - 1] * d_linha[i - 1]) / m

    # Back substitution
    u = [0.0] * n
    u[-1] = d_linha[-1]

    for i in range(n - 2, -1, -1):
        u[i] = d_linha[i] - c_linha[i] * u[i + 1]

    return u


def resolver_problema_original():
    # Parâmetros fixos
    a, b, c, d = 1.0, 7.0, -1.0, 2.0
    x0, xL, dx = 0.0, 2.0, 0.1
    u0, uL = 10.0, 1.0

    N_intervalos = int(round((xL - x0) / dx))
    malha_x = [x0 + i * dx for i in range(N_intervalos + 1)]
    N_incognitas = N_intervalos - 1

    # Coeficientes da EDO discretizada
    alpha = a - (b * dx) / 2.0
    beta = c * (dx**2) - 2.0 * a
    gamma = a + (b * dx) / 2.0
    termo_independente = d * (dx**2)

    # Montagem dos vetores das diagonais
    # Sub e Sup devem ter tamanho N-1, Principal tem tamanho N
    sub_diag = [alpha] * (N_incognitas - 1)
    diag_princ = [beta] * N_incognitas
    sup_diag = [gamma] * (N_incognitas - 1)

    vetor_b = [termo_independente] * N_incognitas

    # Aplicação das condições de contorno
    vetor_b[0] -= alpha * u0
    vetor_b[-1] -= gamma * uL

    # Chama o motor
    u_internos = algoritmo_de_thomas(sub_diag, diag_princ, sup_diag, vetor_b)
    
    return malha_x, [u0] + u_internos + [uL]