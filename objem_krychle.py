def objem_krychle(strana):

    if strana <= 0:
        raise ValueError("Délka strany krychle musí být kladné číslo.")
    return strana ** 3

if __name__ == "__main__":
    try:
        strana = float(input("Zadejte délku strany krychle: "))
        print(f"Objem krychle je: {objem_krychle(strana)}")
    except ValueError as e:
        print(f"Chyba: {e}")
