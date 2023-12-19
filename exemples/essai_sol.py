"""
Essai sol

Le robot possède 6 capteurs de ligne / sol
La valeur logique renvoyée par les capteurs indiquent la présence d'une ligne ou pas
 - 0 (led éteinte) : Sol clair
 - 1 (led bleue)   : Sol sombre, ligne noir, pas de sol

Le résultat est du type (gauche) [0,0,0,0,0,0] (droite)
Ex, si seul le capteur le plus à gauche est sur la ligne noire : [1,0,0,0,0,0]
"""
from Maqueen_Plus import *

for i in range(8) :
    print(groundReadLogique()) # visualisation de l'état du sol
    sleep(500)
