#Disse tre gjør relativt det samme, returnere regnet
def addisjon(tall1, tall2):
    return tall1 + tall2

def subtraksjon(tall1, tall2):
    return tall1 - tall2

def divisjon(tall1, tall2):
    return tall1/tall2

print(addisjon(1, 1))
print(subtraksjon(4, 2))
print(divisjon(1000, 42))

#returnerer en konversjon fra tommer til centimeter
def tommerTilCm(antallTommer):
    return antallTommer * 2.54

tommerTilCm(15)

#Kjører alle funksjonene
def skrivBeregning():
    tall1 = float(input("Tall 1: "))
    tall2 = float(input("Tall 2: "))
    print("Addisjon: " + str(addisjon(tall1, tall2)))
    print("Subtraksjon: " + str(subtraksjon(tall1, tall2)))
    print("Divisjon: " + str(divisjon(tall1, tall2)))
    print(tommerTilCm(float(input("Tommer -> Centimeter: "))))
#Tester funksjonen  
skrivBeregning()
    