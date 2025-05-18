def povrch_krychle(a):

    if a <= 0:
        raise ValueError("Délka hrany musí být kladné číslo.")
    return 6 * a * a

if __name__ == "__main__":
    try:
        hrana = float(input("Zadejte délku hrany krychle: "))
        print(f"Povrch krychle je: {povrch_krychle(hrana)}")
    except ValueError as e:
        print(f"Chyba: {e}")
