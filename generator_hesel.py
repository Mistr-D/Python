import random
import string

def random_string (length = 12, cisla = True, velka_pismena = True, znaky = True):
    characters = string.ascii_lowercase
    if cisla:
        characters += string.digits
    if velka_pismena:
        characters += string.ascii_uppercase
    if  znaky:
        characters += string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
print(random_string(12))