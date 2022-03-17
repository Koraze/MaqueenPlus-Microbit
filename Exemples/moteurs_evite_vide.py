"""
Dans ce programme, le robot va continuellement en marche avant lente
Il fait une marche arrière rapide et brève s'il rencontre du vide

Le programme peut être proprement arrêté via les boutons a et b, ou via le "stop" de thonny
(d'ou le try et le finally)
En effet, suite à l'arrêt du programme, les moteurs peuvent toujours être actifs
il est donc important (à l'aide du finally) de s'assurer de l'arrêt des moteurs
"""
from Maqueen_Plus import *

# Fonction marche avant lent
def marche_avant_lent() :
    display.show(Image.HAPPY)
    motorSetPower(40, 40) # Impulsion pour démarrer le robot (démarrer à 25 n'est pas possible)
    sleep(100)
    motorSetPower(25, 25) # Puissance de croisière

# Fonction marche arrière brève et rapide
def marche_arriere_breve():
    display.show(Image.ANGRY)
    motorSetPower(-70, -70)
    sleep(600)
    motorSetPower(0, 0)
    sleep(300)

# Initialisation
print("démarrage programme")
marche_avant_lent() # Robot en marche avant

# Lancement boucle
try :
    while not button_a.is_pressed() and not button_b.is_pressed() : 
        if sum(groundReadLogique()) : # Si obstacle, reculer, puis avancer
            marche_arriere_breve()
            marche_avant_lent()
finally : # Si erreur de programme ou arrêt par l'utilisateur
    motorSetPower(0, 0)
    display.show(Image.NO)
