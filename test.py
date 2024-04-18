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

