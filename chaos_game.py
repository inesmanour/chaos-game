import numpy as np
import matplotlib.pyplot as plt

# Définition des coordonnées des nucléotides
nucleotide_coords = {
    'A': np.array([0, 0]),
    'T': np.array([1, 0]),
    'C': np.array([0, 1]),
    'G': np.array([1, 1])
}

def count_kmers(sequence, k):
    """
    Compte le nombre d'occurrences de chaque k-mer dans la séquence.
    """
    kmer_count = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if "N" not in kmer:  # Ignorer les k-mers contenant des 'N'
            kmer_count[kmer] = kmer_count.get(kmer, 0) + 1
    return kmer_count

def probabilities(kmer_count):
    """
    Calcule les probabilités pour chaque k-mer.
    """
    total_count = sum(kmer_count.values())
    if total_count == 0:
        return {}  # Éviter la division par zéro
    return {kmer: count / total_count for kmer, count in kmer_count.items()}

def generate_chaos_game_representation(sequence, size):
    """
    Génère une représentation du Chaos Game à partir d'une séquence d'ADN.

    :param sequence: Séquence d'ADN
    :param size: Taille de l'image de sortie (en pixels)
    :return: Matrice représentant le Chaos Game
    """
    # Initialisation de la matrice de représentation
    chaos_game_representation = np.zeros((size, size))
    
    # Division de l'image en sections
    section_size = size // 2
    
    # Parcours de la séquence pour générer les points
    for nucleotide in sequence:
        # Calcul des coordonnées du prochain point
        next_position = nucleotide_coords.get(nucleotide, np.array([0, 0]))  # Utilisation de get pour gérer les nucléotides inconnus
        
        # Redimensionnement des coordonnées pour qu'elles s'inscrivent dans les limites de l'image
        x = min(int(next_position[0] * section_size), section_size - 1)
        y = min(int(next_position[1] * section_size), section_size - 1)
        
        # Attribution du nucléotide à la section correspondante
        chaos_game_representation[y, x] += 1
    
    # Affichage de la matrice du Chaos Game
    plt.imshow(chaos_game_representation, cmap='hot', origin='upper')
    plt.title("Représentation du Chaos Game")
    plt.colorbar()
    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    dna_sequence = "ATCGATCGATCG"
    kmer_length = 3
    image_size = 1000
    
    kmer_counts = count_kmers(dna_sequence, kmer_length)
    kmer_probs = probabilities(kmer_counts)
    chaos_game_matrix = generate_chaos_game_representation(dna_sequence, image_size)
