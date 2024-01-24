

from Cipo import Cipo


def pldListaba():
	peldany1 = Cipo("Nike", 42)
	peldany2 = Cipo("Adidas", 41)
	peldany3 = Cipo("Adidas", 45)

	cipok = []
	cipok.append(peldany1)
	cipok.append(peldany2)
	cipok.append(peldany3)
	return cipok


def listaKiir(cipok):
	for i in range(0, len(cipok), 1):
	    nev: str = cipok[i].nev
	    meret: int = cipok[i].meret
	    print(f"{nev} ({meret})")


#listaKiir(pldListaba())






def osszegzesTetele():
    ossz: int = 0
    for i in range(0, len(cipok), 1):
        ossz += cipok[i].meret

    atlag = ossz / len(cipok)
    print(round(atlag, 3))





#legnagyobb cipo + a markaja
def LegnagyobbPluszMarkaja():
    legn = 0
    for i in range(0, len(cipok), 1):
        if cipok[i].meret > cipok[legn].meret:
            legn = i
    print(f"Legnagyobb cipő neve és mérete: {cipok[legn].nev}")



# Progtétel: Egy sorozathoz egy értéket rendelünk!!!!----------------






def HanyAdidasVan():
    db = 0
    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas":
            db += 1
    print(f"Ennyi db Adidas van: {db}")









def nagyobb_42_adidas():
    #eldontes tetele
    van_nagyobb: bool = False

    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van_nagyobb = True

    if van_nagyobb == True:
        print("Van, Adidasból 42-es méret")
    else:
        print("Nincs, Adidasból 42-es méret")














cipok = pldListaba()
listaKiir(cipok)

osszegzesTetele()
LegnagyobbPluszMarkaja()
HanyAdidasVan()
nagyobb_42_adidas()








def FajlBeolvas():
    f = open("cipok.txt", "r",encoding="UTF-8")
    file.readline()
    sorok = file.readlines()

    cipoLista = []
    for i in range(len(sorokLista)):
        aktElem = sorokLista[i]
        sorLista = aktElem.strip().split(",")
        nev = str(sorLista[0])
        meret = str(sorLista[1])

        cipo = Cipo(nev,meret)
        cipoLista.append(cipo)

    return cipoLista


lista = fajlbeolvasas()


