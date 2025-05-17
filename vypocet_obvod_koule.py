import math

def vypocet_obvodu_koule(polomer_cm):
    """
    Vypočítá obvod koule na základě zadaného poloměru v centimetrech.
    
    :param polomer_cm: Poloměr koule v centimetrech
    :return: Obvod koule v centimetrech
    """
    return 2 * math.pi * polomer_cm

# Příklad použití
if __name__ == "__main__":
    try:
        polomer = float(input("Zadejte poloměr koule v cm: "))
        if polomer < 0:
            print("Poloměr nemůže být záporný.")
        else:
            obvod = vypocet_obvodu_koule(polomer)
            print(f"Obvod koule s poloměrem {polomer} cm je přibližně {obvod:.2f} cm.")
    except ValueError:
        print("Zadejte platné číslo pro poloměr.")