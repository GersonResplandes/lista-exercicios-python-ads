def calcular_multa(velocidade: float) -> float:
    if velocidade > 80:
        return (velocidade - 80) * 7
    return 0.0


def main() -> None:
    velocidade: float = float(input("Velocidade: "))

    multa: float = calcular_multa(velocidade)

    if multa > 0:
        print(f"Multa: R$ {multa:.2f}")
    else:
        print("Velocidade dentro do permitido")


if __name__ == "__main__":
    main()
