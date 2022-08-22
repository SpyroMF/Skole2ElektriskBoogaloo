
#Lager en ordbok
varer = {
    "melk":14.9,
    "brød":24.90,
    "yoghurt":12.90,
    "pizza":39.90
}

print(varer)


#En funksjon som legger til selvvalgt antall varer
def legg_til_varer(vareliste):
    #får hvor mange varer en bruker skal legge til
    antall_varer = input("Hvor mange varer vil du legge til? ")
    
    
    #kjører koden så mange ganger brukeren ønsket
    for i in range(0, int(antall_varer)):
        print("----------------------------------")
        vare_navn = input("Legg til vare: ")
        vare_pris = input("Prisen på varen: ")
        #Legger varen til i ordboken
        vareliste[vare_navn] = vare_pris
        print(vareliste)

#kjører funksjonen
legg_til_varer(varer)
print(varer)