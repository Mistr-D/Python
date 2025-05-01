import math

def vypocet_obsha_koule(polomer):
    """
    Funkce pro výpočet povrchu koule.
    :param polomer: Poloměr koule v cm
    :return: Povrch koule v cm²
    """
    if polomer <= 0:
        raise ValueError("Poloměr musí být kladné číslo.")
    povrch = 4 * math.pi * polomer**2
    return povrch

# Příklad použití
try:
    polomer = float(input("Zadejte poloměr koule v cm: "))
    povrch = vypocet_obsha_koule(polomer)
    print(f"Povrch koule o poloměru {polomer} cm je přibližně {povrch:.2f} cm².")
except ValueError as e:
    print(f"Chyba: {e}")