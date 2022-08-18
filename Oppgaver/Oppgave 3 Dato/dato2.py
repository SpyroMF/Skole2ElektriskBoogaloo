#Frivillig oppgave

#To tomme lister, de fylles med input() kommandoen i funksjonen "add_date_to_list"
#Oppsett [Dag, Måned]
dato1 = []

dato2 = []

def add_date_to_list():
    x = []
    
    dato = input("Dato: ")
    
    #Gjør om dato til tre forskjellige variabler
    dag = dato[0] + dato[1]
    maaned = dato[3] + dato[4]
    
    #Legger til dag og måned til x
    x.append(dag)
    x.append(maaned)
    
    
    #Returnerer variablen "x" til add_date_to_list
    return x
#Lager litt mellomrom (Lettere å se hvor man skal skrive)
print(" \f \f \f \f \f \f \f \f ")


print("Skriv en dato (Dag/Måned). Eksemplel: '05/08'")
print(" ")
print("Dato nummer 1")

#Kjører "add_date_to_list" som returner en liste som har en dato i seg
#Dette gjør at dato vil se no sånt ut ---> dato1 = [04,12]
dato1 = add_date_to_list()

print("Dato nummer 2")

#Gjør det samme som dato1, men dette er en annen variabel
dato2 = add_date_to_list()

if dato1[1] == dato2[1]:
    #Om Dato 1 er lik Dato 2 kjør...
    if dato1[0] == dato2[0]:
        print("Samme dato!")
    #Om Dato 1 er mindre en Dato 2 kjør...
    elif dato1[0] < dato2[0]:
        print("Riktig rekkefølge!")
    #Om begge feiler kjør...
    else:
        print("Feil rekkefølge!")
#Om Måned 1 er mindre en måned 2 kjør...
elif dato1[1] < dato2[1]:
    print("Riktig rekkefølge!")
#Om Måned 1 er større en måned 2 kjør...
elif dato1[1] > dato2[1]:
    print("Feil rekkefølge!")