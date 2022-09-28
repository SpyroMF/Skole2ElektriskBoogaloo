#importerer klassen Motorsykkel() fra filen motorsykkel
from motorsykkel import Motorsykkel


class Hovedprogram():
    print("--------\f")

    print("Motorsykkel 1:\f")
    #Lager m1 (Motorsykkel 1)
    m1 = Motorsykkel("Volvo", "EW 142423", 42)
    #Skriver ut all info
    m1.skrivUt()

    print("\f--------\f")
    print("Motorsykkel 2:\f")

    #samme her
    m2 = Motorsykkel("BMW", "EK 124245", 106)
    m2.skrivUt()

    print("\f--------\f")
    print("Motorsykkel 3:\f")

    #Tester kjør funksjonen
    m3 = Motorsykkel("BMW", "EK 124245", 106)
    m3.kjor(10)
    #Skriver ut kilometerstand
    print("Kilometerstand: %s" % m3.hentKilometerstand())

Hovedprogram()