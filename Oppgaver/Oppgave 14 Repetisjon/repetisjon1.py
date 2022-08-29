#Laget en tom liste
mineOrd = []
#En simpel funksjon som tar 2 tekster og legger dem sammen
def slaaSammen(tekst1, tekst2):
    return str(tekst1) + str(tekst2)
#En funksjon som tar en liste og skriver ut allt innhold
def skrivUt(liste):
    for i in range(0, len(liste)):
        print(liste[i])
#Variabel som velger om while løkken kjører
x = True
#While-if løkke som kjører tidligere funksjoner med bruker input
while x:
    print("--------------------------------------------------------")
    user_input = input("'i': Slå sammen to strenger\f'u': Skriv ut liste\f's': Stopp programmet\fSkriv her: ")
    if user_input == "i":
        #Veldig lang streng som sørger for at jeg ikke har noen  unødvendige variabler
        print("--------------------------------------------------------")
        print(slaaSammen(input("Tekst 1: "), input("Tekst 2: ")))
    elif user_input == "u":
        #Skriver ut en tom liste
        skrivUt(mineOrd)
    elif user_input == "s":
        x = False
    else:
        #Om brukeren skrev feil, sier koden ifra
        print("--------------------------------------------------------")
        print("Dette forstod jeg ikke? Prøv på nytt. Husk små bokstaver")
        