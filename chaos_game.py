"""
Nom du fichier : chaos_game.py
Description : Ce fichier contient le code source l'implémentation de l'algorithme du Chaos Game pour générer une représentation visuelle d'une séquence d'ADN.
Auteur : Assa DIABIRA & Inès MANOUR
Dernière modification : 17/04/2024
"""

import sys
import numpy as np  # Importation de la bibliothèque NumPy pour le calcul numérique
import matplotlib.pyplot as plt  # Importation de la bibliothèque Matplotlib pour la création de graphiques

# Définition des coordonnées des bases ATCG dans le carré
nucleotide_coords = {
    'A': np.array([0, 0]),  # Coordonnées pour la base A
    'T': np.array([1, 0]),  # Coordonnées pour la base T
    'C': np.array([0, 1]),  # Coordonnées pour la base C
    'G': np.array([1, 1])   # Coordonnées pour la base G
}

def get_dna_sequence_from_genbank(genbank_file: str) -> str:
    """
    Récupère la séquence d'ADN à partir d'un fichier GenBank.

    Paramètres
    ----------
    genbank_file : str
        Chemin vers le fichier GenBank.

    Renvois
    -------
    dna_sequence : str
        Séquence d'ADN extraite du fichier GenBank.
    """
    dna_sequence = ""
    with open(genbank_file, "r") as file:
        for line in file:
            if line.startswith("ORIGIN"):
                break
        for line in file:
            if line.strip().isalpha():
                dna_sequence += line.strip().upper()
            elif line.startswith("//"):
                break
    return dna_sequence

def count_kmers(seq: str, k: int) -> dict:
    """
    Compte le nombre d'occurrences de chaque k-mer dans la séquence.

    Paramètres
    ----------
    seq : str
        Séquence nucléotidique.
    k : int
        Longueur des k-mers à considérer.

    Renvois
    -------
    kmer_count : dict
        Dictionnaire contenant les k-mers comme clés et leur nombre d'occurrences comme valeurs.
    """
    kmer_count = {}  # Initialisation du dictionnaire de comptage des k-mers
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]  # Extraction du k-mer à partir de la séquence
        if "N" not in kmer:  # Ignorer les k-mers contenant des 'N'
            kmer_count[kmer] = kmer_count.get(kmer, 0) + 1  # Incrémentation du compteur du k-mer
    return kmer_count  # Retourne le dictionnaire de comptage des k-mers

def probabilities(kmer_count: dict) -> dict:
    """
    Calcule les probabilités pour chaque k-mer.

    Paramètres
    ----------
    kmer_count : dict
        Dictionnaire contenant les comptes de chaque k-mer.

    Renvois
    -------
    kmer_probs : dict
        Dictionnaire contenant les k-mers comme clés et leur probabilité d'occurrence comme valeurs.
    """
    total_count = sum(kmer_count.values())  # Calcul du nombre total de k-mers
    if total_count == 0:
        return {}  # Éviter la division par zéro
    return {kmer: count / total_count for kmer, count in kmer_count.items()}  # Calcul des probabilités

def generate_chaos_game_representation(seq: str, size: int) -> np.ndarray:
    """
    Génère une représentation du Chaos Game à partir d'une séquence d'ADN.

    Paramètres
    ----------
    seq : str
        Séquence d'ADN à partir de laquelle générer la représentation du Chaos Game.
    size : int
        Taille de l'image de sortie (en pixels).

    Renvois
    -------
    chaos_game_representation : np.ndarray
        Matrice représentant le Chaos Game.
    """
    # Initialisation de la matrice de représentation
    chaos_game_representation = np.zeros((size, size))  # Création d'une matrice de zéros
    
    # Division de l'image en sections
    section_size = size // 2  # Taille de chaque section
    
    # Parcours de la séquence pour générer les points
    for nucleotide in seq:
        # Calcul des coordonnées du prochain point
        next_position = nucleotide_coords.get(nucleotide, np.array([0, 0]))  # Utilisation de get pour gérer les nucléotides inconnus
        
        # Redimensionnement des coordonnées pour qu'elles s'inscrivent dans les limites de l'image
        x = min(int(next_position[0] * section_size), section_size - 1)  # Coordonnée x avec une limite de taille
        y = min(int(next_position[1] * section_size), section_size - 1)  # Coordonnée y avec une limite de taille
        
        # Attribution du nucléotide à la section correspondante
        chaos_game_representation[y, x] += 1  # Incrémentation du compteur du nucléotide

    # Affichage de la matrice du Chaos Game (pour le débogage)
    print("Matrice du Chaos Game :")
    print(chaos_game_representation)
    

    # Affichage de la matrice avec Matplotlib
    plt.imshow(chaos_game_representation, cmap='hot', origin='upper')
    plt.title("Représentation du Chaos Game")
    plt.colorbar()
    plt.show()
    
    return chaos_game_representation  # Retourne la matrice représentant le Chaos Game

# Exemple d'utilisation
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python chaos_game.py <genbank_file>")
        sys.exit(1)
    genbank_file = sys.argv[1]
    dna_sequence = get_dna_sequence_from_genbank(genbank_file)
    kmer_length = 3  # Longueur des k-mers à considérer
    image_size = 1000  # Taille de l'image de sortie en pixels
    
    kmer_counts = count_kmers(dna_sequence, kmer_length)  # Comptage des k-mers dans la séquence
    kmer_probs = probabilities(kmer_counts)  # Calcul des probabilités des k-mers
    chaos_game_matrix = generate_chaos_game_representation(dna_sequence, image_size)  # Génération de la représentation du Chaos Game
