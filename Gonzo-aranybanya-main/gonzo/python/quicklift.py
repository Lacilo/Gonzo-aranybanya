def Info():
    opciok = {
        "help":"Ennek a menünek a megjelenítése",
        "clear":"Képernyő letiszítása",
        "editor":"",
    }

    for parancs in opciok:
        print(f"{parancs} - {opciok[parancs]}")


usr = input("Kérem adja meg a felhasználónevét --> ")

global felulet
felulet = "menü"

while True:
    parancs = (input(f"\n{usr} /{felulet}/-$ ")).capitalize() + "()"

    try:
        eval(parancs)
    except NameError:
        print("Nem található ilyen parancs!")