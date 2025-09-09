import os
import modulok

os.chdir(os.path.dirname(__file__))

usr = input("Kérem adja meg a felhasználónevét --> ")
modulok.UserRead(usr)

felulet = "menü"

modulok.MenuKiiras()
modulok.KiIrasA(22)

while True:
    parancsNyers = (input(f"\n{usr} /{felulet}/-$ ")).capitalize() + " _ _"
    parancsP = parancsNyers.split(" ")

    felulet = "menü"

    try:
        if parancsP[0] != "":
            os.system('cls')

            felulet = eval("modulok." + parancsP[0] + f"('{parancsP[1]}', '{parancsP[2]}')")

        else:
            modulok.MenuKiiras()
            modulok.KiIrasA(22)

    except NameError:
        modulok.KiIrasT("menü")
        print(f"Nem található ilyen parancs: {parancsP[0].lower()}")
        modulok.KiIrasA(10)

    except AttributeError:
        modulok.KiIrasT("menü")
        print(f"Nem található ilyen parancs: {parancsP[0].lower()}")
        modulok.KiIrasA(10)

    except FileNotFoundError as e:
        modulok.KiIrasT("menü")
        print(f"Hiba: {e} Nem található {parancsP[1]} nevű fájl ezen az elérési úton: \n\n'gonzo/python/adatok/'\n\nvagy valamely parancs paraméterként megadott útvonal helytelen")
        modulok.KiIrasA(14)