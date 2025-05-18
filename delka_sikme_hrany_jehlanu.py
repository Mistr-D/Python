import math

def vypocitej_sikmou_hranu(delka_zakladny, vyska):
    polovina_zakladny = delka_zakladny / 2
    sikma_hrana = math.sqrt(polovina_zakladny**2 + vyska**2)
    return sikma_hrana
if __name__ == "__main__":
    delka_zakladny = float(input("Zadejte délku hrany základny: "))
    vyska = float(input("Zadejte výšku jehlanu: "))
    
    sikma_hrana = vypocitej_sikmou_hranu(delka_zakladny, vyska)
    print(f"Délka šikmé hrany jehlanu je: {sikma_hrana:.2f}")