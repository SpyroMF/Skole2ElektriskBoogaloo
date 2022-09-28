#Klasse som heter motorsykkel
class Motorsykkel():
    
    #Gjør klar alle verdiene
    def __init__(self, merke, registreringsnummmer, kilometerstand):
        self.merke = merke
        self.registreringsnummer = registreringsnummmer
        self.kilometerstand = kilometerstand
        
    #Legger til km i kilometerstand
    def kjor(self, km):
        self.kilometerstand += km
    #returnerer kilometerstand
    def hentKilometerstand(self):
        return self.kilometerstand
    #Skriver ut all info
    def skrivUt(self):
        print(
            "Kilometere:", self.kilometerstand, "\f",
            "Merke:", self.merke, "\f",
            "Registreringsnummer:", self.registreringsnummer
        )