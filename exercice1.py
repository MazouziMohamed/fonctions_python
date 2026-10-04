# L'énoncé de l'exercice
"""
Ecrire un programme utilisant une fonction qui affiche le tableau de
multiplication d'un entier positif.
"""
# la solution corrigée de l'exercice
def tableau_multiplication(entier_naturel) :
    for i in range(11) :
        print(f"{entier_naturel} * {i} = {entier_naturel*i}")
while True :
    entier_naturel = int(input('Veuillez entrer un entier naturel : '))
    if entier_naturel < 0 :
        continue
    break
print(f'+----------------------- Le tableau de multiplication de {entier_naturel} -----------------------+')
tableau_multiplication(entier_naturel)