temp_fil = open("temperatur.txt", "r")
maander = ["Januar", "Februar", "Marsj", "April", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

temperaturer = []

with open("temperatur.txt") as fil:
    for line in fil:
        #For å ta vekk "\n" som ødelegger strukturen av oppsettet mitt, velger jeg å skrive ut tegn 0 til tegn -1, "\n" regnes ikke som et tegn
        #temperaturer.append(line[0:-1])
        temperaturer.append(line[0:-1])
        
print(temperaturer)

def gjennomsnitt(liste):
    x = 0
    for i in range(0, len(liste) + 1):
        x += liste[i]
    return x/len(liste)
print(gjennomsnitt(temperaturer))