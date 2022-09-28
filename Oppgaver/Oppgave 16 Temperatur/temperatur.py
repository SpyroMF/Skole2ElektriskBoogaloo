

#Lager en liste som er veldig nyttig senere
maander = ["Januar", "Februar", "Marsj", "April", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]
#Tom liste som også brukes senere
temperaturer = []

#åpner et tekst dokument (PATH må endres)
with open("c:\\txt\\temperatur.txt") as fil:
    #kjører for alle linjene i fil
    for line in fil:
        
        x = ""
        #Denne for løkken fjerner \n
        for i in range(0, len(line)):
            tallogtegn = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
            #Om valgt tegn er i tallogtegn
            if line[i] in tallogtegn:
                x += line[i]
        #legger til dag i temperaturer listen
        temperaturer.append(int(x))

print(temperaturer)

#gjennomsnitt funksjon som tar in en liste med tall
def gjennomsnitt(liste):
    x = 0
    #for løkke som legger til alle tallene
    for i in range(0, len(liste)):
        x += int(liste[i])
    #Returnerer det sammenlagte tallet delt på hvor mange tall i listen
    return x/len(liste)
#skriver ut det returnerte gjennomsnittet av listen temperaturer
print(gjennomsnitt(temperaturer))