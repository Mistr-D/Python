import math

def celkova_delka_hran(delka_hrany_zakladu, vyska_sikme_hrany):

    
    delka_zakladnich_hran = 4 * delka_hrany_zakladu
    
    
    delka_sikmych_hran = 4 * math.sqrt((delka_hrany_zakladu / 2) ** 2 + vyska_sikme_hrany ** 2)
    
    
    return delka_zakladnich_hran + delka_sikmych_hran


delka_hrany_zakladu = float(input("Zadejte délku jedné strany základny (v centimetrech): "))
vyska_sikme_hrany = float(input("Zadejte šikmou výšku jehlanu (v centimetrech): "))


celkova_delka = celkova_delka_hran(delka_hrany_zakladu, vyska_sikme_hrany)
print(f"Celková délka všech hran je: {celkova_delka:.2f} centimetrů")