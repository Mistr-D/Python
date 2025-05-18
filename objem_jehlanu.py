def vypocitej_objem_jehlanu(delka_zakladu, sirka_zakladu, vyska):
    return (delka_zakladu * sirka_zakladu * vyska) / 3

if __name__ == "__main__":
    delka_zakladu = float(input("Zadejte délku základny jehlanu: "))
    sirka_zakladu = float(input("Zadejte šířku základny jehlanu: "))
    vyska = float(input("Zadejte výšku jehlanu: "))
    
    objem = vypocitej_objem_jehlanu(delka_zakladu, sirka_zakladu, vyska)
    print(f"Objem jehlanu je: {objem}")