"""minta:
II/A, B, C:
           	FEJ-ÍRÁS-ÍRÁS-ÍRÁS-FEJ-ÍRÁS-ÍRÁS
II/D, E:
           	A fejek száma: 2.
A fejek.txt tartalma:
II/F:
A fejek száma: 2.

A.	Írasson ki a konzolra kötőjellel (-) elválasztva 7 pénzérmével való dobást véletlen számsorozat alapján a mintának megfelelően! (4p)
B.	A generált értékeket tárolja lista adatszerkezetben logikai típusokkal (0: írás, 1: fej)! (1p)
C.	A „–” jel csak az értékek között szerepeljen (a végén ne)! (2p)
D.	Írjon függvényt fejek_szama néven, amiben számolja meg, hogy hány olyan elem van, ami fej (1). A visszatérési érték legyen egy egész szám! (3p)
E.	A fejek_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
F.	A fejek_szama függvény eredményét írassa ki a mintának megfelelően a fejek.txt nevű fájlba, amit file_kiir nevű metódusban fogalmazzon meg! (2p)
"""
import random

logikai_lista = []
szoveges_lista = []
def fej_iras():
    i=0
    while i<7:
        logikai_lista.append(random.randint(0,1))
        if logikai_lista[i]==1:
            szoveges_lista.append("ÍRÁS")
        elif logikai_lista[i]==0:
            szoveges_lista.append("FEJ")
        i+=1
    print("-".join(str(szamok)for szamok in logikai_lista))
    print("-".join(szoveg for szoveg in szoveges_lista))
    return logikai_lista
def fejek_szama():
    i=0
    fejek_db=0
    while i<len(logikai_lista):
        if logikai_lista[i]==0:
            fejek_db+=1
        i+=1
    return fejek_db
    konzol_kiir(fejek_db)
    fajl_kiir(fejek_db)
def konzol_kiir(fejek_db):
    print(f"A fejek száma: {fejek_db}")

def fajl_kiir(fejek_db):
    fajlom=open("fejek.txt","w",encoding="utf-8")
    fajlom.write(f"a fejek txt tartalma: {fejek_db}")




