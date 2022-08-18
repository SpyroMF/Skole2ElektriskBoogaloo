
#Begge funksjonene er mer eller mindre like. (utenom formelen)
def fahrenheit_celsius(temp_farenheit):
    #Gjør om gitt farenheit temp til celsius
    temp_celsius = (temp_farenheit - 32) * 5/9
    #Returnerer den konverterte
    return(temp_celsius)

#Denne gjør det samma som den over, men motsatt
def celsius_fahrenheit(temp_celsius):
    temp_fahrenheit = temp_celsius * 9/5 + 32
    return(temp_fahrenheit)



while True:
    valg = input("Konverter\f1. C --> F\f2. F --> C\f1 eller 2?: ")
    temp = input("Hvilke temperatur vil du konvertere?\fTemperatur: ")
    if valg == "1":
        print(celsius_fahrenheit(int(temp)))
    if valg == "2":
        print(fahrenheit_celsius(int(temp)))