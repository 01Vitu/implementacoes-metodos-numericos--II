def gerar_malha(t0, tf, h):
    """Gera o vetor de tempo de forma numericamente segura contra erros de float."""
    num_passos = int(round((tf - t0) / h))
    return [t0 + i * h for i in range(num_passos + 1)]