import pgzrun
import random
import time 
WIDTH   = 600
HEIGHT  = 600
TITLE   = "Dodger"

global score
score=0
class Joueur:
	def __init__(self,posx,posy):
		self.posx=posx
		self.posy=posy
		self.alive=True
	def left(self):
		self.posx-=10
	def right(self):
		self.posx+=10
	def down(self):
		self.posy+=10
	def up(self):
		self.posy-=10
	def est_sortie(self):
		if self.posy>HEIGHT:
			self.posy=0
		if self.posy<0:
			self.posy=HEIGHT
		if self.posx>WIDTH:
			self.posx=0
		if self.posx<0:
			self.posx=WIDTH
class rectangle:
	def __init__(self):
		self.x=random.randint(0,WIDTH)
		self.y=-10
	def descendre(self):
		self.y+=10
	def est_sortie(self):
		if self.y>HEIGHT:
			self.x=random.randint(0,WIDTH)
			self.y=-10
			return True
player1=Joueur(0,0)
player2=Joueur(0,0)
rectangle1=rectangle()
def clavier():
    if keyboard[keys.ESCAPE]:
        exit()
    if keyboard[keys.UP]:
        player1.up()
    if keyboard[keys.DOWN]:
        player1.down()
    if keyboard[keys.RIGHT]:
        player1.right()
    if keyboard[keys.LEFT]:
        player1.left()
    if keyboard[keys.Z]:
        player2.up()
    if keyboard[keys.S]:
        player2.down()
    if keyboard[keys.D]:
        player2.right()
    if keyboard[keys.Q]:
        player2.left()   

def draw_tableau():
	screen.fill("grey")
	screen.draw.text(str(score),topright=(100, 20), color="orange")
	if player1.alive:
		screen.draw.filled_rect(Rect(player1.posx, player1.posy, 50, 50), "blue")
	screen.draw.filled_rect(Rect(rectangle1.x, rectangle1.y, 50, 50), "red")
	if player2.alive:
		screen.draw.filled_rect(Rect(player2.posx, player2.posy, 50, 50), "green")
def collison():
	if (rectangle1.x<player1.posx < rectangle1.x+50 and rectangle1.y<player1.posy < rectangle1.y+50) or (rectangle1.x<player1.posx+50 < rectangle1.x+50 and rectangle1.y<player1.posy+50 < rectangle1.y+50) or (rectangle1.x<player1.posx < rectangle1.x+50 and rectangle1.y<player1.posy+50 < rectangle1.y+50) or (rectangle1.x<player1.posx+50 < rectangle1.x+50 and rectangle1.y<player1.posy < rectangle1.y+50):
		player1.alive=False
	if (rectangle1.x<player2.posx < rectangle1.x+50 and rectangle1.y<player2.posy < rectangle1.y+50) or (rectangle1.x<player2.posx+50 < rectangle1.x+50 and rectangle1.y<player2.posy+50 < rectangle1.y+50) or (rectangle1.x<player2.posx < rectangle1.x+50 and rectangle1.y<player2.posy+50 < rectangle1.y+50) or (rectangle1.x<player2.posx+50 < rectangle1.x+50 and rectangle1.y<player2.posy < rectangle1.y+50):
		player2.alive=False
	if not player1.alive and not player2.alive:
		player1.posx=5
		player1.posy=0
		player2.posx=5
		player2.posy=0
		player1.alive=True
		player2.alive=True
def draw():
    draw_tableau()
def update():
    global score
    clavier()
    player1.est_sortie()
    rectangle1.descendre()
    player2.est_sortie()
    if rectangle1.est_sortie():
    	score+=1
    collison()
pgzrun.go()