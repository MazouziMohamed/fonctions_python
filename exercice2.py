# L'énoncé de l'exercice
"""
Ecrire un programme utilisant une fonction qui affiche le cube d'un
nombre réel saisi au clavier.
"""
# la solution corrigée de l'exercice
def cube_nombre_reel(nombre_reel) :
    return nombre_reel**3
nombre_reel = float(input('Veuillez entrer un nombre réel : '))
print(f"Le cube de {nombre_reel} est : {cube_nombre_reel(nombre_reel)}")