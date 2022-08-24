def skrivUt(tekst1,tekst2,tall1):
    print(tekst1) 
    print(tekst2," ", tall1)
#Koden starter her på linje 5. fra linje 5 til 9 lager koden variabler
antallOppgaver = 4 
t1="Melding til alle programmerere:"
t2="Antall oppgaver igjen: "
t3="Hvor mange nye oppgaver får vi: "
t4="Vi har fått flere oppgaver. Antall oppgaver er nå: "
#Her kjører den funksjonen på linje 1, Denne ville skrevet ut print("Melding til alle programmerere") deretter skrive ut print("Antall oppgaver igjen: 4")
skrivUt(t1,t2,antallOppgaver)

#Denne legger bruker t3("Hvor mange nye oppgaver får vi: ") og tar brukerindata og legger det i variabelen antallNyeOppgaver som en integer (heltall)
antallNyeOppgaver = int(input(t3)) 
#Legger sammen antallNyeOppgaver med antallOppgaver og putter dem i antallOppgaver
antallOppgaver = antallOppgaver + antallNyeOppgaver

#Gjør akkuratt det samme som linje 11 bare bytter ut "Antall oppgaver igjen: XXXX" med 4 + brukerindata
skrivUt(t1,t2,antallOppgaver) 

#Om antallOppgaver er større en 10 kjør...
if antallOppgaver > 10:
    print("Det er mer enn 10 oppgaver igjen.")
#Om antallOppgaver lik 10 kjør... 
elif antallOppgaver == 10:
    print("Det er 10 oppgaver igjen.") 
#Om ingen av dem funker kjør... (da er det bare mindre en 10 som er mulig)
else:
    print("Det er mindre enn 10 oppgaver igjen")
