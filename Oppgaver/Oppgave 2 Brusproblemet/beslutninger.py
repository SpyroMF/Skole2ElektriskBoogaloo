#Oppgave 2

#Bruker skriver in ja eller nei
valg = input("Liker du brus? ")

#Gjør valg om til små bokstaver, dette gjør at programmet ikke trenger å skille mellom store og små bokstaver
valg = valg.lower

#Om brukeren har skrevet "ja" kjør...
if valg == "ja":
    print("Her har du en brus!")
#Om brukeren har skrevet "nei" kjør...
if valg == "nei":
    print("Den er grei.")
#Om brukeren skrev feil kjør...
else:
    print("Det forstod jeg ikke helt?")