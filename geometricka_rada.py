def geometricka_rada(a, r, n):

    rada = [a * (r ** i) for i in range(n)]
    return rada

prvni_clen = float(input("Zadejte první člen řady (a): "))
kvocient = float(input("Zadejte kvocient (r): "))
pocet_clenu = int(input("Zadejte počet členů řady (n): "))

rada = geometricka_rada(prvni_clen, kvocient, pocet_clenu)
print("Geometrická řada:", rada)