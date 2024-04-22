"""
Nom du fichier : clustering.py
Description : Ce fichier contient le code source de l'implémentation d'un clustering hiérarchique basé sur la signature génomique d'une séquence. Il génère le dendrogramme correspondant.
Auteur : Assa DIABIRA & Inès MANOUR
Dernière modification : 22/04/2024
"""

#-----------------------------------------------------------------------------------------------------------------
#                                   Partie 3 :  Classification hiérarchique
#-----------------------------------------------------------------------------------------------------------------

import numpy as np
import sys
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import os

def read_sequence_from_gbk(gbk_file):
    """
    Lecture du fichier GenBank et extraction de la séquence d'ADN.
    """
    sequence = ""
    with open(gbk_file, "r") as file:
        for line in file:
            if line.startswith("ORIGIN"):
                break
        for line in file:
            if line.startswith("//"):
                break
            filtered_line = ''.join(filter(str.isalpha, line.strip().upper()))
            sequence += ''.join(filter(lambda base: base in ['A', 'C', 'G', 'T'], filtered_line))
    return sequence

def generate_signature_matrix(sequence, k):
    """
    Génère une matrice de signature génomique à partir de la séquence d'ADN.
    """
    kmers = [sequence[i:i + k] for i in range(len(sequence) - k + 1)]
    signature_matrix = np.zeros((4, 4), dtype=np.int64)
    bases = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    for kmer in kmers:
        for i in range(len(kmer) - 1):
            current_base = kmer[i]
            next_base = kmer[i + 1]
            signature_matrix[bases[current_base], bases[next_base]] += 1
    return signature_matrix

def calculate_similarity_matrix(signature_matrices):
    """
    Calcule une matrice de similarité entre les séquences d'ADN à partir de leurs signatures génomiques.
    """
    n = len(signature_matrices)
    similarity_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            similarity_matrix[i, j] = calculate_similarity(signature_matrices[i], signature_matrices[j])
    return similarity_matrix

def calculate_similarity(matrix1, matrix2):
    """
    Calcule la similarité entre deux matrices de signature génomique.
    """
    similarity = np.corrcoef(matrix1.flatten(), matrix2.flatten())[0, 1]
    return similarity

def hierarchical_clustering(similarity_matrix, gbk_files):
    """
    Effectue le clustering hiérarchique à partir de la matrice de similarité et affiche le dendrogramme.
    """
    linkage_matrix = linkage(similarity_matrix, method='average')
    plt.figure(figsize=(10, 8))

    # print("Dimensions de la matrice de liaison:", linkage_matrix.shape) vérifications

    dendrogram(linkage_matrix, labels=gbk_files, leaf_rotation=90)
    plt.title('Dendrogramme de la Classification hiérachique')
    plt.xlabel('Séquences GenBank testées')
    plt.ylabel('Similarité')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    directory = sys.argv[1]
    k = 5
    signature_matrices = []
    gbk_files = []
    for file in os.listdir(directory):
        if file.endswith(".gbk"):
            gbk_files.append(file)
            sequence = read_sequence_from_gbk(os.path.join(directory, file))
            if sequence:
                signature_matrix = generate_signature_matrix(sequence, k)
                signature_matrices.append(signature_matrix)
            else:
                print("Impossible de générer une séquence à partir du fichier:", file)


    print("Nombre de fichiers GenBank trouvés:", len(gbk_files))
    print("Nombre de matrices de signature génomique générées:", len(signature_matrices))

    similarity_matrix = calculate_similarity_matrix(signature_matrices)
    hierarchical_clustering(similarity_matrix, gbk_files)
