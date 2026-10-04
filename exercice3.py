# L'énoncé de l'exercice
"""
Ecrire un programme qui demande à l'utilisateur de saisir une année et
qui utilise une fonction pour vérifie si l'année est bissextile (366 jours) ou
non.
"""
# la solution corrigée de l'exercice
def estBissextile(annee) :
    if (annee%4 == 0 and annee%100 != 0) or annee%400 == 0 :
        return True
    return False
annee = int(input('Veuillez entrer une année : '))
if estBissextile(annee) : print(f"{annee} est une année bissextile.")
else : print(f"{annee} n'est pas une année bissextile.")