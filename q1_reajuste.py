def calcular_reajuste(salario: float, cargo: str) -> float:
    cargo = cargo.lower()
    if cargo == "gerente":
        return salario * 1.10
    elif cargo == "engenheiro":
        return salario * 1.20
    elif cargo in ("técnico", "tecnico"):
        return salario * 1.30
    else:
        return salario * 1.40

def main() -> None:
    salario: float = float(input("Digite o salário atual: R$ "))
    cargo: str = input("Digite o cargo: ")

    novo_salario: float = calcular_reajuste(salario, cargo)

    print(f"Novo salário: R$ {novo_salario:.2f}")

if __name__ == "__main__":
    main()
