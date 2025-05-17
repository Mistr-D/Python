import math

def plocha_podstavy_jehlanu(a, b):
    return a * b
if __name__ == "__main__":
    a = float(input("Zadejte délku první strany podstavy (a): "))
    b = float(input("Zadejte délku druhé strany podstavy (b): "))
    plocha = plocha_podstavy_jehlanu(a, b)
    print(f"Plocha podstavy jehlanu je: {plocha}")