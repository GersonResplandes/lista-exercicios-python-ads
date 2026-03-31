def aprovar_emprestimo(valor: float, salario: float, anos: int) -> bool:
    prestacao: float = valor / (anos * 12)
    limite: float = salario * 0.30
    return prestacao <= limite


def main() -> None:
    valor: float = float(input("Valor da casa: "))
    salario: float = float(input("Salário: "))
    anos: int = int(input("Anos: "))

    if aprovar_emprestimo(valor, salario, anos):
        print("Aprovado")
    else:
        print("Negado")


if __name__ == "__main__":
    main()
