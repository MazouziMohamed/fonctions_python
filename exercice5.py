# L'énoncé de l'exercice
"""
Écrire un programme qui demande à l'utilisateur d'entrer un entier, puis
le programme utilise une fonction pour compte et affiche le nombre de
chiffres qui composent cet entier.
"""
# la solution corrigée de l'exercice
def nombre_chiffres(entier) :
    temp = 1
    entier = abs(entier) // 10
    while entier != 0 :
        temp += 1
        entier //= 10
    return temp
entier = int(input('Veuillez entrer un entier : '))
print(f"Le nombre de chiffres qui composent {entier} est : {nombre_chiffres(entier)}")