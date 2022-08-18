#Oppgave 1
#Lag en fil ved navn variabler

#Skriv et program i denne filen som skriver ut ”Hallo Verden!” til terminalen. 
print("Hallo Verden!")
#Endre programmet slik at du ber brukeren om å oppgi et navn i form av en tekststreng ved hjelp av funksjonen input(), og lagre denne verdien i en variabel navn. 
#Skriv så ut “Hei “ og variabelen navn. 
oppg2_navn = input("Hva er navnet ditt? ")
print("Hallo " + oppg2_navn + "!")


#Utvid programmet ditt med to variabler. Du kan velge variabelnavn selv, men gi begge variablene heltallsverdier. Skriv ut variablene på hver sin linje. 
oppg3_tall1 = 5
oppg3_tall2 = 4
print(str(oppg3_tall1) + "\f" + str(oppg3_tall2))



#Beregne differansen av de to variablene (den første minus den andre) og legg resultatet inn i en ny variabel. 
#Skriv ut “Differanse:” etterfulgt av denne tredje variabelen. Du skal sjekke at begge tallene er heltall, og koden skal lage unntak hvis de ikke er det. 


oppg4_tall1 = oppg3_tall1
oppg4_tall2 = oppg3_tall2
if type(oppg4_tall1) == int and type(oppg4_tall2) == int:
    oppg4_tall3 = oppg4_tall1 - oppg4_tall2
    print("Differanse: " + str(oppg4_tall3))

#Be bruker om å oppgi et nytt navn, og legg svaret i en ny variabel. Lag nok en variabel ved navn sammen, 
#og gi den verdien av det første navnet etterfulgt av det andre navnet. Skriv ut sammen på en ny linje. 

oppg5_navn1 = oppg2_navn
oppg5_navn2 = "Knut"
oppg5_sammen = str(oppg5_navn1) + str(oppg5_navn2)
print(oppg5_sammen)

#Du skal nå endre verdien av variabelen sammen. Dette skal du gjøre ved å slå sammen de to navnene som i forrige deloppgave, 
#men denne gangen skal du legge til “og” med et mellomrom på hver side mellom dem. For eksempel: Dersom sammen først hadde verdien “OlaKari!” 
#skal den nå ha verdien “Ola og Kari”.  
oppg6_sammen = str(oppg2_navn) + " og " + str(oppg5_navn2)
print(oppg6_sammen)



        
#Viktig: Du skal utvide programmet ditt ved å endre verdien av variabelen sammen på en ny linje, ikke endre linjen der du først definerte variabelen. 
