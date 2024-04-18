"""
import sys
import numpy as np
import matplotlib.pyplot as plt

def read_sequence_from_gbk(gbk_file):
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
    coordinates = [(0.5, 0.5)]  # Commencer au centre du carré
    x, y = 0.5, 0.5
    
    nucleotide_coordinates = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}

    for nucleotide in sequence:
        nx, ny = nucleotide_coordinates.get(nucleotide, (0.5, 0.5))
        x = (x + nx) / 2
        y = (y + ny) / 2
        coordinates.append((x, y))
    
    return coordinates

def graph(chaos_kx, kmerSize):
    plt.figure(1)
    plt.title('Chaos game representation for {}-mers'.format(kmerSize))
    plt.imshow(chaos_kx, interpolation='nearest', origin="lower", cmap='gray')
    # plt.axis("off")
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python chaos_game.py <gbk_file>")
        sys.exit(1)
    
    gbk_file = sys.argv[1]
    sequence = read_sequence_from_gbk(gbk_file)
    cgr_coordinates = generate_cgr_coordinates(sequence)
    # Création de la matrice du Chaos Game (pour cet exemple, une matrice aléatoire est utilisée)
    cgr_matrix = np.random.randint(0, 10, (100, 100))  # Exemple de matrice aléatoire de taille 100x100
    graph(cgr_matrix, 10)  # Appel de la fonction graph avec la matrice et la taille des k-mers
"""
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_cgr_coordinates(sequence):
    coordinates = [(0.5, 0.5)]  # Commencer au centre du carré
    x, y = 0.5, 0.5
    
    nucleotide_coordinates = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}

    for nucleotide in sequence:
        nx, ny = nucleotide_coordinates[nucleotide]
        x = (x + nx) / 2
        y = (y + ny) / 2
        coordinates.append((x, y))
    
    return coordinates

def plot_cgr(coordinates):
    x, y = zip(*coordinates)
    plt.plot(x, y, 'k-', linewidth=0.5)
    plt.scatter(x, y, c=range(len(x)), cmap='viridis', s=20)  # Modifiez le paramètre s ici pour rendre les points plus gros
    
    # Ajouter les bases à côté du carré en fonction de leurs coordonnées
    nucleotide_positions = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}
    for nucleotide, (nx, ny) in nucleotide_positions.items():
        plt.text(nx, ny, nucleotide, fontsize=12, ha='left', va='baseline')
    
    plt.title("Représentation du Chaos Game")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([])  # Supprimer les graduations de l'axe x
    plt.yticks([])  # Supprimer les graduations de l'axe y
    plt.show()

def generate_cgr_matrix(coordinates, size=1000):
    cgr_matrix = np.zeros((size, size), dtype=np.int32)

    for x, y in coordinates:
        x_index = int(x * size)
        y_index = int(y * size)
        cgr_matrix[y_index, x_index] += 1
    
    return cgr_matrix

# Test avec une séquence d'ADN factice
sequence = "ATGG"
cgr_coordinates = generate_cgr_coordinates(sequence)
plot_cgr(cgr_coordinates)
cgr_matrix = generate_cgr_matrix(cgr_coordinates)
print("Matrice du Chaos Game :")
print(cgr_matrix)
"""
"""
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
    coordinates = [(0.5, 0.5)]  # Commencer au centre du carré
    x, y = 0.5, 0.5
    
    nucleotide_coordinates = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}

    for nucleotide in sequence:
        nx, ny = nucleotide_coordinates[nucleotide]
        x = (x + nx) / 2
        y = (y + ny) / 2
        coordinates.append((x, y))
    
    return coordinates

def plot_cgr(coordinates):
    x, y = zip(*coordinates)
    plt.scatter(x, y, c=range(len(x)), cmap='gray', s=1)  # Modifiez le paramètre s ici pour rendre les points plus gros
    
    # Ajouter les bases à côté du carré en fonction de leurs coordonnées
    nucleotide_positions = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}
    for nucleotide, (nx, ny) in nucleotide_positions.items():
        plt.text(nx, ny, nucleotide, fontsize=12, ha='right', va='baseline')
    
    plt.title("Représentation du Chaos Game")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([])  # Supprimer les graduations de l'axe x
    plt.yticks([])  # Supprimer les graduations de l'axe y
    plt.show()

def generate_cgr_matrix(coordinates, size=1000):
    cgr_matrix = np.zeros((size, size), dtype=np.int32)

    for x, y in coordinates:
        x_index = int(x * size)
        y_index = int(y * size)
        cgr_matrix[y_index, x_index] += 1
    
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

"""

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

def generate_kmers(sequence, k):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmers.append(sequence[i:i + k])
    return kmers

def generate_cgr_coordinates(sequence, k):
    coordinates = [(0.5, 0.5)]  # Commencer au centre du carré
    x, y = 0.5, 0.5
    
    nucleotide_coordinates = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}

    kmers = generate_kmers(sequence, k)
    for kmer in kmers:
        for nucleotide in kmer:
            nx, ny = nucleotide_coordinates[nucleotide]
            x = (x + nx) / 2
            y = (y + ny) / 2
            coordinates.append((x, y))
    
    return coordinates

def plot_cgr(coordinates):
    x, y = zip(*coordinates)
    plt.scatter(x, y, c=range(len(x)), cmap='gray', s=1)  # Modifiez le paramètre s ici pour rendre les points plus gros
    
    # Ajouter les bases à côté du carré en fonction de leurs coordonnées
    nucleotide_positions = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}
    for nucleotide, (nx, ny) in nucleotide_positions.items():
        plt.text(nx, ny, nucleotide, fontsize=12, ha='right', va='baseline')
    
    plt.title("Représentation du Chaos Game")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([])  # Supprimer les graduations de l'axe x
    plt.yticks([])  # Supprimer les graduations de l'axe y
    plt.show()

def generate_cgr_matrix(coordinates, size=1000):
    cgr_matrix = np.zeros((size, size), dtype=np.int32)

    for x, y in coordinates:
        x_index = int(x * size)
        y_index = int(y * size)
        cgr_matrix[y_index, x_index] += 1
    
    return cgr_matrix

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python chaos_game.py <gbk_file> <k>")
        sys.exit(1)
    
    gbk_file = sys.argv[1]
    k = int(sys.argv[2])
    
    sequence = read_sequence_from_gbk(gbk_file)
    
    if not sequence:
        print("La séquence extraite du fichier est vide.")
        sys.exit(1)
    
    cgr_coordinates = generate_cgr_coordinates(sequence, k)
    plot_cgr(cgr_coordinates)
    
    cgr_matrix = generate_cgr_matrix(cgr_coordinates)
    print("Matrice du Chaos Game :")
    print(cgr_matrix)
