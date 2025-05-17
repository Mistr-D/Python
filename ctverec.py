print("1. obsah čtverce")
print("2. obvod čtverce")

choice = input()
def obsah_ctverce(strana_cm):
    return strana_cm ** 2

if choice == "1":

    try:
        strana = float(input("Zadejte délku strany čtverce v cm: "))
        if strana < 0:
            print("Délka strany nemůže být záporná.")
        else:
            obsah = obsah_ctverce(strana)
            print(f"Obsah čtverce o straně {strana} cm je {obsah} cm².")
    except ValueError:
        print("Prosím, zadejte platné číslo.")

if choice == "2":
    def obvod_ctverce(strana):
        return 4 * strana

    try:
        strana = float(input("Zadejte délku strany čtverce: "))
        if strana <= 0:
            print("Délka strany musí být kladné číslo.")
        else:
            print(f"Obvod čtverce je: {obvod_ctverce(strana)}")
    except ValueError:
        print("Zadejte platné číslo.")