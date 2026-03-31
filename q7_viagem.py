def calcular_preco(distancia: float) -> float:
    if distancia <= 200:
        return distancia * 0.50
    return distancia * 0.45


def main() -> None:
    distancia: float = float(input("Distância (Km): "))

    preco: float = calcular_preco(distancia)

    print(f"Preço: R$ {preco:.2f}")


if __name__ == "__main__":
    main()
