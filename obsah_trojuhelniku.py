def obsah_trojuhelniku(a, v):

    return (a * v) / 2

# Příklad použití
if __name__ == "__main__":
    a = float(input("Zadejte délku základny trojúhelníku (a): "))
    v = float(input("Zadejte výšku trojúhelníku (v): "))
    print(f"Obsah trojúhelníku je: {obsah_trojuhelniku(a, v)}")