def calcular_desconto(preco: float, categoria: str) -> float:
    categoria = categoria.upper()

    if categoria == "A":
        return preco * 0.90
    elif categoria == "B":
        return preco * 0.85
    elif categoria == "C":
        return preco * 0.80

    raise ValueError("Categoria inválida")


def main() -> None:
    preco: float = float(input("Preço: "))
    categoria: str = input("Categoria (A/B/C): ")

    try:
        final: float = calcular_desconto(preco, categoria)
        print(f"Preço final: R$ {final:.2f}")
    except ValueError as erro:
        print(erro)


if __name__ == "__main__":
    main()
