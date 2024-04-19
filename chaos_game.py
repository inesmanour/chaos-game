"""
Nom du fichier : chaos_game.py
Description : Ce fichier contient le code source de l'implémentation de l'algorithme du Chaos Game pour générer une représentation visuelle d'une séquence d'ADN.
Auteur : Assa DIABIRA & Inès MANOUR
Dernière modification : 18/04/2024
"""

#-----------------------------------------------------------------------------------------------------------------
#                                   Partie 1 : Représentation CGR Simple
#-----------------------------------------------------------------------------------------------------------------

import numpy as np # Importation de la bibliothèque numpy pour le calcul numérique
import sys # Importation pour la mise en argument des fichiers
import matplotlib.pyplot as plt # Importation de la bibliothèque matplotlib pour les graphiques

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

def generate_cgr_coordinates(sequence, k):
    """
    Génère les coordonnées pour chaque k-mer dans l'espace du Chaos Game.

    Paramètres
    ----------
    sequence : str
        Séquence d'ADN.
    k : int
        Taille des k-mers.

    Renvois
    -------
    coordinates : list
        Liste des coordonnées (x, y) pour chaque k-mer.
    """
    coordinates = [(0.5, 0.5)]  # Définition du début au centre du carré
    x, y = 0.5, 0.5
    
    # Définir les coordonnées des nucléotides
    nucleotide_coordinates = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}

    # Générer les k-mers et calculer les coordonnées pour chaque nucléotide
    kmers = generate_kmers(sequence, k)
    for kmer in kmers:
        for nucleotide in kmer:
            nx, ny = nucleotide_coordinates[nucleotide]
            x = (x + nx) / 2
            y = (y + ny) / 2
            coordinates.append((x, y))
    
    return coordinates

def plot_cgr(coordinates, filename, k):
    """
    Représente graphiquement les coordonnées dans l'espace du Chaos Game.

    Paramètres
    ----------
    coordinates : list
        Liste des coordonnées (x, y) des nucléotides.
    filename : str
        Nom du fichier GenBank.
    k : int
        Taille des k-mers.

    Renvois
    -------
    None
    """
    x, y = zip(*coordinates)
    plt.scatter(x, y, c=range(len(x)), cmap='gray', s=0.2)  # Modifier le paramètre s ici pour ajuster la taille des points
    
    # Ajouter les bases à côté du carré en fonction de leurs coordonnées
    nucleotide_positions = {'A': (0, 1), 'T': (1, 1), 'G': (1, 0), 'C': (0, 0)}
    for nucleotide, (nx, ny) in nucleotide_positions.items():
        plt.text(nx, ny, nucleotide, fontsize=12, ha='left', va='center_baseline')
    
    
    plt.title("Représentation CGR de {} avec {} kmer(s)".format(filename, k))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([])  # Supprimer les graduations de l'axe x
    plt.yticks([])  # Supprimer les graduations de l'axe y
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Erreur: Nombre incorrect d'arguments.")
        print("Usage: python chaos_game.py <fichier_genbank> <k>")
        sys.exit(1)
    
    gbk_file = sys.argv[1]
    k = sys.argv[2]
    
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
    
    cgr_coordinates = generate_cgr_coordinates(sequence, k)
    plot_cgr(cgr_coordinates, gbk_file, k)
#-----------------------------------------------------------------------------------------------------------------
#                                   Partie 2 : Représentation FCGR with count matrix
#-----------------------------------------------------------------------------------------------------------------
