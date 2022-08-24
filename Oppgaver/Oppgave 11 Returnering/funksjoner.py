# adder legger sammen tall1 og tall2 og returnerer det
def adder(tall1, tall2):
    return int(tall1) + int(tall2)


print(adder(1, 1))
print(adder(924, 124))


tekst1 = input("Skriv no kult: ")
def tellForekomst(minTekst, minBokstav):
    x = 0
    for i in range(0, len(minTekst)):
        if minTekst[i] == minBokstav:
            x += 1
    return x

print(tellForekomst(tekst1, "e"))