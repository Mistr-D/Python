def obsah_ctverce(strana_cm):

    return strana_cm ** 2

try:
    strana = float(input("Zadejte délku strany čtverce v cm: "))
    if strana < 0:
        print("Délka strany nemůže být záporná.")
    else:
        obsah = obsah_ctverce(strana)
        print(f"Obsah čtverce o straně {strana} cm je {obsah} cm².")
except ValueError:
    print("Prosím, zadejte platné číslo.")