import pgzrun

CELLULE = 50
DIMENSION=3
WIDTH   = CELLULE*DIMENSION
HEIGHT  = CELLULE*DIMENSION
TITLE   = "TIC TAC TOE"

LARGEUR = WIDTH  // CELLULE
HAUTEUR = HEIGHT // CELLULE
CROIX_WIN=0
ROND_WIN=0
class Jeux:
	def __init__(self):
		self.turn=0
		self.map=self.generer_map()
		self.en_cours=True
	def generer_map(self):
		liste=[]
		for i in range(0,3):
			temp=[]
			for j in range(0,3):
				temp.append([])
			liste.append(temp)
		return liste
	def have_started(self):
		for i in range(len(self.map)):
			for j in range(len(self.map)):
				if self.map[i][j]==[]:
					return True
		return False
	def a_jouer(self,i,j):
		if self.en_cours:
			if self.turn%2==0 and self.map[i][j]==[]:
				self.map[i][j]="X"
			else:
				if self.map[i][j]==[]:
					self.map[i][j]="O"
			self.turn+=1

	def get_turn(self):
		return self.turn==9	
	def reset(self):
		self.turn=0
		self.map=self.generer_map()
		self.en_cours=True
	def stop(self):
		self.en_cours=False 
	def draw_map(self):
		screen.fill("white")
		screen.draw.filled_rect(Rect(50,0, 1, CELLULE*3+15),"Black")
		screen.draw.filled_rect(Rect(100,0, 1, CELLULE*3+15),"Black")
		screen.draw.filled_rect(Rect(0,50, CELLULE*3+15,1),"Black")
		screen.draw.filled_rect(Rect(0,100, CELLULE*3+15,1 ),"Black")
		tableau=self.map
		for i in range(len(tableau)):
			for j in range(len(tableau)):
				if tableau[i][j]!=[]:
					screen.draw.text(str(tableau[i][j]), (i*CELLULE+20, j*CELLULE+20),color ="Black",fontsize=40)
jeux=Jeux()
def on_mouse_down(pos):
    """bascule chaque case cliquée"""
    x, y = pos
    abs = x // CELLULE
    ord = y // CELLULE
    jeux.a_jouer(abs,ord)


def draw():
	jeux.draw_map()
def clavier():
	if keyboard[keys.ESCAPE]:
		exit()
	if keyboard[keys.R]:
		jeux.reset()
def update():
	clavier()
	if not jeux.en_cours:
		print("EGALITE")
		jeux.reset()
	if jeux.get_turn():
		verification_croix(jeux.map) 
		verification_rond(jeux.map)
		jeux.stop()

	if jeux.have_started():
		verification_croix(jeux.map) 
		verification_rond(jeux.map) 
	
		


def verification_croix(matrice):
    for i in range (3):
        if matrice[i][0] == matrice[i][1] == matrice[i][2]=="X":
            victoire_croix()
            return True
    for i in range(3):
        if matrice[0][i] == matrice[1][i] == matrice[2][i]=="X":
            victoire_croix()
            return True
    if matrice[0][0] == matrice[1][1] == matrice[2][2]=="X" :
        victoire_croix()
        return True
    if matrice[0][2] == matrice[1][1] == matrice[2][0]=="X" :
        victoire_croix()
        return True
def verification_rond(matrice):
    for i in range (3):
        if matrice[i][0] == matrice[i][1] == matrice[i][2]=="O":
            victoire_rond()
            return True
    for i in range(3):
        if matrice[0][i] == matrice[1][i] == matrice[2][i]=="O":
            victoire_rond()
            return True
    if matrice[0][0] == matrice[1][1] == matrice[2][2]=="O" :
        victoire_rond()
        return True
    if matrice[0][2] == matrice[1][1] == matrice[2][0]=="O" :
        victoire_rond()
        return True
def victoire_croix():
	global CROIX_WIN
	CROIX_WIN+=1
	print(f"Victoire des croix qui on actuellement {CROIX_WIN} victoire contre {ROND_WIN} pour les rond ")
	jeux.reset()
def victoire_rond():
	global ROND_WIN
	ROND_WIN+=1
	print(f"Victoire des ROND qui on actuellement {ROND_WIN} victoire contre {CROIX_WIN} pour les CROIX ")
	jeux.reset()
pgzrun.go()