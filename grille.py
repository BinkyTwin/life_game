import cellule 

class Grille:
    def __init__(self, taille):
        self.taille = taille
        self.grille = []  # initialisation de l'attribut grille
        self.creer()      # appel automatique à la création de la grille

    def creer(self):
        for i in range(self.taille): 
            ligne = []
            for j in range(self.taille): 
                ligne.append(cellule.Cellule(i,j))
            self.grille.append(ligne)
        return self.grille
    
    def afficher(self):
        print(self.grille)

