# L'énoncé de l'exercice
"""
Ecrire un programme utilisant une fonction qui détermine si un nombre
est premier ou non (rappel : un nombre premier n'est divisible que par 1
et par lui-même).
"""
# la solution corrigée de l'exercice
def estPremier(nombre_premier) :
    if nombre_premier < 2:
        return False
    for i in range(2, nombre_premier // 2 + 1) :
        if nombre_premier % i == 0 :
            return False
    return True
nombre_premier = int(input('Veuillez entrer un nombre premier(supérieur ou égale à 2) : '))
if estPremier(nombre_premier) : print(f"{nombre_premier} est un nombre premier.")
else : print(f"{nombre_premier} n'est pas un nombre premier.")