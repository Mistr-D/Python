spravne_jmeno = "admin"
spravne_heslo = "heslo123"

jmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")

if jmeno == spravne_jmeno and heslo == spravne_heslo:
    print("Přihlášení bylo úspěšné.")
else:
    print("Neplatné jméno nebo heslo.")
