#Oppgave 3


#Dato 1
datoD1 = 1
#Månede 1
datoM1 = 3


#Dato 2
datoD2 = 1
#Månede 2
datoM2 = 3

#Om Månedene er like kjør...
if datoM1 == datoM2:
    #Om Dato 1 er lik Dato 2 kjør...
    if datoD1 == datoD2:
        print("Samme dato!")
    #Om Dato 1 er mindre en Dato 2 kjør...
    elif datoD1 < datoD2:
        print("Riktig rekkefølge!")
    #Om begge feiler kjør...
    else:
        print("Feil rekkefølge!")
#Om Månede 1 er mindre en månede 2 kjør...
elif datoM1 < datoM2:
    print("Riktig rekkefølge!")
#Om Månede 1 er større en månede 2 kjør...
elif datoM1 > datoM2:
    print("Feil rekkefølge!")