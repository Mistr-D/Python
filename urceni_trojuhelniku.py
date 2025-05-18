a = float(input("Zadej stranu a: "))
b = float(input("Zadej stranu b: "))
c = float(input("Zadej stranu c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Rovnostranný trojúhelník")
    elif a == b or b == c or a == c:
        print("Rovnoramenný trojúhelník")
    else:
        print("Různostranný trojúhelník")
else:
    print("Z těchto stran nelze sestavit trojúhelník.")
