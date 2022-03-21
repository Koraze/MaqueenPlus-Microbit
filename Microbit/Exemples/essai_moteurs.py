"""
Essai des moteurs

Le robot est propulsé par deux moteurs
Chaque moteur peut aller indépendemment en marche avant / arrière (de -255 à 255)
La valeur indique la puissance à envoyer au moteur, le signe donne le sens de rotation
La base peut aller jusqu'à 0.3 m/s

Attention :
- une puissance inférieure à 40 est souvent trop faible pour actionner les moteurs
- "motorSetPower" n'accepte que des valeurs entières. Pas de flottant !
- Pas de batterie, pas de moteurs (vérifiez la charge à l'aide du témoin "soc")
"""
from Maqueen_Plus import *

motorSetPower(60, 60) # Marche avant (Droit 60, Gauche 60)
sleep(500)
motorSetPower(-60, 0) # Marche arrière à droite (Droit -60, Gauche 0)
sleep(500)
motorSetPower( 0,  0) # Arrêt des moteurs
sleep(500)
motorSetPower( 60, 0) # Marche avant à droite (Droit -60, Gauche 0)
sleep(500)
motorSetPower(-60, -60) # Marche arrière (Droit 60, Gauche 60)
sleep(500)
motorSetPower( 0,  0) # Arrêt des moteurs