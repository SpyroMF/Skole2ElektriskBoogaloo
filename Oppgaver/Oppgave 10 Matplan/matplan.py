matplan = {
    "Kari Nordmann":["Brød", "Egg", "Pølser"],
    "Knut":["Banan", "Banan", "Banan"],
    "Per":["Idun pølse senep", "Heinz tomat ketsjup", "Råtten fisk"]
}



def søk():
    
    navn = input("SØK: ")
    if navn in matplan:
        f = matplan[navn][0]
        l = matplan[navn][1]
        m = matplan[navn][2]
        print("--------------------------------------------------")
        print("Frokost:", f)
        print("Lunch:  ", l)
        print("Middag: ", m)
        print("--------------------------------------------------")
    else:
        print("--------------------------------------------------")
        print("Finner ikke hva du søker på. Husk stor forbokstav!")
        print("--------------------------------------------------")
        

while True:
    søk()