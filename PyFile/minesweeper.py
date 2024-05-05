import pgzrun
from random import *
import time
CELLULE = 40
DIMENSION=16
WIDTH   = CELLULE*DIMENSION+20
HEIGHT  = CELLULE*DIMENSION+20
TITLE   = "DEMINEUR"
LARGEUR = WIDTH  // CELLULE
HAUTEUR = HEIGHT // CELLULE
BOMBE  = 1
PAS_BOMBE  = 0
NB_BOMBE=40
FIRST_CLICK=True
def est_dans_le_tableau(abs: int, ord: int) -> bool:
    """Vrai ssi la cellule est dans le tableau"""
    return 0 <= abs < LARGEUR and 0 <= ord < HAUTEUR 

class bombe:
    def __init__(self):
        self.is_bombe=PAS_BOMBE
        self.voisine_bombe=0
        self.already_count=False
    def chnager_voisin(self,nombre):
        self.voisine_bombe=nombre
        return
    def switch_to_bomb(self):
        self.is_bombe=BOMBE
    def get_etat(self):
        return self.is_bombe
    def update_voisin_bombe(self):
        self.voisine_bombe+=1
    def get_voisine_bombe(self):
        return self.voisine_bombe
    def __repr__(self):
        return str(self.is_bombe)
class Map:
    def __init__(self):
        self.tableau=[]
        self.nb_bombe=40
        self.dimension=DIMENSION
        self.nb_presente=0
        self.show_bombe=False
        self.nb_bleue=0
        self.have_been_reset=False
    def update_nb_bleu(self):
        self.nb_bleue=self.nb_bleue+1
    def remove_nb_bleu(self):
        self.nb_bleue=self.nb_bleue-1
    def reset(self):
        self.creer_map()
        self.nb_bombe=40
        self.dimension=DIMENSION
        self.nb_presente=0
        self.show_bombe=False
        self.nb_bleue=0
        self.have_been_reset=True
    def get_nb_bleue(self):
        return self.nb_bleue
    def draw_map(self):
        tableau=Map
        if self.show_bombe:
            for i in range(len(self.tableau)):
                for j in range(len(self.tableau)):
                    x = self.tableau[i][j][1]* CELLULE
                    y =  self.tableau[i][j][2] *CELLULE
                    if self.tableau[i][j][0].get_etat()==1:
                        couleur="red"
                        screen.draw.filled_rect(Rect(x, y, CELLULE, CELLULE), couleur)
        else:
            for i in range(len(self.tableau)):
                for j in range(len(self.tableau)):
                    x = self.tableau[i][j][1]* CELLULE
                    y =  self.tableau[i][j][2] *CELLULE
                    if self.tableau[i][j][3]=="":
                        if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                            couleur="black"
                        else:
                            couleur="grey"
                        screen.draw.filled_rect(Rect(x, y, CELLULE, CELLULE), couleur)
                    if self.tableau[i][j][3]=="1":
                        couleur="blue"
                        screen.draw.filled_rect(Rect(x, y, CELLULE, CELLULE), couleur)
                    if self.tableau[i][j][3]=="0": 
                        texte=self.tableau[i][j][0].get_voisine_bombe()
                        if texte==0:
                            screen.draw.filled_rect(Rect(x, y, CELLULE, CELLULE), "white")
                        else:
                            screen.draw.filled_rect(Rect(x, y, CELLULE, CELLULE), "white")
                            screen.draw.text(str(texte), (x+15,y+15), color="black")
            screen.draw.text(str(self.get_nb_bleue()), (HEIGHT-20,HEIGHT-20), color="black")
            screen.draw.text("Nombre de drapeau", (HEIGHT-200,HEIGHT-20), color="black")
            screen.draw.text("nombre de bombe restante " +str(self.nb_bombe-self.get_nb_bleue()), (HEIGHT-650,HEIGHT-20), color="black")
    def ajout_bombe(self,x,y):
        while self.nb_presente!=self.nb_bombe:
            coordonee_x=randint(0,15)
            coordonne_y=randint(0,15)
            if coordonee_x==x and coordonne_y==y:
                pass
            else:
                if self.tableau[coordonee_x][coordonne_y][0].get_etat()==1:
                    pass
                else:
                    self.tableau[coordonee_x][coordonne_y][0].switch_to_bomb()
                    self.nb_presente+=1
    def compter_voisin_bombe(self,abs,ord):
        if not self.tableau[abs][ord][0].already_count:
            if est_dans_le_tableau(abs - 1, ord - 1):
                if self.tableau[abs-1][ord-1][0].get_etat()==1:
                    self.tableau[abs][ord][0].update_voisin_bombe()
            if est_dans_le_tableau(abs    , ord - 1):
                if self.tableau[abs][ord-1][0].get_etat()==1:
                    self.tableau[abs][ord][0].update_voisin_bombe()
            if est_dans_le_tableau(abs + 1, ord - 1):
                if self.tableau[abs+1][ord-1][0].get_etat()==1:
                    self.tableau[abs][ord][0].update_voisin_bombe()
            if est_dans_le_tableau(abs - 1, ord    ):
                if self.tableau[abs-1][ord][0].get_etat()==1:
                    self.tableau[abs][ord][0].update_voisin_bombe()
            if est_dans_le_tableau(abs + 1, ord    ):
                if self.tableau[abs+1][ord][0].get_etat()==1:
                    self.tableau[abs][ord][0].update_voisin_bombe()
            if est_dans_le_tableau(abs - 1, ord + 1):
                if self.tableau[abs-1][ord+1][0].get_etat()==1:
                    self.tableau[abs][ord][0].update_voisin_bombe()
            if est_dans_le_tableau(abs    , ord + 1):
                if self.tableau[abs][ord+1][0].get_etat()==1:
                    self.tableau[abs][ord][0].update_voisin_bombe()
            if est_dans_le_tableau(abs + 1, ord + 1):
                if self.tableau[abs+1][ord+1][0].get_etat()==1:
                    self.tableau[abs][ord][0].update_voisin_bombe()
        self.tableau[abs][ord][0].already_count=True
    def creer_map(self):
        self.tableau=[]
        for j in range(self.dimension):
            ligne=[]
            for i in range(self.dimension):
                a_ajouter=bombe()
                ligne.append([a_ajouter,j,i,""])
            self.tableau.append(ligne)
        return self.tableau
    def changer_etat(self, x, y):
        if self.tableau[x][y][0].get_etat() == 1:
            self.loose()
        else:
            if self.tableau[x][y][3] == "":
                self.tableau[x][y][3] = "0"
                self.compter_voisin_bombe(x, y)
            if self.tableau[x][y][0].get_voisine_bombe() == 0:
                if est_dans_le_tableau(x - 1, y - 1):
                    if self.tableau[x - 1][y - 1][3] == "":
                        self.changer_etat(x - 1, y - 1)
                if est_dans_le_tableau(x, y - 1):
                    if self.tableau[x][y - 1][3] == "":
                        self.changer_etat(x, y - 1)
                if est_dans_le_tableau(x + 1, y - 1):
                    if self.tableau[x + 1][y - 1][3] == "":
                        self.changer_etat(x + 1, y - 1)
                if est_dans_le_tableau(x - 1, y):
                    if self.tableau[x - 1][y][3] == "":
                        self.changer_etat(x - 1, y)
                if est_dans_le_tableau(x + 1, y):
                    if self.tableau[x + 1][y][3] == "":
                        self.changer_etat(x + 1, y)
                if est_dans_le_tableau(x - 1, y + 1):
                    if self.tableau[x - 1][y + 1][3] == "":
                        self.changer_etat(x - 1, y + 1)
                if est_dans_le_tableau(x, y + 1):
                    if self.tableau[x][y + 1][3] == "":
                        self.changer_etat(x, y + 1)
                if est_dans_le_tableau(x + 1, y + 1):
                    if self.tableau[x + 1][y + 1][3] == "":
                        self.changer_etat(x + 1, y + 1)

    def loose(self):
        self.show_bombes()
    def show_bombes(self):
        self.show_bombe=True
    def click_droit(self,x,y):
        if self.tableau[x][y][3]=="1":
            self.tableau[x][y][3]=""
            self.remove_nb_bleu()
        else:
            self.tableau[x][y][3]="1"
            self.update_nb_bleu()
    def __repr__(self):
        return str(self.tableau)
def update():
    clavier()  
def clavier():
    if keyboard[keys.UP]:
        map.nb_bleue=40
    if keyboard[keys.ESCAPE]:
        exit()
    if keyboard[keys.SPACE]:
        map.show_bombes()
    if keyboard[keys.R]:
        map.reset()
        FIRST_CLICK=True
def draw():
    screen.fill("white")
    map.draw_map()
def on_mouse_down(pos,button):
    """bascule chaque case cliquée"""
    global FIRST_CLICK
    x, y = pos
    abs = x // CELLULE
    ord = y // CELLULE
    if button == mouse.LEFT:
        if FIRST_CLICK==True:
            map.ajout_bombe(abs,ord)
            FIRST_CLICK=False
        elif map.have_been_reset==True:
            map.ajout_bombe(abs,ord)
            map.have_been_reset=False
        map.changer_etat(abs,ord)
    else:
        map.click_droit(abs,ord)

map=Map()
map.creer_map()
pgzrun.go()
