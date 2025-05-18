import time

print("Digitální hodiny - stiskni Ctrl+C pro ukončení")
while True:
    print(time.strftime("%H:%M:%S"), end="\r")
    time.sleep(1)
