def repetir_mensagem(msg: str, vezes: int) -> str:
    return (msg + " ") * vezes


def main() -> None:
    mensagem: str = input("Digite a mensagem: ")
    quantidade: int = int(input("Quantidade: "))

    resultado: str = repetir_mensagem(mensagem, quantidade)

    print(resultado)


if __name__ == "__main__":
    main()
