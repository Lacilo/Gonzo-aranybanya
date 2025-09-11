import os
import modulok

os.chdir(os.path.dirname(__file__))

usr = input("Kérem adja meg a felhasználónevét --> ")

if usr == "":
    usr = "vendég"

dulok.UserRead(usr)

felulet = "menü"

modulok.MenuKiiras()
modulok.KiIrasA(24)

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
            modulok.KiIrasA(24)

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
        print(f"Hiba: {e} \n\nNem található {parancsP[1]} nevű fájl vagy valamely\nparancs paraméterként megadott fájlnév helytelen")
        modulok.KiIrasA(13)
