heslo = input("Zadej heslo: ")

cisla = sum(1 for znak in heslo if znak.isdigit())
delka = len(heslo)

if delka >= 8 and cisla >= 2:
    print("Silné heslo")
else:
    print("Slabé heslo")
