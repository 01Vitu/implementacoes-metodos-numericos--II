class TabelaConvergencia: 
    def __init__(self, derivada_numerica, f_x, x_alvo, delta, filosofia, p, n, tolerancia):
        self.derivada_numerica = derivada_numerica
        self.f_x = f_x
        self.x_alvo = x_alvo
        self.delta = delta
        self.filosofia = filosofia
        self.p = p
        self.n = n
        self.tolerancia = tolerancia

    def print_resultados(self):
        # Calcular o valor de f(x) no ponto (que é constante para a coluna f(x))
        valor_fx = self.f_x(self.x_alvo)

        print("-" * 75)
        print(f"{'Δ(k)':<10} | {'f(x)':<15} | {'f\"(x)':<18} | {'e(x)':<15}")
        print("-" * 75)

        # Primeira iteração fora do ciclo 
        derivada_anterior = self.derivada_numerica(self.f_x, self.x_alvo, self.delta, self.filosofia, self.p, self.n)

        # Imprimir a primeira linha (o erro fica em branco ou usamos um traço)
        print(f"{self.delta:<10.5f} | {valor_fx:<15.5f} | {derivada_anterior:<18.8f} | {'-':<15}")

        erro_relativo = 1.0 # Iniciar com um erro grande para entrar no ciclo

        # Iniciar o estudo de convergência
        while erro_relativo >= self.tolerancia:
            # O passo é dividido por 2 a cada iteração (0.5 -> 0.25 -> 0.125 ...)
            self.delta = self.delta / 2 
            
            # Calcular a nova derivada com o novo delta
            derivada_atual = self.derivada_numerica(self.f_x, self.x_alvo, self.delta, self.filosofia, self.p, self.n)
            
            # Calcular o Erro Relativo Aproximado (fórmula da tabela)
            erro_relativo = abs((derivada_atual - derivada_anterior) / derivada_atual)
            
            # Imprimir a linha atual da tabela
            print(f"{self.delta:<10.5f} | {valor_fx:<15.5f} | {derivada_atual:<18.8f} | {erro_relativo:<15.8f}")
            
            # Atualizar a variável para a próxima iteração
            derivada_anterior = derivada_atual

        print("-" * 75)
        print(f"\nConvergência alcançada! O erro é: {erro_relativo:.8f} < {self.tolerancia}.")
