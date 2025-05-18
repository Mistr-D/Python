def obsah_obdelniku(sirka, vyska):

    return sirka * vyska

if __name__ == "__main__":
    sirka = float(input("Zadejte šířku obdélníku: "))
    vyska = float(input("Zadejte výšku obdélníku: "))
    print(f"Obsah obdélníku je: {obsah_obdelniku(sirka, vyska)}")
