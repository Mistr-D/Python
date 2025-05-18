rim = input("Zadej římské číslo (I, V, X, L, C, D, M): ").upper()

hodnoty = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100,
    'D': 500, 'M': 1000
}

cislo = 0
predchozi = 0

for znak in reversed(rim):
    hodnota = hodnoty.get(znak, 0)
    if hodnota < predchozi:
        cislo -= hodnota
    else:
        cislo += hodnota
        predchozi = hodnota

print("číslo:", cislo)
