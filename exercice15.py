# L'énoncé de l'exercice
'''
Créer un programme qui permet qui permet de tester la conjecture de la
suite de Syracuse.
'''
# la solution corrigée de l'exercice
def estVerifie(n) :
    while n!= 1 :
        if n%2 == 0 :
            n //= 2
        else :
            n = 3*n + 1
    return True
# Test (Remarque : il faut n > 0)
n = 15
if estVerifie(n) :
    print(f"La conjecture de la suite de syracuse est vérifie pour n = {n}")
else :
    print(f"La conjecture de la suite de syracuse n'est pas vérifie pour n = {n}")