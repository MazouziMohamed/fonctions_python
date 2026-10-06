# L'énoncé de l'exercice
'''
Ecrire un programme qui affiche le résultat de lancement d'un dé, nous
gagnons la partie si le numéro est 2 ou 5, sinon nous perdons la partie.
- Ajoutez les instructions qui vous permettent de simuler ce jeu 10 fois,
en affichant à chaque fois «gagné» ou «perdu».
- Ajoutez les instructions pour compter combien de fois nous gagnons si
nous jetons le dé 1000 fois successives.
'''
# la solution corrigée de l'exercice
from random import randint
def lancement_de_n_fois() :
    nombre_aleatoire = randint(1, 6)
    if nombre_aleatoire == 2 or nombre_aleatoire == 5 :
        return True
    return False
# Test
n = 10
print(f'Pour n = {n}')
for i in range(n) :
    if lancement_de_n_fois() :
        print('Gagné')
    else :
        print('Perdu')
n, somme_fois_gagne = 1000, 0
for i in range(n) :
    if lancement_de_n_fois() :
        somme_fois_gagne += 1
print(f'nous gagnons {somme_fois_gagne} fois si nous jetons le dé {n} fois successives.')