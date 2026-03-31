def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do Peso"
    elif imc < 25:
        return "Peso Ideal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 40:
        return "Obesidade"
    return "Obesidade Mórbida"


def main() -> None:
    peso: float = float(input("Peso: "))
    altura: float = float(input("Altura: "))

    imc: float = calcular_imc(peso, altura)

    print(f"IMC: {imc:.2f}")
    print(classificar_imc(imc))


if __name__ == "__main__":
    main()
