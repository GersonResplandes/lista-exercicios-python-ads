def eh_par(numero: int) -> bool:
    return numero % 2 == 0


def main() -> None:
    numero: int = int(input("Digite um número: "))

    if eh_par(numero):
        print("PAR")
    else:
        print("ÍMPAR")


if __name__ == "__main__":
    main()
