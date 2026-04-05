def calcular_preco_final(preco: float, opcao: int) -> float:
    if opcao == 1:
        return preco * 0.90
    elif opcao == 2:
        return preco * 0.95
    elif opcao == 3:
        return preco
    elif opcao == 4:
        return preco * 1.20
    else:
        raise ValueError("Opção de pagamento inválida.")

def main() -> None:
    preco: float = float(input("Preço do produto: R$ "))
    print("\nFORMAS DE PAGAMENTO")
    print("[ 1 ] À vista (dinheiro/cheque)")
    print("[ 2 ] À vista no cartão")
    print("[ 3 ] Em até 2x no cartão")
    print("[ 4 ] 3x ou mais no cartão")
    opcao: int = int(input("Escolha a opção: "))

    try:
        total: float = calcular_preco_final(preco, opcao)
        print(f"Valor final a ser pago: R$ {total:.2f}")
    except ValueError as err:
        print(f"Erro: {err}")

if __name__ == "__main__":
    main()
