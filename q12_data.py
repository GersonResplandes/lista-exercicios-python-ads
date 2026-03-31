def data_valida(dia: int, mes: int, ano: int) -> bool:
    if ano <= 0 or mes < 1 or mes > 12:
        return False

    if mes == 2:
        max_dias: int = 28
    elif mes in (4, 6, 9, 11):
        max_dias = 30
    else:
        max_dias = 31

    return 1 <= dia <= max_dias


def main() -> None:
    dia: int = int(input("Dia: "))
    mes: int = int(input("Mês: "))
    ano: int = int(input("Ano: "))

    if data_valida(dia, mes, ano):
        print("Data válida")
    else:
        print("Data inválida")


if __name__ == "__main__":
    main()
