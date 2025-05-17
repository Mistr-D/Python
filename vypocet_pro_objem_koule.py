import math

def vypocet_objemu_koule(polomer):
    """
    Funkce pro výpočet objemu koule na základě zadaného poloměru.
    :param polomer: Poloměr koule
    :return: Objem koule
    """
    if polomer < 0:
        raise ValueError("Poloměr nemůže být záporný.")
    objem = (4/3) * math.pi * (polomer ** 3)
    return objem

# Příklad použití
try:
    polomer = float(input("Zadejte poloměr koule: "))
    objem = vypocet_objemu_koule(polomer)
    print(f"Objem koule s poloměrem {polomer} je {objem:.2f}.")
except ValueError as e:
    print(f"Chyba: {e}")