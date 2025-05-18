text = input("Zadej text: ").lower()
frekvence = {}

for znak in text:
    if znak.isalpha():
        frekvence[znak] = frekvence.get(znak, 0) + 1

for pismeno in sorted(frekvence):
    print(pismeno, ":", frekvence[pismeno])
print("Celkový počet písmen:", sum(frekvence.values()))
print("Celkový počet všech znaků:", len(text))