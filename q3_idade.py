def converter_idade(anos: int) -> tuple[int, int]:
    meses: int = anos * 12
    dias: int = anos * 365
    return meses, dias


def main() -> None:
    idade: int = int(input("Digite sua idade: "))

    meses, dias = converter_idade(idade)

    print(f"Meses: {meses}")
    print(f"Dias: {dias}")


if __name__ == "__main__":
    main()
