print("1 - Celsius na Fahrenheit")
print("2 - Fahrenheit na Celsius")

volba = input("Zadej volbu: ")

if volba == "1":
    c = float(input("Zadej teplotu ve °C: "))
    f = c * 9/5 + 32
    print(f"Teplota ve °F: {f}")
elif volba == "2":
    f = float(input("Zadej teplotu ve °F: "))
    c = (f - 32) * 5/9
    print(f"Teplota ve °C: {c}")
else:
    print("Neplatná volba.")
