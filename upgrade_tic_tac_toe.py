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

pgzrun.go()
