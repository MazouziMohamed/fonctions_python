# L'énoncé de l'exercice
'''
En important uniquement les fonctions nécessaires du module math,
écrivez deux fonctions pour vérifier la validité de la formule suivante
pour n = 10 :
'''
# la solution corrigée de l'exercice
from math import cos, sin
def estValide(n, x) :
    s1 = 0
    for i in range(n + 1) :
        s1 += cos(i * x)
    s2 = 1/2 + sin((2*n + 1) * x / 2) / (2 * sin(x / 2))
    if abs(s1 - s2) < 1e-9 :
        return True
    return False
# Test, Remarque x != 0
n, x = 10, 1
if estValide(n, x) :
    print(f'La formule est valide pour n = {n}.')
else :
    print(f"La formule n'est pas valide pour n = {n}")