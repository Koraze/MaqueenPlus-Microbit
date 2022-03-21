"""
Dans ce programme, le robot va uniquement en marche avant lente
Il fait une marche arrière rapide et brève s'il rencontre du vide
"""
from Maqueen_Plus import *

# Marche avant lente
motorSetPower(40, 40) # Impulsion pour démarrer le robot (démarrer à 25 n'est pas possible)
sleep(100)
motorSetPower(25, 25) # Puissance de croisière

# Ne rien faire tant qu'il y a du sol
while sum(groundReadLogique()) == 0:
    pass

# Marche arrière rapide brève
motorSetPower(-70, -70)
sleep(800)
motorSetPower(0, 0)
    
    