import math

def telesova_uhlopricka_krychle(a):

    if a <= 0:
        raise ValueError("Délka hrany krychle musí být kladné číslo.")
    return math.sqrt(3) * a

if __name__ == "__main__":
    try:
        a = float(input("Zadejte délku hrany krychle: "))
        uhlopricka = telesova_uhlopricka_krychle(a)
        print(f"Tělesová úhlopříčka krychle s hranou {a} je {uhlopricka:.2f}")
    except ValueError as e:
        print(e)
