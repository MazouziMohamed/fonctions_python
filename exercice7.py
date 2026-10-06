# L'énoncé de l'exercice
'''
Ecrire un programme qui affiche la ou les solutions d'une équation du
second degré de la forme ax² + bx + c. Utiliser une fonction pour calculer
le discriminant Delta et une autre pour afficher les solution selon delta.

PS : Pour calculer la racine carrée d'un nombre, nous utilisons la fonction : sqrt.
Exemple : Après l'exécution de l'instruction suivante la valeur de A sera 2.
import math
A = math.sqrt(4)
'''
# la solution corrigée de l'exercice
from math import sqrt
def equation_premier_degre(a, b) :
    if a == 0 :
        if b == 0 :
            print("L'ensemble des solutions est : l'ensemble des nombres réels")
        else :
            print("L'ensemble des solutions est : l'ensemble vide")
    else :
        racine_double = -b / a
        print("L'ensemble des solutions est : S = {", racine_double, "}")
def equation_second_degre(a, b, c) :
    if a == 0 :
        equation_premier_degre(b, c)
    else :
        delta = b**2 - 4*a*c
        if delta > 0 :
            premiere_solution = (-b - sqrt(delta)) / (2*a)
            deuxieme_solution = (-b + sqrt(delta)) / (2*a)
            print("L'ensemble des solutions est : S = {", premiere_solution, ";", deuxieme_solution, "}")
        elif delta == 0 :
            racine_double = -b / (2*a)
            print("L'ensemble des solutions est : S = {", racine_double, "}")
        else :
            print("L'ensemble des solutions est : l'ensemble vide")
a = float(input('Veuillez entrer la valeur du coefficient a : '))
b = float(input('Veuillez entrer la valeur du coefficient b : '))
c = float(input('Veuillez entrer la valeur du coefficient c : '))
equation_second_degre(a, b, c)