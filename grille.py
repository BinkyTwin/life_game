from cellule import Cellule

class Grille:
    def __init__(self, taille):
        self.taille = taille
        self.grille = []  # initialisation de l'attribut grille
        self.creer()      # appel automatique à la création de la grille
        self.cellules_vivantes = []
    def creer(self):
        for i in range(self.taille): 
            ligne = []
            for j in range(self.taille): 
                ligne.append(Cellule(i,j))

            self.grille.append(ligne)
        return self.grille
    
    def afficher(self):
        for ligne in self.grille:
            print(" ".join(str(cellule) for cellule in ligne))

    def find_cellule_vivante(self):
        self.cellules_vivantes = []  # Remet la liste à zéro avant de la remplir
        for chaque_ligne in self.grille:
            for cellule in chaque_ligne:
                if cellule.etat:
                    self.cellules_vivantes.append((cellule.x, cellule.y))  # Stocke les coordonnées des cellules vivantes
        return self.cellules_vivantes

   