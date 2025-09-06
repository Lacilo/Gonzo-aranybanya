import os

def Info(a, b):
    opciok = {
        "help":"Ennek a menünek a megjelenítése",
        "clear":"Képernyő letiszítása",
        "editor":"",
    }

    for parancs in opciok:
        print(f"{parancs} - {opciok[parancs]}")

def Create(fajlnev = "", datum = ""):
    if fajlnev == "_" and datum == "_":

        print("Az adatok beolvasásához, és az azokból való adattábla létrehozására\nhasználja a create parancsot.\n\nPontos használat:\n\ncreate [beolvasandó fájl].txt [dátum (formátum = 2025_09_06)]")
    else:
        tablaKod = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>datum</title>
</head>
<body>
    <table>   
        <tr>  <th>Gép típusa</th> <th>Állapot</th> <th>Időpont</th> <th>Kapitány</th> <th>Első tiszt/Másodpilóta</th> <th>Kifutó</th> <th>Úticél</th> <th>Indulási reptér</th>  </tr>""" # ITT MÉG CSAK ELINDULT A TÁBLÁZAT KÉSŐBB BE KELL ZÁRNI

        with open("../web/adatok/" + fajlnev, "r", encoding="utf-8") as file:
            for sorNy in file:
                sorH = sorNy.split(";")
                tipus = sorH[0]
                allapot = sorH[1]
                ido = sorH[2]
                kapitany = sorH[3]
                masodP = sorH[4]
                kifuto = sorH[5]
                
                if allapot == "Érkezés":
                    indR = sorH[6]
                    uticel = "-"
                else:
                    uticel = sorH[6]
                    indR = "-"

                tablaKod += f"\n\t\t<tr>  <th>{tipus}</th> <th>{allapot}</th> <th>{ido}</th> <th>{kapitany}</th> <th>{masodP}</th> <th>{kifuto}</th> <th>{uticel}</th> <th>{indR}</th>  </tr>"

        tablaKod += """
    </table>
</body>
</html>
"""

        with open("../web/adatok/" + datum + ".html", "w", encoding="utf-8") as file:
            file.write(tablaKod)
    
    return "létrehozás"

def Delete(fajlnev, b):
    if fajlnev != "_" and b == "_":
        if fajlnev[-5:] != ".html":
            print(f"Hiba: úgy néz ki a megadott fájl nem html fájl, a törléshez adjon meg egy html fájlt")
        else:
            os.remove(f"../web/adatok/{fajlnev}")
    else:
        print("Egy adattáblázat törléséhez kérem adja meg a html fájl nevét (a dátumot) \nebben a formátumban: \n\ndelete [fájlnév].html pl.: delete 2025_09_06.html")
        
    return "törlés"

def List(a, b):
    print("■ html fájlok")
    egyebFajl = []

    for fajl in os.listdir("../web/adatok/"):
        if fajl[-5:] == ".html":
            print("│")
            print("├─── " + fajl)
        else:
            egyebFajl.append(fajl)
    print("│")
    print("└──■")

    print("\n\n■ Egyéb fájlok")

    for fajl in egyebFajl:
        print("│")
        print("├─── " + fajl)
    print("│")
    print("└──■")

    return "listázás"