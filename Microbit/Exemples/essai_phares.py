"""
Essai des phares

Le robot possède 2 phares avant
Chaque phare est indépendant, et peut adopter 8 couleurs (de 0 à 7)
Noir (éteint) Blanc Rouge Vert Bleu Cyan Rose Jaune
Les phares sont utilisables même sans batterie
"""
from Maqueen_Plus import *

pharesSetRGB(1, 7) 
sleep(500)
pharesSetRGB(5, 4) 
sleep(500)
pharesSetRGB(0, 0) # Extinction des phares