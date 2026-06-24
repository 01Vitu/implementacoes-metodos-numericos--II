from mdf_solver import resolver_problema_original

def main():
    xs, us = resolver_problema_original()

    print("=== SOLUÇÃO DO PROBLEMA ORIGINAL ===")
    print("\nPares ordenados para plotagem:")
    pares = [f"({xs[i]:.1f}, {us[i]:.6f})" for i in range(len(xs))]
    print(", ".join(pares))

    print("\n\nTabela de valores:")
    print("-" * 30)
    print(f"{'x':^10} | {'u(x)':^15}")
    print("-" * 30)
    for x, u in zip(xs, us):
        print(f"{x:^10.1f} | {u:^15.6f}")
    print("-" * 30)

if __name__ == "__main__":
    main()