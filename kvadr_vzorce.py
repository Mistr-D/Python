import math

def cuboid_properties(length, width, height):
    volume = length * width * height
    
    surface_area = 2 * (length * width + width * height + height * length)
    
    body_diagonal = math.sqrt(length**2 + width**2 + height**2)
    
    return volume, surface_area, body_diagonal

print("Co chcete vypočítat?")
print("1. Objem")
print("2. Povrch")
print("3. Tělesová úhlopříčka")
volba = input("Zadejte svou volbu (1/2/3): ")

length = float(input("Zadejte délku kvádru: "))
width = float(input("Zadejte šířku kvádru: "))
height = float(input("Zadejte výšku kvádru: "))

objem, povrch, telesova_uhlopricka = cuboid_properties(length, width, height)

if volba == "1":
    print(f"Objem: {objem}")
elif volba == "2":
    print(f"Povrch: {povrch}")
elif volba == "3":
    print(f"Tělesová úhlopříčka: {telesova_uhlopricka}")
else:
    print("Neplatná volba.")
