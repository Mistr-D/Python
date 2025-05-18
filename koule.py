import math

def objem_koule(polomer):
 
    return (4/3) * math.pi * polomer**3

def povrch_koule(polomer):

    return 4 * math.pi * polomer**2

if __name__ == "__main__":
    r = float(input("Zadejte poloměr koule: "))
    print(f"Objem koule: {objem_koule(r):.2f}")
    print(f"Povrch koule: {povrch_koule(r):.2f}")



