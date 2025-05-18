import random

def hadani_cisla_hra():
    print("Vítejte ve hře Had!")
    print("Cílem hry je uhodnout správné číslo mezi 1 a 100.")
    
    tajne_cislo = random.randint(1, 100)
    pokusy = 0

    while True:
        try:
            tip = int(input("Zadejte svůj tip: "))
            pokusy += 1

            if tip < tajne_cislo:
                print("Had říká: Vaše číslo je příliš malé.")
            elif tip > tajne_cislo:
                print("Had říká: Vaše číslo je příliš velké.")
            else:
                print(f"Gratulujeme! Uhodli jste správné číslo {tajne_cislo} za {pokusy} pokusů.")
                break
        except ValueError:
            print("Prosím, zadejte platné číslo.")

if __name__ == "__main__":
    hadani_cisla_hra()