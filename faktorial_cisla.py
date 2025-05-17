def faktorial(n):
    if n < 0:
        return "Faktoriál není definován pro záporná čísla."
    elif n == 0 or n == 1:
        return 1
    else:
        vysledek = 1
        for i in range(2, n + 1):
            vysledek *= i
        return vysledek

if __name__ == "__main__":
    cislo = int(input("Zadejte číslo pro výpočet faktoriálu: "))
    print(f"Faktoriál čísla {cislo} je {faktorial(cislo)}")