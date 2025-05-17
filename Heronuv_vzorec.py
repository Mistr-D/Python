import math

def heron_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2  
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        raise ValueError("The given sides do not form a valid triangle.")

if __name__ == "__main__":
    try:
        a = float(input("zadejte první stranu: "))
        b = float(input("Zadejte druhou stranu: "))
        c = float(input("Zadejte třetí stranu: "))
        area = heron_area(a, b, c)
        print(f"Obsah trojuhelniku je: {area}")
    except ValueError as e:
        print(e)