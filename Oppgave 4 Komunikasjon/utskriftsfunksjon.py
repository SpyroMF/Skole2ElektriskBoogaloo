
#Definerer en funksjon som heter preik
def preik():
    #lager 2 variabler som brukes i print()
    navn = input("Hva heter du? ")
    sted = input("Hvor kommer du fra? ")
    print("Hei " + str(navn) + "! Du er fra " + str(sted) + ".")
#Her kjører jeg koden inni preik()
preik()