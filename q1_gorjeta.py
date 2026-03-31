def calcular_gorjeta(valor_conta: float) -> tuple[float, float]:
    gorjeta: float = valor_conta * 0.10
    total: float = valor_conta + gorjeta
    return gorjeta, total


def main() -> None:
    valor_conta: float = float(input("Digite o valor da conta: R$ "))

    gorjeta, total = calcular_gorjeta(valor_conta)

    print(f"Valor da Conta: R$ {valor_conta:.2f}")
    print(f"Gorjeta (10%): R$ {gorjeta:.2f}")
    print(f"Total a Pagar: R$ {total:.2f}")


if __name__ == "__main__":
    main()
