from datetime import datetime

def overeni_veku():
    try:
        datum_narozeni = input("Zadejte svůj datum narození (ve formátu DD.MM.RRRR): ")
        narozeni = datetime.strptime(datum_narozeni, "%d.%m.%Y")
        dnes = datetime.now()
        vek = dnes.year - narozeni.year - ((dnes.month, dnes.day) < (narozeni.month, narozeni.day))
        if vek >= 18:
            print("Jste plnoletý/á.")
        else:
            print("Nejste plnoletý/á.")
    except ValueError:
        print("Zadejte platné datum ve formátu DD.MM.RRRR.")

if __name__ == "__main__":
    overeni_veku()