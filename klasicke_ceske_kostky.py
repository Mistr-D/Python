import random

def hod_kostkami():
    return random.randint(1, 6), random.randint(1, 6)

def vyhodnot_hod(k1, k2):
    soucet = k1 + k2
    if k1 == 6 and k2 == 6:
        return "vyhra", soucet
    elif k1 == 1 and k2 == 1:
        return "prohra", soucet
    else:
        return "normal", soucet

def hraj_hru(jmena_hracu, pocet_kol):
    pocet_hracu = len(jmena_hracu)
    skore = [0] * pocet_hracu
    for kolo in range(1, pocet_kol + 1):
        print(f"\n--- Kolo {kolo} ---")
        vysledky = []
        for i in range(pocet_hracu):
            input(f"{jmena_hracu[i]}, stiskni Enter pro hod kostkami...")
            k1, k2 = hod_kostkami()
            stav, soucet = vyhodnot_hod(k1, k2)
            print(f"{jmena_hracu[i]} hodil: {k1} a {k2} (součet: {soucet})")
            vysledky.append((i, stav, soucet))

        for idx, stav, soucet in vysledky:
            if stav == "vyhra":
                skore[idx] += 10
            elif stav == "prohra":
                skore[idx] -= 5
            else:
                skore[idx] += soucet

        print("Skóre po kole:", ', '.join(f"{jmena_hracu[i]}: {skore[i]}" for i in range(pocet_hracu)))

    max_skore = max(skore)
    vyherci = [jmena_hracu[i] for i, s in enumerate(skore) if s == max_skore]
    if len(vyherci) == 1:
        print(f"\nVítěz je {vyherci[0]} se skóre {max_skore}!")
    else:
        print(f"\nRemíza mezi hráči: {', '.join(vyherci)} se skóre {max_skore}!")

pocet_hracu = int(input("Zadej počet hráčů: "))
jmena_hracu = []
for i in range(1, pocet_hracu + 1):
    jmeno = input(f"Zadej jméno hráče {i}: ")
    jmena_hracu.append(jmeno)
pocet_kol = int(input("Zadej počet kol: "))
hraj_hru(jmena_hracu, pocet_kol)

