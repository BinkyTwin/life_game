
class Cellule: 
    #Permet de creer une cellule
    def __init__(self,x,y,etat=False):
        self.x = x
        self.y = y
        self.etat = etat

    #Permet de changer l'etat de la cellule
    def change_etat(self):
        self.etat = not self.etat

    #Permet de donner l'etat de la cellule
    def etat(self):
        return self.etat
    #Permet de donner la position de la cellule
    def position(self):
        return self.x,self.y
