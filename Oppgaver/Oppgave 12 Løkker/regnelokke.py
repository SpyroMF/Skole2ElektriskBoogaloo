x = 1
liste = []
#Kjører while helt til x == 0
while x != 0:
    x = int(input('Ikke skriv "0": '))
    #Legger til x i listen
    liste.append(x)
#Skriver ut alle verdiene i liste
for i in range(0, len(liste)):
    print(liste[i])
minSum = 0
#Legger sammen alle variablene i liste
for i in range(0, len(liste)):
    minSum += liste[i]
print("Sammenlagt:",minSum)
minsteTall = liste[0]
#Går igjennom alle verdiene og finner den minste verdien
for i in range(0, len(liste)):
    #Om valgte liste tallet er mindre enn variablen minsteTall gjør om variablen minsteTall til liste[i]
    if minsteTall < liste[i]:
        minsteTall = liste[i]
#Gjør det samme her, bare at den finner den variablen som er størst
storsteTall = liste[0]
for i in range(0, len(liste)):
    if storsteTall > liste[i]:
        storsteTall = liste[i]
print("Minste Tall:",minsteTall)
print("Storste Tall:",storsteTall)