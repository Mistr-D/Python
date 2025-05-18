import math

def pythagorean_theorem(a, b):

    return math.sqrt(a**2 + b**2)

# Example usage
if __name__ == "__main__":
    a = float(input("Zadejte délku strany a: "))
    b = float(input("Zadejte délku strany b: "))
    c = pythagorean_theorem(a, b)
    print(f"Délka přepony je: {c}")