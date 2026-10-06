# L'énoncé de l'exercice
"""
Ecrire un programme utilisant des fonctions qui demande à l'utilisateur
de saisir le rayon du cercle, puis le programme affiche le diamètre, la
surface et le périmètre du cercle.
"""
# la solution corrigée de l'exercice
from math import pi
def diametre_cercle(rayon_cercle) :
    return rayon_cercle*2
def surface_cercle(rayon_cercle) :
    return pi*(rayon_cercle**2)
def perimetre_cercle(rayon_cercle) :
    return 2*pi*rayon_cercle
rayon_cercle = float(input('Veuillez entrer le rayon du cercle : '))
print(f"Le diamètre du cercle est : {diametre_cercle(rayon_cercle)}")
print(f"La surface du cercle est : {surface_cercle(rayon_cercle)}")
print(f"Le périmètre du cercle est : {perimetre_cercle(rayon_cercle)}")