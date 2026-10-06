# L'énoncé de l'exercice
'''
Écrire une fonction qui vérifie si un nombre est parfait ou non.
Un nombre est dit parfait s'il est égal à la somme de ses diviseurs
propres (diviseurs de ce nombre autres que lui-même).
'''
# la solution corrigée de l'exercice
def estParfait(entier_naturel) :
    somme_diviseurs_propres = 1
    for i in range(2, entier_naturel//2+1) :
        if entier_naturel%i == 0 :
            somme_diviseurs_propres += i
    if somme_diviseurs_propres == entier_naturel :
        return True
    return False
# Test
entier_naturel = 6
if estParfait(entier_naturel) :
    print(f"{entier_naturel} est un nombre parfait.")
else :
    print(f"{entier_naturel} n'est pas un nombre parfait.")