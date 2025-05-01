print("1. Sčítání")
print("2. Odčítání")
print("3. Násobení")
print("4. Dělení")

volba = int(input("Zadejte číslo operace (1-4): "))
A = int(input("Zadejte první číslo: "))
B = int(input("Zadejte druhé číslo: "))

if volba == 1:
    print(A + B)
if volba == 2:
    print(A - B)
if volba == 3:
    print(A * B)
if volba == 4:
    if B == 0:
        print("0")
    else:
        print(A / B)
    
