import math

def delka_bocni_steny(delka_zakladny, vyska):

    return math.sqrt((delka_zakladny / 2) ** 2 + vyska ** 2)


if __name__ == "__main__":
    delka_zakladny = float(input("Zadejte délku strany základny: "))
    vyska = float(input("Zadejte výšku jehlanu: "))
    delka_steny = delka_bocni_steny(delka_zakladny, vyska)
    print(f"Délka boční stěny jehlanu je: {delka_steny:.2f}")