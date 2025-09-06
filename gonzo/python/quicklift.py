import os
import modulok

usr = input("Kérem adja meg a felhasználónevét --> ")

felulet = "menü"

while True:
    parancsNyers = (input(f"\n{usr} /{felulet}/-$ ")).capitalize() + " _ _"
    parancsP = parancsNyers.split(" ")

    felulet = "menü"

    try:
        if parancsP[0] != "":
            os.system('cls')
            felulet = eval("modulok." + parancsP[0] + f"('{parancsP[1]}', '{parancsP[2]}')")
        else:
            os.system('cls')
    except NameError:
        print(f"Nem található ilyen parancs: {parancsP[0]}")

    except AttributeError:
        print(f"Nem található ilyen parancs: {parancsP[0]}")

    except FileNotFoundError:
        print(f"Hiba: Nem található {parancsP[1]} nevű fájl ezen az elérési úton: \n\n'gonzo/web/adatok/\n\nvagy valamely parancs paraméterként megadott útvonal helytelen")