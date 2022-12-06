# Ziehung der Lottozahlen
# ohne Doubletten und aufsteigend sortiert
# Zahlenverteilung:
#   Durchschnitt aus 1 bis 49: 25 (wer hätte das gedacht)
#   mal 6 = 150
#   10% Streuung nach oben und unten
#   ergibt minimum = 135, maximum = 165

import random
random.seed()

# const
minimum = 135
maximum = 165

print()
print("Lottozahlen 6 aus 49:")

def ziehung():
    # repeat-until Ersatz
    until = False
    while until == False:

        # array erstellen und löschen
        array = [False]         # steht wohl für index 0 der nie genutzt wird
        for i in range(1,50):   # blöde syntax, zählt nur bis max - 1
            array.append(False)

        anzahl = 0
        summe = 0
        # solange weniger als 6 zahlen gezogen
        while anzahl < 6:
            # ziehe eine Zahl
            gezogen = random.randint(1,49)
            # falls nicht schon gezogen
            if array[gezogen] == False:
                # im array als gezogen vermerken
                array[gezogen] = True
                # und zähler eins rauf
                anzahl = anzahl + 1
                summe = summe + gezogen

        # Abbruchbedingung für endlose while-Schleife anstatt repeat-until     
        if summe > minimum and summe < maximum: # gewünschte Zahlenverteilung
            until = True

    # ausgabe
    i = 1
    # array durchgehen und
    while i < 50:
        # falls gezogen
        if array[i] == True:
            # Treffer ausgeben
            print(i, "* ", end="")
        i = i + 1

    print("Summe:", summe)

d = 0
print("Anzahl Kästchen: ", end="")
dmax = int(input())
print()
while d < dmax:
    ziehung()
    print() # Leerzeile
    d = d + 1
