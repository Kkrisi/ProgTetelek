import math

# Eldöntés 1

szam = int(input("Kérek egy számot: "))

def Osztoi(szam):
	lista = []
	for i in range(2,round(math.sqrt(szam)+1)):
		if szam % i == 0:
			lista.append(i)
	return lista


#print(Osztoi(szam))





def OsztoiWhile(szam):
	lista = []
	i = 2
	while i <= round(math.sqrt(szam)):
		if szam % i == 0:
			lista.append(i)
		i += 1
	return lista

print(OsztoiWhile(szam))









#Lineáris keresés
also = 42
felso = 67
i = also
while i <= felso and i % 10 != 0:
	i += 1

van = i <= felso

if van:
	print(f"van 0-ra végződő szám: {i}")
else:
	print("nincs 0-ra végződő")
















#Kivalasztas tetele

def Kivalasztas():
	prim = False
	n = 9999
	while prim == False:
		n += 1
		i = 2
		while i <= math.sqrt(n) and n % i != 0:
			i += 1
		prim = i > math.sqrt(n)
	print(n)


Kivalasztas()
