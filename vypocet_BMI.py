vaha = float(input("Zadej svou váhu (kg): "))
vyska = float(input("Zadej svou výšku (m): "))

bmi = vaha / (vyska ** 2)
print(f"Tvé BMI je {bmi:.2f}")

if bmi < 18.5:
    print("Podváha")
elif bmi < 25:
    print("Normální váha")
elif bmi < 30:
    print("Nadváha")
else:
    print("Obezita")
