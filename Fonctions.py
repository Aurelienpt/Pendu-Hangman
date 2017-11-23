def Erreur(i):
	print("Essai", i, "/ 11")

def Proposition(p):
	p = p.upper()
	p = p[0]
	return p

def Affreponse(mot, trouve):
	reponse = ""
	for lettre in mot:
		if lettre in trouve:
			reponse += lettre
		else:
			reponse += "*"
	return reponse