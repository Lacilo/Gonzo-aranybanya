import os
import webbrowser

def UserRead(user):
    global usr
    usr = user

def KiIrasT(felulet):
    szel = os.get_terminal_size().columns

    os.system('cls')
    title = f"QuickLift 1.0 - "
    print((szel//2 - (len(title) + len(felulet)//2) + 5) * " ", title + felulet)
    print(os.get_terminal_size().columns * "-" + "\n\n")

def KiIrasA(csokk = 9):
    mag = os.get_terminal_size().lines

    print((mag - csokk) * "\n")

def DatumFrissites():
    foHtml = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adatok</title>
    <link rel="stylesheet" href='../web/css/style.css'>
</head>
<body>
    <script>
    </script>

    <nav>
        <div id="logo"><a href="index.html"><img src="./img/logo1.png" height="60" alt=""></a></div>
        <div id="linkek">
            <a class="link" href="gonzo.html">Gonzo</a>
            <a class="link" href="adatok.html">Adatok</a>
            <a class="link" href="kapcsolat.html">Fejlesztők</a>
        </div>
    </nav>
    <div id='datumok'>

"""

    for datum in os.listdir("../adatok/"):
                if datum[-5:] == ".html":
                    foHtml += f'\n\t<a href="../adatok/{datum}">{datum}</a><br>'

    foHtml += """</div><footer>
        <p>Az oldal kizárólag tanulmányi okokból készült</p>
    </footer>
</body>
</html>"""
    
    with open("../web/adatok.html", "w", encoding="utf-8") as file:
        file.write(foHtml)

def Create(datum = "", fajlnev = "", m = "c"):
    if m == "c" and datum in os.listdir("../adatok/"):
        KiIrasT("létrehozás")
        print("Már létezik ilyen fájl! Szerkesztéshez kérem használja az edit parancsot. \nMost nem változott semmi.")
        KiIrasA(11)
    else:
        KiIrasT("létrehozás")

        if fajlnev == "_" and datum == "_":

            print(f"Az adatok beolvasásához, és az azokból való adattábla létrehozására\nhasználja a create parancsot.\n\nPontos használat:\n\ncreate [fájlnév (a program megfelelő működéséhez mindenkéeppen\ndátumot adjon meg fájlnévnek) (formátum = 2025_09_06.html)] [beolvasandó fájl].txt \n\npl.: {usr} /létrehozás/-$ create 2025_05_06.html fajl.txt")
            KiIrasA(18)
        else:
            tablaKod = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{datum[:-5]}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href='../web/css/adat.css'>
    <link rel="stylesheet" href='../web/css/style.css'>
</head>
<body>
    <nav class="container-fluid">
        <div id="logo"><a href="../web/index.html"><img src="../web/img/logo1.png" height="60" alt=""></a></div>
        <div id="linkek">
            <a class="link" href="../web/gonzo.html">Gonzo</a>
            <a class="link" href="../web/adatok.html">Adatok</a>
            <a class="link" href="../web/kapcsolat.html">Fejlesztők</a>
        </div>
    </nav>
    <table class="table table-bordered table-striped text-center">   
        <tr class="table-primary">  <th>Gép típusa</th> <th>Állapot</th> <th>Időpont</th> <th>Kapitány</th> <th>Első tiszt/Másodpilóta</th> <th>Kifutó</th> <th>Úticél</th> <th>Indulási reptér</th>  </tr>""" # ITT MÉG CSAK ELINDULT A TÁBLÁZAT KÉSŐBB BE KELL ZÁRNI

            with open("../" + fajlnev, "r", encoding="utf-8") as file:
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

                    tablaKod += f"\n\t\t<tr>  <td>{tipus}</td> <td>{allapot}</td> <td>{ido}</td> <td>{kapitany}</td> <td>{masodP}</td> <td>{kifuto}</td> <td>{uticel}</td> <td>{indR}</td>  </tr>"

            tablaKod += """
    </table>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

            with open("../adatok/" + datum, "w", encoding="utf-8") as file:
                file.write(tablaKod)

            DatumFrissites()

            print(f"Sikeresen létrehoztuk a {datum}.html fájlt!")

            KiIrasA(10)

    return "létrehozás"

def Delete(fajlnev, b):
    KiIrasT("törlés")
    if fajlnev != "_" and b == "_":
        if fajlnev[-5:] != ".html":
            print(f"Hiba: úgy néz ki a megadott fájl nem html fájl, a törléshez adjon meg egy html fájlt")

            KiIrasA(11)

        else:
            os.remove(f"../adatok/{fajlnev}")
            DatumFrissites()

            print(f"A {fajlnev} fájlt sikeresen eltávolítottuk!")

            KiIrasA(10)

    else:
        print(f"Egy adattáblázat törléséhez kérem adja meg a html fájl nevét (a dátumot) \nebben a formátumban: \n\ndelete [fájlnév].html pl.: {usr} /törlés/-$ delete 2025_09_06.html")
        KiIrasA(13)
    
    return "törlés"

def List(a, b):
    KiIrasT("listázás")

    terkoz = 12

    print("■ html fájlok")

    mappa = os.listdir("../adatok/")

    if len(mappa) == 0:
        terkoz = 10

    for i, fajl in enumerate(mappa):
        if fajl[-5:] == ".html":
            if i == len(mappa) -1:
                print("│")
                print("└─── " + fajl)
            else:    
                print("│")
                print("├─── " + fajl)

                terkoz += 2

    KiIrasA(terkoz)

    return "listázás"

def MenuKiiras():
    KiIrasT("menü")

    print(f"Parancsok:\n\nexit - kilépés a programból\ncreate - fájlból adattáblázat létrehozása\nedit - már létrehozott adattáblázat szerkesztése(adatainak kicserélése)\ndelete - már létrehozott adattáblázat törlése\nlist - létrehozott adattáblázatok neveinek listázása/megjeleítése\nopen - Az adattáblázatokat megjelenítő weblap megnyitása\n       open parancs után fájlnév megadásával az adott nevű adattáblázat megnyitása\n\nA parancsok használatának további részleteiért\n(amelyik parancsnál vannak részletek, a list-nél nincs)\nÍrja be a használni kívánt parancsot\n\npl.: {usr} /menü/-$ create")

def Open(fajl, b):
    if fajl == "_":
        relUtv = "../web/adatok.html"

        absUtv = os.path.abspath(relUtv)

        webbrowser.open(f"file://{absUtv}")

        KiIrasT("web")
        print("Az adattáblákat tartalmazó weblapot sikeresen megnyitottuk!")
        KiIrasA(10)
    else:
        relUtv = f"../adatok/{fajl}"

        absUtv = os.path.abspath(relUtv)

        webbrowser.open(f"file://{absUtv}")

        KiIrasT("web")
        print("Az adattáblát tartalmazó weblapot sikeresen megnyitottuk!")
        KiIrasA(10)

    return "web"

def Edit(datum, fajlnev):
    if datum != "_" and fajlnev != "_":
        Create(datum, fajlnev, "e")
        
        os.system('cls')
        KiIrasT("szerkesztés")
        print(f"Sikeresen szerkesztettük a {datum} fájlt!")
        KiIrasA(10)

    else:
        KiIrasT("szerkesztés")
        print(f"A fájl szerkesztéséhez adja meg a szerkeszteni kívánt adattáblát(html fájlt)\nmajd a txt fájlt ami tartalmazza az új adatokat\n\npl.: {usr} /szerkesztés/-$ edit 2025_01_01.html ujadatok.txt")
        KiIrasA(13)

    return "szerkesztés"

def Exit(a, b):
    exit()