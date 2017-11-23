import random
from Donnees import mots, essais
from Fonctions import Erreur, Proposition, Affreponse
errorlvl = 0
print("Selection d'un mot aleatoire")
i = random.randint(0, len(mots)-1)
mot = mots[i]
mot = str(mot)
trouve = []
while errorlvl != essais:
	reponse = Affreponse(mot, trouve)
	print(reponse)
	if reponse == mot:
		print("Bravo vous n'etes pas mort :)")
		exit()
	proposition = input("Entrez une lettre : ")
	proposition = Proposition(proposition)
	if proposition in mot:
		print("Bravo ! Vous avez trouver la lettre", proposition)
		trouve.append(proposition)
	else:
		errorlvl += 1
		print(proposition, "n'est pas dans le mot")
		Erreur(errorlvl)
print("Perdu le mot etait", mot)