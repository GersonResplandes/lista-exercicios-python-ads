def analisar_alistamento(idade: int) -> str:
    if idade < 18:
        return f"Faltam {18 - idade} anos"
    elif idade == 18:
        return "Hora de se alistar"
    return f"Passaram {idade - 18} anos"


def main() -> None:
    nascimento: int = int(input("Ano nascimento: "))
    atual: int = int(input("Ano atual: "))

    idade: int = atual - nascimento

    print(analisar_alistamento(idade))


if __name__ == "__main__":
    main()
