import time

sekundy = int(input("Zadej počet sekund: "))

while sekundy > 0:
    print(f"Zbývá: {sekundy} s", end="\r")
    time.sleep(1)
    sekundy -= 1

print("\nČas vypršel!")
