import numpy as np
import matplotlib.pyplot as plt

def create_cgr_image(sequence):
    # Créer une grille vide pour l'image CGR
    cgr_image = np.zeros((len(sequence), len(sequence)))
    
    # Fonction récursive pour attribuer les coordonnées à chaque mot
    def assign_coordinates(subsequence, x, y, step):
        if step == len(subsequence):
            # Attribuer les coordonnées au mot dans l'image CGR
            cgr_image[x][y] += 1
        else:
            # Diviser le quadrant en quatre sous-quadrants
            if subsequence[step] == 'A':
                assign_coordinates(subsequence, x + step, y + step, step + 1)
            elif subsequence[step] == 'C':
                assign_coordinates(subsequence, x + step, y - step, step + 1)
            elif subsequence[step] == 'G':
                assign_coordinates(subsequence, x - step, y + step, step + 1)
            elif subsequence[step] == 'T':
                assign_coordinates(subsequence, x - step, y - step, step + 1)
    
    # Appliquer la fonction récursive à chaque mot dans la séquence
    for i in range(len(sequence)):
        assign_coordinates(sequence[i:], len(sequence)//2, len(sequence)//2, 0)
    
    return cgr_image

# Exemple d'utilisation
sequence = "ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG"
cgr_image = create_cgr_image(sequence)

# Afficher l'image CGR
plt.imshow(cgr_image, cmap='gray', interpolation='nearest')
plt.title("Chaos Game Representation (CGR)")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.colorbar(label="Frequency")
plt.show()
