import numpy as np
import sys
import matplotlib.pyplot as plt

def read_sequence_from_gbk(gbk_file):
    print("Lecture du fichier GenBank : {}".format(gbk_file))
    sequence = ""
    with open(gbk_file, "r") as file:
        for line in file:
            if line.startswith("ORIGIN"):
                break
        for line in file:
            if line.startswith("//"):
                break
            sequence += ''.join(filter(str.isalpha, line.strip().upper()))
    return sequence

def generate_cgr_coordinates(sequence):
    print("Génération des coordonnées du Chaos Game...")
    coordinates = [(0.5, 0.5)]  # Commencer au centre du carré
    x, y = 0.5, 0.5
    
    nucleotide_coordinates = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}

    for nucleotide in sequence:
        nx, ny = nucleotide_coordinates.get(nucleotide, (0.5, 0.5))  # Gestion des nucléotides inconnus
        x = (x + nx) / 2
        y = (y + ny) / 2
        # Correction pour éviter les coordonnées en dehors des limites de la matrice
        x = min(max(x, 0), 1)
        y = min(max(y, 0), 1)
        coordinates.append((x, y))
        # Vérifier si les coordonnées sont déjà présentes
        if (x, y) in coordinates[:-1]:
            print("Coordonnées déjà présentes : ({}, {})".format(x, y))
            break
    
    print("Coordonnées générées avec succès.")
    return coordinates

def plot_cgr(coordinates, size=1000):
    print("Affichage de la représentation du Chaos Game...")
    if not coordinates:
        print("Aucune coordonnée générée.")
        return
    
    x, y = zip(*coordinates)
    plt.scatter(x, y, c=range(len(x)), cmap='viridis', s=5, marker='s')
    plt.title("Représentation du Chaos Game")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    print("Affichage terminé.")

def generate_cgr_matrix(coordinates, size=1000):
    print("Génération de la matrice du Chaos Game...")
    cgr_matrix = np.zeros((size, size), dtype=np.int32)

    for x, y in coordinates:
        x_index = int(x * size)
        y_index = int(y * size)
        if 0 <= x_index < size and 0 <= y_index < size:
            cgr_matrix[y_index, x_index] += 1
        else:
            print("Coordonnées en dehors des limites de la matrice : ({}, {})".format(x_index, y_index))
    
    print("Matrice du Chaos Game générée avec succès.")
    return cgr_matrix


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python chaos_game.py <gbk_file>")
        sys.exit(1)
    
    gbk_file = sys.argv[1]
    sequence = read_sequence_from_gbk(gbk_file)
    
    if not sequence:
        print("La séquence extraite du fichier est vide.")
        sys.exit(1)
    
    cgr_coordinates = generate_cgr_coordinates(sequence)
    plot_cgr(cgr_coordinates)
    
    cgr_matrix = generate_cgr_matrix(cgr_coordinates)
    print("Matrice du Chaos Game :")
    print(cgr_matrix)
