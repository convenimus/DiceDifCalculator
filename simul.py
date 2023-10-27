#Installiere alle nötigen Bibliotheken
import math
import random
import matplotlib.pyplot as plt
import numpy as np

#Definiere alle nötigen Variablen
p_kleiner3 = int(0)
p_größergleich3 = int(0)
difliste = [0,0,0,0,0,0] #Array
reldifliste = [0,0,0,0,0,0] #Array

#Ausgabe zur Abfrage der Durchgänge
print("Enter the number of trys:")
n_max = int(input())

#Würfelt und trägt Differenzen in die zugehörige Liste ein
for x in range(n_max):
    p1_w = random.randint(1, 6)
    p2_w = random.randint(1, 6)
    difp1_p2 = int(abs(p1_w - p2_w))
    difliste[difp1_p2] += 1
    if difp1_p2 < 3:
        p_kleiner3 += 1
    else:
        p_größergleich3 += 1
#Übertragt und rechnet die relative Häufigkeit in den zugehöriigen Array aus
for y in range(6):
    reldifliste[y] = difliste[y]/n_max
#
#
#Gibt die Ergebnisse aus
print("Final-Value: ")
print(reldifliste)
print("Absolute häufigkeiten")
print("[00, 01, 02, 03, 04, 05]")
print(difliste)
print("Absolut: P von kleiner als 3: ", p_kleiner3)
print("Relativ: P von kleiner als 3: ", p_kleiner3 / n_max)
print("Absolut: P von größergleich 3: ", p_größergleich3)
print("Relativ: P von größergleich 3: ", p_größergleich3 / n_max)
#
#Erstellt ein Diagramm mit den einzelnen relativen Häufigkeiten der einzelnen Differenzen
x = np.arange(6)
width = 0.9
plt.bar(x, reldifliste, width, color='cyan')
plt.xticks(x, ['0', '1', '2', '3', '4', '5'])
plt.xlabel("Differenz")
plt.ylabel("Relative Häufigkeit")
plt.show()
