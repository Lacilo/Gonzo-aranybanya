import os

def KiIrasT(felulet):
    szel = os.get_terminal_size().columns

    os.system('cls')
    title = f"QuickLift 1.0 - "
    print((szel//2 - (len(title) + len(felulet)//2) + 5) * " ", title + felulet)
    print(os.get_terminal_size().columns * "-" + "\n\n")

def KiIrasA(csokk = 9):
    mag = os.get_terminal_size().lines

    print((mag - csokk) * "\n")

def Create(fajlnev = "", datum = ""):
    KiIrasT("létrehozás")

    if fajlnev == "_" and datum == "_":

        print("Az adatok beolvasásához, és az azokból való adattábla létrehozására\nhasználja a create parancsot.\n\nPontos használat:\n\ncreate [beolvasandó fájl].txt [dátum (formátum = 2025_09_06)]")
        KiIrasA(15)
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
    KiIrasT("törlés")
    if fajlnev != "_" and b == "_":
        if fajlnev[-5:] != ".html":
            print(f"Hiba: úgy néz ki a megadott fájl nem html fájl, a törléshez adjon meg egy html fájlt")

            KiIrasA(11)
        else:
            os.remove(f"../web/adatok/{fajlnev}")
    else:
        print("Egy adattáblázat törléséhez kérem adja meg a html fájl nevét (a dátumot) \nebben a formátumban: \n\ndelete [fájlnév].html pl.: delete 2025_09_06.html")
        KiIrasA(13)

    return "törlés"

def List(a, b):
    KiIrasT("listázás")

    terkoz = 17

    print("■ html fájlok")
    egyebFajl = []

    for fajl in os.listdir("../web/adatok"):
        if fajl[-5:] == ".html":
            print("│")
            print("├─── " + fajl)

            terkoz += 2
        else:
            egyebFajl.append(fajl)
    print("│")
    print("└──■")

    print("\n\n■ egyéb fájlok")

    for fajl in egyebFajl:
        print("│")
        print("├─── " + fajl)
        
        terkoz += 2
    print("│")
    print("└──■")

    KiIrasA(terkoz)

    return "listázás"