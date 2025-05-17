def delka_vysky_trojuhelniku(base, area):

    if base <= 0 or area <= 0:
        raise ValueError("Base and area must be positive numbers.")
    
    height = (2 * area) / base
    return height

# Example usage
try:
    base = float(input("Zadejte délku základny trojúhelníku: "))
    area = float(input("Zadejte obsah trojúhelníku: "))
    vyska = delka_vysky_trojuhelniku(base, area)
    print(f"Délka výšky trojúhelníku je: {vyska}")
except ValueError as e:
    print(f"Chyba: {e}")