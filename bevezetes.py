"""minta
(a stílus kialakítása nem része a feladatnak, de a sorszámok és betűjelek kiíratása igen):
I/A:
Játékos neve: Gandalf
szerepkör: varázsló

I/B:
Üdvözlünk Gandalf, 2 életed van!
A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
Játékos neve és szerepköre!  (2p)
B.	A program az adatbekérés után írasson ki egy üdvözlést az alábbiak alapján!
Amennyiben „varázsló” a játékosunk, 2 élete van.
Amennyiben „harcos” a játékosunk, 10 életereje van.
Amennyiben ismeretlen a játékosunk szerepköre, 8 életereje van. (4p)
A mintának megfelelően jelenítette meg az eredményt, és kérte be az adatokat. (1p)
"""
def adatbeker():
    jatekos_nev=input("Játékos neve: ")
    szerep_kör=input("szerepkör: ")
    elet_pont=0
    if szerep_kör=="varázsló":
        elet_pont=2
    elif szerep_kör=="harcos":
        elet_pont=10
    else:
        elet_pont=8
    print(f"Üdvözlünk {jatekos_nev}, {elet_pont} életed van!")