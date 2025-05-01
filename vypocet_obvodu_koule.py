import math

def vypocet_obvodu_koule(polomer):
    if polomer <= 0:
        raise ValueError("Poloměr musí být kladné číslo.")
    obvod = 2 * math.pi * polomer
    return obvod

# Příklad použití
try:
    polomer = float(input("Zadejte poloměr koule: "))
    obvod = vypocet_obvodu_koule(polomer)
    print(f"Obvod koule s poloměrem {polomer} je {obvod:.2f}")
except ValueError as e:
    print(f"Chyba: {e}")