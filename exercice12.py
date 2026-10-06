# L'énoncé de l'exercice
'''
Ecrire un programme qui évalue les fonctions mathématiques suivantes :
f(x) = cos(4x)
f'(x) = -4sin(4x)
f''(x) = -16cos(4x)
Calculer les résultats de pour les valeurs suivantes :
x = 0 , x = pi/2 , x = pi , x = -pi/2
'''
# la solution corrigée de l'exercice
from math import cos, sin, pi
def f(x) :
    return cos(4*x)
def f_prime(x) :
    return -4*sin(4*x)
def f_seconde(x) :
    return -16*cos(4*x)
# Test
x = 0
print(f"Pour x = {x}")
print('-'*20)
print(f"f({x}) = {f(x)}")
print(f"f'({x}) = {f_prime(x)}")
print(f"f''({x}) = {f_seconde(x)}")
x = pi/2
print(f"Pour x = {x}")
print('-'*20)
print(f"f({x}) = {f(x)}")
print(f"f'({x}) = {f_prime(x)}")
print(f"f''({x}) = {f_seconde(x)}")
x = pi
print(f"Pour x = {x}")
print('-'*20)
print(f"f({x}) = {f(x)}")
print(f"f'({x}) = {f_prime(x)}")
print(f"f''({x}) = {f_seconde(x)}")
x = -pi/2
print(f"Pour x = {x}")
print('-'*20)
print(f"f({x}) = {f(x)}")
print(f"f'({x}) = {f_prime(x)}")
print(f"f''({x}) = {f_seconde(x)}")