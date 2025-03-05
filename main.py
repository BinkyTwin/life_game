from grille import Grille

g = Grille(5)  # Création d'une grille 5x5

# On active manuellement quelques cellules vivantes pour tester
g.grille[1][1].change_etat()
g.grille[2][2].change_etat()
g.grille[3][3].change_etat()

# Vérification des cellules vivantes
print("Cellules vivantes :", g.find_cellule_vivante())

# Vérification du voisinage d'une cellule
cellule_test = g.grille[2][2]  # Sélectionne une cellule
voisins_vivants = cellule_test.verification_voisinage(g.grille)
print(f"La cellule ({cellule_test.x}, {cellule_test.y}) a {voisins_vivants} voisins vivants.")
