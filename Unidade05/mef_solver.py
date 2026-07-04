from mdf_solver import algoritmo_de_thomas

def resolver_problema_mef():
    """
    Resolve o problema u''(x) + 7u'(x) - u(x) = 2 com u(0)=10, u(2)=1
    Utilizando o Método dos Elementos Finitos (Galerkin) com elementos lineares 1D.
    """
    a, b, c, d_val = 1.0, 7.0, -1.0, 2.0
    x0, xL, dx = 0.0, 2.0, 0.1
    u0, uL = 10.0, 1.0

    N_intervalos = int(round((xL - x0) / dx))
    malha_x = [x0 + i * dx for i in range(N_intervalos + 1)]
    N_incognitas = N_intervalos - 1
    h = dx

    # Montagem das diagonais da matriz de Rigidez Global (K)
    # Originada das integrais das funções de base N_i (funções 'chapéu')
    # \int N_i' N_j' dx , \int N_i' N_j dx , \int N_i N_j dx
    val_sub = -a/h + b/2.0 + (c*h)/6.0
    val_princ = (2.0*a)/h + (2.0*c*h)/3.0
    val_sup = -a/h - b/2.0 + (c*h)/6.0
    
    sub_diag = [val_sub] * (N_incognitas - 1)
    diag_princ = [val_princ] * N_incognitas
    sup_diag = [val_sup] * (N_incognitas - 1)

    # Vetor de Forças global F
    # F_i = - \int d_val * N_i dx = -d_val * h
    vetor_f = [-d_val * h] * N_incognitas

    # Aplicação das Condições de Contorno (Dirichlet)
    vetor_f[0] -= val_sub * u0
    vetor_f[-1] -= val_sup * uL

    # Resolução do sistema tridiagonal
    u_internos = algoritmo_de_thomas(sub_diag, diag_princ, sup_diag, vetor_f)
    
    return malha_x, [u0] + u_internos + [uL]

if __name__ == "__main__":
    xs, us = resolver_problema_mef()
    print("=== SOLUÇÃO POR ELEMENTOS FINITOS (BÔNUS) ===")
    for x, u in zip(xs, us):
        print(f"{x:^10.1f} | {u:^15.6f}")
