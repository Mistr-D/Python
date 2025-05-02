def objem_ctverce(a, v):
  
    if a <= 0 or v <= 0:
        raise ValueError("Délka strany a výška musí být kladná čísla.")
    return a**2 * v

# Příklad použití
if __name__ == "__main__":
    try:
        a = float(input("Zadejte délku strany čtverce (a): "))
        v = float(input("Zadejte výšku hranolu (v): "))
        print(f"Objem čtvercového hranolu je: {objem_ctverce(a, v)}")
    except ValueError as e:
        print(f"Chyba: {e}")