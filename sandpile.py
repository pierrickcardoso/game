
import pgzrun
# U can edit this
# for dimension n width and eight i recommend using power of 2 big dimension mean longer time to render 
DIMENSION=128 # DIMENSION <= HEIGT 
COLOR_FOR_0='white'
COLOR_FOR_1='brown'
COLOR_FOR_2='orange'
COLOR_FOR_3='pink' 
WIDTH   = 512 # WITDH = HEIGT
HEIGHT  = 512
AMOUNT_TO_START=2**20 # If they are still black put a higher value

#STOP HERE
CELLULE=WIDTH//DIMENSION
TITLE   = "Sandpiles"
LARGEUR = WIDTH  // CELLULE
HAUTEUR = HEIGHT // CELLULE

def est_dans_le_tableau(abs: int, ord: int) -> bool:
    """Vrai ssi la cellule est dans le tableau"""
    return 0 <= abs <LARGEUR  and 0 <= ord < HAUTEUR

def generation(nombre):
    tableau=[]
    for j in range(nombre):
        ligne=[]
        for i in range(nombre):
        	ligne.append(-1)
        tableau.append(ligne)
    return tableau
def spawn_centre(tableau,nombre):
	tableau[len(tableau)//2][len(tableau)//2]=nombre
	return tableau
def is_finish(tableau):
	for i in tableau:
		for elem in i:
			if not elem in [0,1,2,3]:
				return False
	return True

def ecoulement(tableau):
	for i in range(len(tableau)):
			for j in range(len(tableau)):
				if tableau[i][j]>=4:
					nb_a_deplacer=tableau[i][j]//4
					reste=tableau[i][j]%4
					if est_dans_le_tableau(i,j+1):
						tableau[i][j+1]+=nb_a_deplacer
					if est_dans_le_tableau(i,j-1):
						tableau[i][j-1]+=nb_a_deplacer
					if est_dans_le_tableau(i+1,j):
						tableau[i+1][j]+=nb_a_deplacer
					if est_dans_le_tableau(i-1,j):
						tableau[i-1][j]+=nb_a_deplacer
					tableau[i][j]=reste
	return tableau
TABLEAU=generation(DIMENSION)
def draw():
	draw_map(TABLEAU)
def update():
	global TABLEAU,iteration
	if not is_finish(TABLEAU):
		TABLEAU=ecoulement(TABLEAU)
def draw_map(tableau):
	for i in range(len(tableau)):
		for j in range(len(tableau)):
			if tableau[i][j]==0:
				screen.draw.filled_rect(Rect(i*CELLULE, j*CELLULE, CELLULE, CELLULE), COLOR_FOR_0)
			if tableau[i][j]==1:
				screen.draw.filled_rect(Rect(i*CELLULE, j*CELLULE, CELLULE, CELLULE), COLOR_FOR_1)	
			if tableau[i][j]==2:
				screen.draw.filled_rect(Rect(i*CELLULE, j*CELLULE, CELLULE, CELLULE), COLOR_FOR_2)
			if tableau[i][j]==3:
				screen.draw.filled_rect(Rect(i*CELLULE, j*CELLULE, CELLULE, CELLULE), COLOR_FOR_3)

spawn_centre(TABLEAU,AMOUNT_TO_START)

pgzrun.go()
