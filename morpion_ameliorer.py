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
class File:
	def __init__(self):
		self.file=[]
	def enfiler(self,element):
		self.file.append(element)
	def defiler(self):
		return self.file.pop(0)
	def longueur_file(self):
		return len(self.file)
	def __repr__(self):
		return str(self.file)
class Jeux:
	def __init__(self):
		self.jeux=self.generer_map()
		self.p1=File()
		self.p2=File()
		self.turn=0
	def reset(self):
		self.jeux=self.generer_map()
		self.p1=File()
		self.p2=File()
		self.turn=0
	def generer_map(self):
		liste=[]
		for i in range(0,3):
			temp=[]
			for j in range(0,3):
				temp.append("")
			liste.append(temp)
		return liste
	def jouer(self,i,j):
		if self.turn%2==0:
			if self.jeux[i][j]=="":
				self.jeux[i][j]="X"
				self.p1.enfiler([i,j])
		else:
			self.jeux[i][j]="O"
			self.p2.enfiler([i,j])
		self.turn+=1
	def verif(self):
		if self.p1.longueur_file()==4:
			temp=self.p1.defiler()
			self.jeux[temp[0]][temp[1]]=""
		if self.p2.longueur_file()==4:
			temp=self.p2.defiler()
			self.jeux[temp[0]][temp[1]]=""

	def __repr__(self):
		return f"{self.jeux},{self.p1},{self.p2}"
	def draw_map(self):
		screen.fill("white")
		screen.draw.filled_rect(Rect(50,0, 1, CELLULE*3+15),"Black")
		screen.draw.filled_rect(Rect(100,0, 1, CELLULE*3+15),"Black")
		screen.draw.filled_rect(Rect(0,50, CELLULE*3+15,1),"Black")
		screen.draw.filled_rect(Rect(0,100, CELLULE*3+15,1 ),"Black")
		tableau=self.jeux
		for i in range(len(tableau)):
			for j in range(len(tableau)):
				if tableau[i][j]!=[]:
					screen.draw.text(str(tableau[i][j]), (i*CELLULE+20, j*CELLULE+20),color ="Black",fontsize=40)
def on_mouse_down(pos):
    """bascule chaque case cliquée"""
    x, y = pos
    abs = x // CELLULE
    ord = y // CELLULE
    jeux.jouer(abs,ord)
jeux=Jeux()
def draw():
	jeux.draw_map()
def clavier():
	if keyboard[keys.ESCAPE]:
		exit()
def update():
	clavier()
	jeux.verif()
	verification_croix(jeux.jeux)
	verification_rond(jeux.jeux)
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
pgzrun.go()