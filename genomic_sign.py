"""
Nom du fichier : genomic_sign.py
Description : Ce fichier contient le code source de l'implémentation de l'algorithme du Chaos Game pour générer une signature d'une séquence d'ADN.
Auteur : Assa DIABIRA & Inès MANOUR
Dernière modification : 22/04/2024
"""

#-----------------------------------------------------------------------------------------------------------------
#                                   Partie 2 : Signature génomique 
#-----------------------------------------------------------------------------------------------------------------

import numpy as np
import sys
import os
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
    coordinates = [(0.5, 0.5)]
    x, y = 0.5, 0.5
    for nucleotide in sequence:
        if nucleotide == 'A':
            x = x / 2
            y = (y + 1) / 2
        elif nucleotide == 'T':
            x = (x + 1) / 2
            y = (y + 1) / 2
        elif nucleotide == 'G':
            x = (x + 1) / 2
            y = y / 2
        elif nucleotide == 'C':
            x = x / 2
            y = y / 2
        coordinates.append((x, y))
    return coordinates

def plot_cgr(coordinates, gbk_file, k):
    n_bins = 2 ** k
    counts = np.zeros((n_bins, n_bins), dtype=int)
    for x, y in coordinates:
        i = int(x * n_bins)
        j = int(y * n_bins)
        if i >= n_bins or j >= n_bins:
            continue
        counts[j, i] += 1
    cgr_text = ""
    for i in range(n_bins - 1, -1, -1):
        for j in range(n_bins):
            cgr_text += str(counts[i, j]) + " "
        cgr_text += "\n"
    cmap = plt.get_cmap('gist_yarg')
    plt.imshow(counts, cmap=cmap, origin='lower')
    fontsize = max(5, 10 - k)
    for i in range(n_bins):
        for j in range(n_bins):
            text_color = 'black' if counts[i, j] < np.max(counts) / 2 else 'white'
            plt.text(j, i, int(counts[i, j]), ha='center', va='center', color=text_color, fontsize=fontsize)
    cbar = plt.colorbar(label='Nombre d\'occurrences', orientation='vertical')
    plt.title("Signature génomique avec {}-mers ({})\n".format(k, gbk_file))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    return cgr_text

def generate_signature_matrix_from_cgr(cgr_text):
    rows = cgr_text.strip().split("\n")
    signature_matrix = np.array([list(map(int, row.split())) for row in rows])
    return signature_matrix

def save_matrix(signature_matrix, filename, gbk_file):
    if os.path.exists(filename):
        print("Attention: Le fichier de sortie existe déjà. Les données seront ajoutées à la fin du fichier existant.")
    with open(filename, 'a') as file:
        file.write("\n----------------------------------------\n")
        file.write("Signature génomique avec des {}-mers (fichier GenBank : {})\n".format(k, gbk_file))
        np.savetxt(file, signature_matrix, fmt='%d')

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
    
    sequence = read_sequence_from_gbk(gbk_file)
    
    if not sequence:
        print("Erreur: Le fichier GenBank est vide ou inaccessible.")
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
    
    cgr_coordinates = generate_cgr_coordinates(sequence)
    plot_text = plot_cgr(cgr_coordinates, gbk_file, k)
    signature_matrix = generate_signature_matrix_from_cgr(plot_text) 
    save_matrix(signature_matrix, output_file, gbk_file)

