def analisar_jogada(usuario: str, pc: str) -> str:
    if usuario not in ("pedra", "papel", "tesoura"):
        return "Opção inválida!"

    if usuario == pc:
        return "EMPATE"

    if (usuario == "pedra" and pc == "tesoura") or \
       (usuario == "papel" and pc == "pedra") or \
       (usuario == "tesoura" and pc == "papel"):
        return "VOCÊ VENCEU"
    
    return "COMPUTADOR VENCEU"

def main() -> None:
    print("Jokenpô: [pedra] [papel] [tesoura]")
    escolha_usuario: str = input("Sua jogada: ").lower()

    escolha_computador: str = "pedra"
    
    print(f"Computador escolheu: {escolha_computador}")
    
    resultado: str = analisar_jogada(escolha_usuario, escolha_computador)
    print(resultado)

if __name__ == "__main__":
    main()
