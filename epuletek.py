"""Az epulet.txt forrásállomány, épületek adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
Az epulet.txt állomány szerkezete:
·         az épület neve: pl: Centrum LIM
·         az épület városa: pl.: Varsó
·         az épület országa: pl.: Lengyelország
·         az épület magassága m-ben: pl.: 140
·         az épület emeleteinek a száma, pl.: 43
·	az épület építésének az éve, pl.1949
Az állomány első sora a mezőneveket tartalmazza „$” jellel elválasztva.
A megoldás mintája:
III/A, B:
            	Az épületek száma: 8
III/C:
            	Az 555 lábnál magasabb épületek száma: 2.
III/D:
            	A legöregebb épület országa: Lengyelország.
A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a epulet.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki az épületek számát a mintának megfelelően a konzolra! (2p)
C.	Adja meg az 555 lábnál magasabb épületek számát, ha 1 m = 3.280839895 láb! (4p)
D.	Írassa ki konzolra a mintának megfelelően a legöregebb épület (ha több is van, akkor az első legöregebb adatait) országát. (4p)
"""
from Epuletclass import Epulet
varos_epulet_lista=[]
def beolvas():
    fajlom=open("epulet.txt","r",encoding="utf-8")
    fajlom.readline()
    fajltartalom=fajlom.readlines()
    i=0
    while i< len(fajltartalom):
        sor=fajltartalom[i].strip().split("$")
        varos_epulet_lista.append(Epulet(sor))
        #print(sor)
        i+=1
    #print(varos_epulet_lista[0])
    print(len(varos_epulet_lista))
def magas_epuletek():
    i=0
    magas_db=0
    while i< len(varos_epulet_lista):
        if varos_epulet_lista[i].magassag > 555/3.280839895:
            magas_db+=1
        i+=1
    return magas_db
def legoregebb_ep():
    i=0
    legoregebb=0
    while i < len(varos_epulet_lista):
        if varos_epulet_lista[legoregebb].epult > varos_epulet_lista[i].epult:
            legoregebb=i
        i+=1
    return varos_epulet_lista[legoregebb].orszag