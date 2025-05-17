def obvod_trojuhelniku(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Délky stran musí být kladné číslo.")
    return a + b + c

# Příklad použití
try:
    a = float(input("Zadejte délku první strany trojúhelníku: "))
    b = float(input("Zadejte délku druhé strany trojúhelníku: "))
    c = float(input("Zadejte délku třetí strany trojúhelníku: "))
    print(f"Obvod trojúhelníku je: {obvod_trojuhelniku(a, b, c)}")
except ValueError as e:
    print(f"Chyba: {e}")