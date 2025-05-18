n = int(input("Zadej číslo: "))

if n < 2:
    print("Číslo není prvočíslo.")
else:
    je_prvocislo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            je_prvocislo = False
            break

    if je_prvocislo:
        print("Číslo je prvočíslo.")
    else:
        print("Číslo není prvočíslo.")
