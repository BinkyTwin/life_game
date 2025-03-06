decalages = [
        (-1, -1), (-1, 0), (-1, 1),  # Voisins au-dessus
        (0, -1),         (0, 1),    # Voisins à gauche et à droite
        (1, -1), (1, 0), (1, 1)     # Voisins en dessous
          ]
for fx, fy in decalages: 
    print(fx, fy)