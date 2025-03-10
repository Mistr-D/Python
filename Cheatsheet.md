# Python Cheat Sheet
vytvořili: Solnař Alex, Linka Tomáš, Hruška David

## Základní syntaxe
```python
# Komentář
print("Hello, World!")  # Výpis na obrazovku
```

## Proměnné a datové typy
```python
x = 10          # Celé číslo
pi = 3.14       # Desetinné číslo
text = "Ahoj"   # Řetězec
je_pravda = True  # Boolean
```

## Podmínky
```python
if x > 5:
    print("x je větší než 5")
elif x == 5:
    print("x je 5")
else:
    print("x je menší než 5")
```

## Smyčky
```python
# For loop
for i in range(5):
    print(i)

# While loop
x = 0
while x < 5:
    print(x)
    x += 1
```

## Funkce
```python
def soucet(a, b):
    return a + b

print(soucet(3, 4))
```

## Seznamy
```python
seznam = [1, 2, 3, 4, 5]
print(seznam[0])  # První prvek
seznam.append(6)  # Přidání prvku
```

## Slovníky
```python
data = {"jmeno": "Jan", "vek": 30}
print(data["jmeno"])  # Přístup k hodnotě
```

## Třídy a objekty
```python
class Clovek:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def predstav_se(self):
        print(f"Jmenuji se {self.jmeno} a je mi {self.vek} let.")

osoba = Clovek("Petr", 25)
osoba.predstav_se()
```

## Práce se soubory
```python
# Zápis do souboru
with open("soubor.txt", "w") as f:
    f.write("Hello, svět!")

# Čtení ze souboru
with open("soubor.txt", "r") as f:
    obsah = f.read()
    print(obsah)
```

## Import modulů
```python
import math
print(math.sqrt(16))  # Druhá odmocnina
```

## Výjimky
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Chyba: dělení nulou")
```

## Lambda funkce
```python
soucet = lambda a, b: a + b
print(soucet(3, 4))
```

## Matematické operace (math)
```python
import math
print(math.pi)  # Pí
print(math.sin(math.radians(30)))  # Sinus 30°
print(math.factorial(5))  # Faktoriál
```

## Náhodná čísla (random)
```python
import random
print(random.randint(1, 10))  # Náhodné číslo mezi 1 a 10
print(random.choice(["jablko", "banán", "třešeň"]))  # Náhodný prvek ze seznamu
```

## Práce s časem (time)
```python
import time
print(time.time())  # Aktuální čas v sekundách od epochy
print(time.ctime())  # Formátovaný aktuální čas

time.sleep(2)  # Pauza na 2 sekundy
```

## Práce s API (requests)
```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # HTTP status kód
print(response.json())  # Obsah odpovědi v JSON formátu
```