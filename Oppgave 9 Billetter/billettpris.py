#Funksjon som tar inn navn og alder
def kjøp_billett(navn, alder):
    billet_pris = 0
    if type(alder) != int:
        pass
    #Om alder er lik eller mindre enn 17 kjør...
    elif alder <= 17:
        billet_pris = 30
    #Om alder er mellom 18 og 63 kjør...
    elif alder > 17 and alder < 63:
        billet_pris = 50
    #Om alder er over 63 kjør...
    else:
        billet_pris = 35
    
    #Printer en kvitering lignene informasjon
    print("----------------")
    print("Navn:", navn)
    print(billet_pris, "kr")

#Tester funksjonen på userinput 
navn1 = input("Navn: ")
alder1 = int(input("Alder: "))

#Tester de forskjellige alderene
kjøp_billett(navn1, alder1)
kjøp_billett("Per", 15)
kjøp_billett("Spelle", 31)
kjøp_billett("Mann", 63)