import random

def hod_kostkami(pocet_kostek):
    return [random.randint(1, 6) for _ in range(pocet_kostek)]

def vyhodnot_hod(hod):
    hod.sort()
    counts = {x: hod.count(x) for x in set(hod)}
    if len(counts) == 1:
        return "Pětka (všech 5 stejných)", 50
    elif 4 in counts.values():
        return "Čtyřka (4 stejné)", 40
    elif sorted(counts.values()) == [2, 3]:
        return "Full house (3 stejné + 2 stejné)", 30
    elif 3 in counts.values():
        return "Trojka (3 stejné)", 20
    elif list(counts.values()).count(2) == 2:
        return "Dvě dvojice", 15
    elif 2 in counts.values():
        return "Dvojice", 10
    elif hod == list(range(hod[0], hod[0]+5)):
        return "Postupka", 60
    else:
        return "Nic zvláštního", 0

def hra():
    print("Vítejte ve hře kostky podle cechovních pravidel!")
    pocet_hracu = int(input("Zadejte počet hráčů: "))
    hraci = []
    body = {}
    for i in range(pocet_hracu):
        jmeno = input(f"Zadejte jméno hráče {i+1}: ")
        hraci.append(jmeno)
        body[jmeno] = 0
    cilove_body = int(input("Zadejte, do kolika bodů se bude hrát: "))
    konec = False
    while not konec:
        for hrac in hraci:
            input(f"{hrac}, stiskněte Enter pro hod kostkami...")
            hod = hod_kostkami(5)
            print(f"{hrac} hodil: {hod}")
            vysledek, body_zisk = vyhodnot_hod(hod)
            print(f"Výsledek: {vysledek} (+{body_zisk} bodů)\n")
            body[hrac] += body_zisk
            if body[hrac] >= cilove_body:
                konec = True
        print("Aktuální skóre:")
        for hrac in hraci:
            print(f"{hrac}: {body[hrac]} bodů")
        if konec:
            print("\nNěkdo dosáhl cílového počtu bodů, hra končí!")
            break
    print("\nKonečné skóre:")
    for hrac in hraci:
        print(f"{hrac}: {body[hrac]} bodů")

if __name__ == "__main__":
    hra()
