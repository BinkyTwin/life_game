from grille import Grille
from cellule import Cellule
import time

jeu = Grille(16)  # On crée une grille de 16x16 cellules

game = True

def regle_du_jeu(grille):
        nouvelle_grille = [[Cellule(x, y, grille.grille[x][y].etat) for y in range(grille.taille)] for x in range(grille.taille)]

        for x in range(grille.taille):
            for y in range(grille.taille):
                cellule = grille.grille[x][y]
                voisins = cellule.verification_voisinage(grille)  # On compte les voisins vivants

                if cellule.etat == 1:  # Si la cellule est vivante
                    if voisins < 2 or voisins > 3:
                        nouvelle_grille[x][y].etat = 0  # Elle meurt
                else:  # Si la cellule est morte
                    if voisins == 3:
                        nouvelle_grille[x][y].etat = 1  # Elle devient vivante

        grille.grille = nouvelle_grille  # Mettre à jour la grille avec la nouvelle génération


while game:
    jeu.afficher()  # Affichage de la grille
    regle_du_jeu(jeu)  # On applique les règles pour générer la nouvelle grille
    time.sleep(1)  # Pause de 1 seconde pour mieux voir l’évolution
