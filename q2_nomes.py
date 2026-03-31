def contar_caracteres(nome: str) -> int:
    return len(nome)


def main() -> None:
    nome: str = input("Digite seu nome completo: ")

    total: int = contar_caracteres(nome)

    print(f"Bem-vindo(a), {nome}!")
    print(f"Seu nome possui {total} caracteres.")


if __name__ == "__main__":
    main()
