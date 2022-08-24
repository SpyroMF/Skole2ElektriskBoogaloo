#Lager 3 tomme lister
steder = []
klesplagg = []
avreisedatoer = []

#Samme loop 3 ganger. Den legger til userinput ting tang i listene
for i in range(0, 5):
    steder.append(input(str("Skriv et sted",str(i)+":")))

for i in range(0, 5):
    klesplagg.append(input(str("Skriv et klesplagg",str(i)+":")))

for i in range(0, 5):
    avreisedatoer.append(input(str("Skriv en reisedato",str(i)+":")))


#Putter alle listene i en ny liste
reiseplan = [steder, klesplagg, avreisedatoer]

#Printer alle listene i reiseplan
for i in range(0, len(reiseplan)):
    print(reiseplan[i])


#Brukeren velger vilken liste i reiseplan de vil få info om
i1 = int(input("Hvilken del av reiseplan skal skrives ut? "))
#Om tallet er gyldig kjør...
if i1 in range(reiseplan[0], reiseplan[-1]):
    i2 = int(input("Hvilken del vil du skrive ut?"))
    #Om i2 er gyldig print liste verdien i listen reiseplan
    if i2 in range(reiseplan[i2][0], reiseplan[i2][-1]):
        print(reiseplan[i2])
    #Om tallet ikke er gyldig kjør...
    else:
        print("Ugyldig input!")
#Vell, om tallet ikke er gyldig kjør...
else:
    print("Ugyldig input!")