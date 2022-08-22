def kjøp_billett(navn, alder):
    billet_pris = 0
    if type(alder) != int:
        pass
    elif alder <= 17:
        billet_pris = 30
    elif alder > 17 and alder < 63:
        billet_pris = 50
    else:
        billet_pris = 35
    
    print("----------------")
    print("Navn:", navn)
    print(billet_pris, "kr")


navn1 = input("Navn: ")
alder1 = int(input("Alder: "))


kjøp_billett(navn1, alder1)
kjøp_billett("Per", 15)
kjøp_billett("Spelle", 31)
kjøp_billett("Mann", 63)