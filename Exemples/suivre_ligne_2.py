"""
Ce programme fait la même chose que le programme v1
Sauf qu'il le fait de manière plus :
 - intelligente : les entrées (ground) sont directement reliées aux sorties (motor) via (droite, gauche)
 - sécurisée    : le robot s'arrête en cas de plantage du programme ou son arrêt par l'utilisateur

Pour arrêter le programme, appuyez sur les boutons a b du microbit ou sur le stop de thonny
"""

from Maqueen_Plus import *


# Fonction suivre ligne
def suivre_ligne() :
    capteur_g, capteur_d = groundReadLogique()[2:4] # On ne regarde que les capteurs du milieu
    moteur_g = capteur_d*40 # Si la ligne est vue par le capteur gauche, on donne une puissance (40)
    moteur_d = capteur_g*40
    motorSetPower(moteur_g, moteur_d) # Envoyer la puissance aux moteurs


# Programme principal
try :
    display.show(Image.YES)
    while not button_a.is_pressed() and not button_b.is_pressed() : # Tant que programme maintenu
        suivre_ligne()
finally : # Si erreur de programme ou arrêt par l'utilisateur
    motorSetPower(0, 0)
    display.show(Image.NO)