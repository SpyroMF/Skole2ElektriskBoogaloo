
#funksjon som tar inn filnavn og gjør om fila til en ordbok den returnerer første ord = andre ord for hver linje
def innlesning(filnavn):
    x = {}
    with open(filnavn) as fil:
        for line in fil:
            y = line.split(" ")
            x[y[0]] = int(y[1])
    
    return x


#Denne går igjennom alle personene i en ordbok og sjekker hvem som har høyest verdi og returnerer den
def maanedensSalgsperson(ordbok):
    x = 0
    
    for i in ordbok:
        #Om ordbok[i] er større en x endre x til den største
        if ordbok[i] > x:
            x = ordbok[i]
            #Her tar den nøkkelen {nøkkel:xyz} og returnerer en liste med navn(nøkkelen) og antall salg.
            for nokkel in ordbok:
                y = [nokkel, ordbok[nokkel]]
    return y

#Legger sammen alle salgene
def totaltAntallSalg(ordbok):
    x = 0
    for i in ordbok:
        x += ordbok[i]
    return x

#finner gjennomsnittet av alle salgen per person
def gjennomSnitt(ordbok):
    x = 0
    y = 0
    for i in ordbok:
        y += 1
        x += ordbok[i]
    return (x/y)


#Her bare skriver den ut all info
def hovedprogram():
    ob = innlesning("c:\\txt\\salg.txt")
    maandens_ob = maanedensSalgsperson(ob)
    print("Maanedens ansatte er %s og har solgt %s produkter." % (maandens_ob[0],maandens_ob[1]))
    print("Aktive selgere denne maaneden: %s Totalt antall salg: %s" % (len(ob), totaltAntallSalg(ob)))
    print("Gjennomsnittlig antall salg per salgsperson: %s" % (gjennomSnitt(ob)))

#og her starter programmet
hovedprogram()