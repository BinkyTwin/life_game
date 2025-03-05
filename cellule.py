class Cellule: 
    #Permet de creer une cellule
    def __init__(self,x,y,etat=False):
        self.x = x
        self.y = y
        self.etat = etat
        self.compteur_voisin = 0
    
    def __str__(self):
        return "1" if self.etat else "."

    #Permet de changer l'etat de la cellule
    def change_etat(self):
        self.etat = not self.etat

    #Permet de donner l'etat de la cellule
    def get_etat(self):
        return self.etat
    #Permet de donner la position de la cellule
    def position(self):
        return self.x,self.y

    def verification_voisinage(self,grille):
        self.compteur_voisin = 0
        decalages = [
                    (-1, -1), (-1, 0), (-1, 1),  # Voisins au-dessus
                    (0, -1),         (0, 1),    # Voisins à gauche et à droite
                    (1, -1), (1, 0), (1, 1)     # Voisins en dessous
                    ]
        for dx,dy in decalages: 
            voisin_x = self.x + dx
            voisin_y = self.y + dy
            if 0 <= voisin_x < len(grille) and 0 <= voisin_y < len(grille[0]):
                if grille[voisin_x][voisin_y].etat:
                    self.compteur_voisin += 1
                    
        return self.compteur_voisin
    