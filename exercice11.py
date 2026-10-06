# L'énoncé de l'exercice
'''
Créer une fonction Python qui prend x comme argument et renvoie y. y
est calculé à l'aide de la fonction suivante:
f(x) = 4 * (x**3) - 13 * (x**2) + x - 60
'''
# la solution corrigée de l'exercice
def f(x) :
    return 4*(x**3) - 13*(x**2) + x - 60
# Test
x = 0
print(f"f({x}) = {f(x)}")
x = 1
print(f"f({x}) = {f(x)}")