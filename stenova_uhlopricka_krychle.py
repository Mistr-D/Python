import math

def stenova_uhlopricka_krychle(a):

    if a <= 0:
        raise ValueError("Délka hrany krychle musí být kladné číslo.")
    return math.sqrt(2) * a

if __name__ == "__main__":
    try:
        a = float(input("Zadejte délku hrany krychle: "))
        uhlopricka = stenova_uhlopricka_krychle(a)
        print(f"Délka stěnové úhlopříčky krychle je: {uhlopricka:.2f}")
    except ValueError as e:
        print(e)
