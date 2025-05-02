def obvod_ctverce(strana):

    return 4 * strana

# Příklad použití
if __name__ == "__main__":
    try:
        strana = float(input("Zadejte délku strany čtverce: "))
        if strana <= 0:
            print("Délka strany musí být kladné číslo.")
        else:
            print(f"Obvod čtverce je: {obvod_ctverce(strana)}")
    except ValueError:
        print("Zadejte platné číslo.")