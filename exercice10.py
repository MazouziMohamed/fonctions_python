# L'énoncé de l'exercice
'''
Ecrire une fonction affiche_employee() de telle sorte qu'elle accepte le
nom de l'employé et son salaire et affiche les deux. Si le salaire manque
dans l'appel de fonction, attribuez la valeur par défaut 3000 au salaire.
'''
# la solution corrigée de l'exercice
def affiche_employee(nom_employe, salaire_employe = 3000) :
    print(f"Le salaire d'employé {nom_employe} est : {salaire_employe}")
# Test
nom_employe = input("Veuillez entrer le nom d'employé : ")
#salaire_employe = float(input("Veuillez entrer le salaire d'employé : "))
affiche_employee(nom_employe)