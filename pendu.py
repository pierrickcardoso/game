#import pgzrun
from random import *
import sys
import time
liste_mot=["jeux","rien","test","ordinateur","amour", "bonjour", "chocolat", "dejeuner", "ecole", "fete",
    "gateau", "hotel", "idee", "jardin", "kiwi", "lampe", "metro",
    "nouveau", "opera", "piano", "quartier", "restaurant", "salade",
    "theatre", "urgent", "vacances", "wagon", "xylophone", "zebre","animal", "basket", "cactus", "dollar", "email", "football",
    "guitare", "hamburger", "internet", "jazz", "kayak", "laser", "micro",
    "nomade", "ocean", "puzzle", "quatar", "robot", "sandwich", "tennis",
    "unique","wagon", "zero", "yoga", "zeppelin",   "chat", "chien", "voiture", "maison", "soleil", "fleur", "arbre", "plage",
    "montagne", "ordinateur", "musique", "livre", "film", "cuisine", "jardin",
    "fenetre", "porte", "ecole", "travail", "vacances", "famille", "amour",
    "amitie", "sport", "voyage", "art", "nuit", "jour", "mer", "rivière", "lac",
    "paysage", "ville", "campagne", "ciel", "terre", "espace", "temps", "histoire",
    "science", "mathematiques", "energie", "electricite", "internet", "python",
    "programmation", "algorithmes", "donnees", "intelligence", "modèle", "apprentissage",
    "connaissance", "information", "communication", "technologie", "robot", "avenir",
    "passe", "present", "realite", "reve", "espoir", "peur", "joie", "tristesse",
    "colère", "sante", "maladie", "medecine", "alimentation", "sommeil", "exercice",
    "meditation", "bonheur", "succès", "echec", "projet", "objectif", "resolution",
    "effort", "recompense", "creativite", "innovation", "imagination", "expression",
    "culture", "langue", "poesie", "theatre", "musee", "peinture", "sculpture",
    "photographie", "danse", "musicien", "artiste", "ecrivain", "philosophie", "religion",
    "spiritualite", "ethique", "morale", "politique", "economie", "societe", "environnement",
    "developpement", "responsabilite", "education", "enseignement", "apprentissage",
    "etudiant", "professeur", "savoir", "ecole", "universite", "elève", "cours",
    "matière", "sciences", "lettres", "langues", "histoire", "geographie", "mathematiques",
    "physique", "chimie", "biologie", "informatique", "sante", "medecine", "ingenierie",
    "technologie", "arts", "sport", "philosophie", "religion", "ethique", "politique",
    "economie", "sociologie", "psychologie", "linguistique", "communication", "medias",
    "culture", "environnement", "developpement", "histoire", "archeologie", "geologie",
    "astronomie", "astrophysique", "cosmologie", "physiologie", "neurosciences", "psychologie",
    "sociologie", "anthropologie", "ecologie", "biodiversite", "climat", "energie",
    "developpement", "economie", "technologie", "innovation", "science","fiction", "fantasie",
    "aventure", "policier", "romance", "horreur", "thriller", "biographie", "autobiographie",
    "essai", "poesie", "theatre", "philosophie", "religion", "histoire", "sciences",
    "societe", "politique", "economie", "psychologie", "art", "musique", "cinema",
    "danse", "peinture", "sculpture", "architecture", "photographie", "mode", "cuisine",
    "voyage", "nature", "animaux", "plantes", "environnement", "astronomie", "espace",
    "technologie", "informatique", "robotique", "intelligence", "internet", "medias",
    "reseaux sociaux", "communication", "jeux", "sport", "fitness", "yoga", "meditation",
    "voyage", "aventure", "decouverte", "culture", "tradition", "gastronomie", "musique",
    "danse", "festival", "celebration", "fete", "rituel", "coutume", "folklore",
    "histoire", "mythologie", "religion", "spiritualite", "philosophie", "sagesse",
    "verite", "beaute", "bonte", "justice", "amour", "paix", "harmonie", "liberte",
    "egalite", "fraternite", "solidarite", "tolerance", "respect", "responsabilite",
    "engagement", "espoir", "courage", "confiance", "patience", "perseverance",
    "reussite", "bonheur", "sante", "prosperite", "generosite", "gratitude", "humilite",
    "compassion", "joie", "creativite", "innovation", "imagination", "expression",
    "communication", "collaboration", "communaute", ]








if len(sys.argv) > 1:                       # l'utilisateur a tape un argument
    expression = sys.argv[1]                # expression : le premier argument
    token = expression.strip().split()      # decoupe l'expression en une liste
    mot=token[0]
else:
	mot=choice(liste_mot)

def jeux(mot):
	if len(mot)<=7:
		NB_VIE=12
	else:
		NB_VIE=8
	a_afficher="_"*len(mot)
	test=list(a_afficher)
	print(f"Le mot est {formatage(test)} et il vous reste {NB_VIE} vie")
	while NB_VIE>0:
		if est_trouve(mot,formatage(test)):
			break
		lettre=input("lettre a jouer ?")
		time.sleep(0.1)
		if lettre in mot:
			indice=indice_lettre(mot,lettre)
			changer_lettre(lettre,indice,test)
		else:
			NB_VIE-=1
		print(f"Le mot est {formatage(test)} ,et il vous reste {NB_VIE} vie")
	if est_trouve(mot,formatage(test)):
		print(f"Vous avez gagne il vous restait {NB_VIE} le mot etait {mot}")
	else:
		print(f"Vous avez perdu le mot etait {mot}")
def changer_lettre(lettre,indice,en_cours):
	for i in indice:
		en_cours[i]=lettre
def indice_lettre(mot,lettre):
	indice=[]
	for i in range(len(mot)):
		if mot[i]==lettre:
			indice.append(i)
	return indice	
def est_trouve(mot,test):
	for i in range(len(mot)):
		if not mot[i]==test[i]:
			return False
	return True
def formatage(liste):
	mot=""
	for i in liste:
		mot=mot+i
	return mot
#parti graphique"
"""WIDTH   = CELLULE*DIMENSION+20
HEIGHT  = CELLULE*DIMENSION+20
TITLE   = "DEMINEUR"
elapsed_time_at_pause = 0
LARGEUR = WIDTH  // CELLULE
HAUTEUR = HEIGHT // CELLULE


def update():
def draw():
def on_mouse_down(pos):


pgzrun.go()"""
jeux(mot)
    