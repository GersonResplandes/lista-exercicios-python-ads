def formar_triangulo(a: float, b: float, c: float) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)

def classificar_triangulo(a: float, b: float, c: float) -> str:
    if a == b == c:
        return "EQUILÁTERO"
    elif a == b or b == c or a == c:
        return "ISÓSCELES"
    return "ESCALENO"

def main() -> None:
    r1: float = float(input("Comprimento da reta 1: "))
    r2: float = float(input("Comprimento da reta 2: "))
    r3: float = float(input("Comprimento da reta 3: "))

    if formar_triangulo(r1, r2, r3):
        print("As retas PODEM formar um triângulo.")
        print(f"Tipo: {classificar_triangulo(r1, r2, r3)}")
    else:
        print("As retas NÃO podem formar um triângulo.")

if __name__ == "__main__":
    main()
