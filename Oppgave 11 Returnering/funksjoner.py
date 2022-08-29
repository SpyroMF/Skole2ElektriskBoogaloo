# adder legger sammen tall1 og tall2 og returnerer det
def adder(tall1, tall2):
    return int(tall1) + int(tall2)

#Bruker adder til å skrive ut sammenlagte tall
print(adder(1, 1))
print(adder(924, 124))


tekst1 = input("Skriv no kult: ")

def tellForekomst(minTekst, minBokstav):
    x = 0
    #For-løkke som sier hvor ofte en bokstav oppstår og legger det som int in i x
    for i in range(0, len(minTekst)):
        if minTekst[i] == minBokstav:
            x += 1
    return x

#Tar userinput og sjekker hvor ofte "e" forekommer
print(tellForekomst(tekst1, "e"))
