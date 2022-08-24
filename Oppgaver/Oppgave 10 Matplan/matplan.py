#Liste med folk, folk har også lister for å lagre måltider til hver individuelle person
matplan = {
    "Kari Nordmann":["Brød", "Egg", "Pølser"],
    "Knut":["Banan", "Banan", "Banan"],
    "Per":["Idun pølse senep", "Heinz tomat ketsjup", "Råtten fisk"]
}



def søk():
    
    navn = input("SØK: ")
    #Om navnet fra navn variablen er i matplan
    if navn in matplan:
        #Henter måltider og putter dem i en variabel
        f = matplan[navn][0]
        l = matplan[navn][1]
        m = matplan[navn][2]
        print("--------------------------------------------------")
        print("Frokost:", f)
        print("Lunch:  ", l)
        print("Middag: ", m)
        print("--------------------------------------------------")
    #Om den ikke finner navnet på lista
    else:
        print("--------------------------------------------------")
        print("Finner ikke hva du søker på. Husk stor forbokstav!")
        print("--------------------------------------------------")
        
#while løkke for å kunne repetere søk funksjonen til programmet stoppes
while True:
    søk()