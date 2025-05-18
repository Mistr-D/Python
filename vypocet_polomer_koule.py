import math

def vypocet_polomer_koule(objem):
    """
    Vypočítá poloměr koule na základě zadaného objemu.

    :param objem: Objem koule (v jednotkách objemu)
    :return: Poloměr koule (v jednotkách délky)
    """
    if objem <= 0:
        raise ValueError("Objem musí být kladné číslo.")
    
    polomer = ((3 * objem) / (4 * math.pi)) ** (1/3)
    return polomer

try:
    objem = float(input("Zadejte objem koule: "))
    polomer = vypocet_polomer_koule(objem)
    print(f"Poloměr koule je přibližně: {polomer:.2f}")
except ValueError as e:
    print(f"Chyba: {e}")
