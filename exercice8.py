# L'énoncé de l'exercice
'''
Écrivez un programme qui demande à l'utilisateur d'entrer un nombre L
de lignes. Ensuite, le programme basé sur une fonction dessine le
triangle suivant :
'''
# la solution corrigée de l'exercice
def triangle_etoiles(nombre_lignes) :
    for ligne in range(nombre_lignes) :
        for espace in range(nombre_lignes-ligne-1) :
            print(end = ' ')
        for etoile in range(ligne+1) :
            print(end = '* ')
        print()
# test
triangle_etoiles(5)
triangle_etoiles(2)
triangle_etoiles(7)