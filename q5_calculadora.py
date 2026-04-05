def operar(num1: float, num2: float, op: str) -> float:
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            raise ValueError("Erro: Divisão por zero não permitida.")
        return num1 / num2
    else:
        raise ValueError("Erro: Operador inválido.")

def main() -> None:
    num1: float = float(input("Primeiro número: "))
    op: str = input("Operador algébrico (+, -, *, /): ")
    num2: float = float(input("Segundo número: "))

    try:
        resultado: float = operar(num1, num2, op)
        print(f"Resultado: {resultado}")
    except ValueError as erro:
        print(erro)

if __name__ == "__main__":
    main()
