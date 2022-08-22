#Oppgave 7



#1
#Lager liste



liste = [1, 40, 124]
#Legger til det fjerde tallet
liste.append(14)

#Printer første og tredje tallene i liste
print("Første Tall: "+str(liste[0])+"\fTredje Tall: "+str(liste[2]))



#2
liste2 = []
def legg_sammen(liste_temp):
    x = 0
    for i in range(0, len(liste_temp)):
        x += liste_temp[i]
    return x

def multipliser(liste_temp):
    x = 0
    #Kjører for alle elementene i liste_temp
    for i in range(0, len(liste_temp)):
        #For å multiplisere alle samt legge til resultatet i x, 
        #må første regnestykke starte med at x = et nummer
        if x != 0:
            x = liste_temp[i] * x
        else:
            x = liste_temp[i]
    return x

liste2.append(legg_sammen(liste))
liste2.append(multipliser(liste))

liste3 = []

#Disse for løkkene legger til liste og liste2 i liste3
for i in range(0, len(liste)):
    liste3.append(liste[i])
for i in range(0, len(liste2)):
    liste3.append(liste2[i])

print(liste3)
#Pop fjerner valgte posisjon fra listen
liste3.pop(-1)
liste3.pop(-2)

print(liste3)

#3


def legg_til_strings_til_liste(antall):
    x = []
    for i in range(0, antall):
        x.append(input((str(i) + "/") + str(antall) + " | Skriv navn her: "))
    return x
liste4 = legg_til_strings_til_liste(4)
print(liste4)

#4
if "Mikkel" in liste4:
    print("Du husket meg!")
else:
    print("Glemte du meg?")