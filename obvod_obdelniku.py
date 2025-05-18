def obvod_obdelniku(delka, sirka):

    return 2 * (delka + sirka)


if __name__ == "__main__":
    delka = float(input("Zadejte délku obdélníku: "))
    sirka = float(input("Zadejte šířku obdélníku: "))
    obvod = obvod_obdelniku(delka, sirka)
    print(f"Obvod obdélníku je: {obvod}")
