text = input("Zadej text: ")
samohlasky = "aeiouáéíóúůAEIOUÁÉÍÓÚŮ"
pocet = 0

for znak in text:
    if znak in samohlasky:
        pocet += 1

print("Počet samohlásek:", pocet)
