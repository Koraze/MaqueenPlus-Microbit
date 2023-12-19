"""
Suiveur de ligne simple

Ce programme suit une ligne continue et s'arrête quand il tombe dans une zone blanche
Ici, nous n'utilisons que les 2 capteurs de sol au milieu

Note 1 : Le programme limite au maximum l'interaction microbit - maqueen
En effet, chaque interaction prend du temps, il est donc important de les réduire
Ici, on alterne lecture des capteurs et commande des actionneurs pour un robot le plus réactif possible

Note 2 : Arrêter / réinitialiser le microbit ne signifie pas arrêter le maqueen.
Les moteurs garderont la dernière commande reçue une fois le microbit arrêté ou réinitialisé.
Placez le robot sur une surface blanche avant de l'arrêter / réinitialiser
"""

from Maqueen_Plus import *

# Programme principal
while True :
    # lecture capteurs
    capteurs_milieu = groundReadLogique()[2:4] # Interaction base -> microbit
    
    # Décision puissance moteur
    if capteurs_milieu == [0, 0] :
        moteurs = (0, 0)
    elif capteurs_milieu == [0, 1] :
        moteurs = (40, 0)
    elif capteurs_milieu == [1, 0] :
        moteurs = (0, 40)
    elif capteurs_milieu == [1, 1] :
        moteurs = (40, 40)
        
    # Envoi puissance moteurs
    # * : Déballe le tuple "moteurs" pour ne faire passer que les valeurs
    motorSetPower(*moteurs) # Interaction microbit -> base
