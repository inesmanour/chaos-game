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
import matplotlib.pyplot as plt
import sys
import os

def read_sequence_from_gbk(gbk_file):
    """
    Lecture du fichier GenBank et extraction de la séquence d'ADN.

    Paramètres
    ----------
    gbk_file : str
        Chemin vers le fichier GenBank.

    Renvois
    -------
    sequence : str
        Séquence d'ADN extraite du fichier GenBank.
    """
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
    """
    Génère tous les k-mers possibles à partir d'une séquence d'ADN.

    Paramètres
    ----------
    sequence : str
        Séquence d'ADN.
    k : int
        Taille des k-mers.

    Renvois
    -------
    kmers : list
        Liste des k-mers de taille k.
    """
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmers.append(sequence[i:i + k])
    return kmers

def generate_signature_matrix(kmers):
    """
    Génère une matrice de signature génomique à partir de la liste de k-mers.

    Paramètres
    ----------
    kmers : list
        Liste des k-mers.

    Renvois
    -------
    signature_matrix : numpy.array
        Matrice de signature génomique.
    """
    bases = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    signature_matrix = np.zeros((4, 4), dtype=np.int64)
    
    for kmer in kmers:
        for i in range(len(kmer) - 1):
            current_base = kmer[i]
            next_base = kmer[i + 1]
            signature_matrix[bases[current_base], bases[next_base]] += 1
    
    return signature_matrix

def plot_signature_matrix(signature_matrix, k):
    """
    Représente graphiquement la matrice de signature génomique.

    Paramètres
    ----------
    signature_matrix : numpy.array
        Matrice de signature génomique.
    k : int
        Taille des mots.

    Renvois
    -------
    None
    """
    plt.imshow(signature_matrix, cmap='gray', interpolation='nearest')

    for i in range(signature_matrix.shape[0]):
        for j in range(signature_matrix.shape[1]):
            plt.text(j, i, str(signature_matrix[i, j]), ha='center', va='center', color='blue')

    plt.title("Signature génomique ({}-mers)".format(k))
    plt.xlabel("Nucleotide suivant")
    plt.ylabel("Nucleotide actuel")
    plt.colorbar(label="Effectif")
    plt.xticks(np.arange(4), ['A', 'C', 'G', 'T'])
    plt.yticks(np.arange(4), ['A', 'C', 'G', 'T'])
    plt.show()

def save_matrix(matrix, filename, kmers, gbk_file):
    """
    Sauvegarde la matrice dans un fichier texte avec une indication sur les k-mers.

    Paramètres
    ----------
    matrix : numpy.array
        Matrice à sauvegarder.
    filename : str
        Chemin vers le fichier de sortie.
    kmers : list
        Liste des k-mers considérés.
    gbk_file : str
        Nom du fichier GenBank d'origine.

    Renvois
    -------
    None
    """
    if os.path.exists(output_file):
        print("Attention: Le fichier de sortie existe déjà. Les données seront ajoutées à la fin du fichier existant.")

    mode = 'a' if os.path.exists(filename) else 'w'
    with open(filename, mode) as file:
            file.write("\n----------------------------------------\n")
            file.write("Signature génomique avec des {}-mers (fichier GenBank : {})\n".format(len(kmers[0]), gbk_file))
            np.savetxt(file, matrix, fmt='%d')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Erreur: Nombre incorrect d'arguments.")
        print("Usage: python {} <fichier_genbank> <k> <fichier_sortie>".format(sys.argv[0]))
        sys.exit(1)
 
    gbk_file = sys.argv[1]
    print("Lecture du fichier GenBank : {}".format(gbk_file))

    k = sys.argv[2]
    output_file = sys.argv[3]
    
    if not gbk_file:
        print("Erreur: Veuillez spécifier le fichier GenBank en tant qu'argument.")
        sys.exit(1)
    
    if not k:
        print("Erreur: Veuillez spécifier la taille des k-mers en tant qu'argument.")
        sys.exit(1)
    
    try:
        k = int(k)
        if k <= 0:
            raise ValueError("La taille des k-mers doit être un entier positif.")
    except ValueError as e:
        print("Erreur de format: La taille des k-mers doit être un entier positif.")
        sys.exit(1)
    
    sequence = read_sequence_from_gbk(gbk_file)
    
    if not sequence:
        print("Erreur: Le fichier GenBank est vide ou inaccessible.")
        sys.exit(1)

    kmers = generate_kmers(sequence, k)
    signature_matrix = generate_signature_matrix(kmers)
    plot_signature_matrix(signature_matrix, k)
    save_matrix(signature_matrix, output_file, kmers, gbk_file)
