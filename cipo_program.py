from Cipo import Cipo

peldany1 = Cipo("Nike", 42)
peldany2 = Cipo("Adidas", 41)
peldany3 = Cipo("Adidas", 45)

cipok = []
cipok.append(peldany1)
cipok.append(peldany2)
cipok.append(peldany3)

for i in range(0, len(cipok), 1):
    nev: str = cipok[i].nev
    meret: int = cipok[i].meret
    print(f"{nev} ({meret})")


def meret_atlag():
    ossz: int = 0
    for i in range(0, len(cipok), 1):
        ossz += cipok[i].meret

    atlag = ossz / len(cipok)
    print(round(atlag, 3))


meret_atlag()


def nagyobb_42_adidas():
    van_nagyobb: bool = False

    for i in range(0, len(cipok), 1):
        if cipok[i].nev == "Adidas" and cipok[i].meret > 42:
            van_nagyobb = True

    if van_nagyobb == True:
        print("Van")
    else:
        print("Nincs")


nagyobb_42_adidas()
