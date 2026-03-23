from derivada_numerica_diferencas_finitas import derivada_numerica_diferencas_finitas
from derivada_numerica_taylor import derivada_numerica_taylor
from derivada_numerica_newton import derivada_numerica_newton
from unidade01_utils import criar_funcao

# ==========================================
# INTERFACE
# ==========================================

class MenuDerivada:

    def obter_dados(self):
        function_expression = input("Digite a função a ser derivada: ")
        f = criar_funcao(function_expression)

        x_val        = float(input("Ponto onde a derivada será avaliada: "))
        h_val        = float(input("Tamanho do passo (h): "))
        ordem_deriv  = int(input("Ordem da derivada: "))
        ordem_erro   = int(input("Ordem do erro: "))
        filosofia    = input("Filosofia: (FW) Forward, (BW) Backward ou (CT) Central: ").strip().lower()

        return f, x_val, h_val, ordem_deriv, ordem_erro, filosofia

    def menu(self):
        while True:
            opcao = input("\nEscolha o método: (1) Diferenças Finitas, (2) Taylor, (3) Newton, (0) Sair: ")

            if opcao == "0":
                print("\nSaindo...")
                break

            if opcao not in ("1", "2", "3"):
                print("Opção inválida. Tente novamente.")
                continue

            try:
                if opcao == "1":
                    print("\nDerivada Numérica - Método de Diferenças Finitas")
                    f, x_val, h_val, ordem_deriv, ordem_erro, filosofia = self.obter_dados()
                    resultado = derivada_numerica_diferencas_finitas(f, x_val, h_val, filosofia, ordem_deriv, ordem_erro)

                elif opcao == "2":
                    print("\nDerivada Numérica - Método de Expansão em Séries de Taylor")
                    f, x_val, h_val, ordem_deriv, ordem_erro, filosofia = self.obter_dados()
                    resultado = derivada_numerica_taylor(f, x_val, h_val, filosofia, ordem_deriv, ordem_erro)

                elif opcao == "3":
                    print("\nDerivada Numérica - Método de Newton")
                    f, x_val, h_val, ordem_deriv, ordem_erro, filosofia = self.obter_dados()
                    resultado = derivada_numerica_newton(f, x_val, h_val, filosofia, ordem_deriv, ordem_erro)

                print(f"\nResultado da Derivada: {resultado:.8f}")

            except (Exception) as e:
                print(f"Erro: {e}")
            
            print("\nPressione 'Enter' para continuar ou '0' para sair ...")
            if input() == "0":
                break
