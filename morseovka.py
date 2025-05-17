# Slovník pro Morseovu abecedu
morseovka = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def text_do_morseovky(text):
    text = text.upper()
    preklad = []
    for znak in text:
        if znak in morseovka:
            preklad.append(morseovka[znak])
        else:
            preklad.append('?')  # Neznámý znak
    return ' '.join(preklad)

# Testovací vstup
vstup = "Ahoj svet"
vystup = text_do_morseovky(vstup)
print(f"Text: {vstup}")
print(f"Morseovka: {vystup}")