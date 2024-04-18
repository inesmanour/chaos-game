import numpy as np

def generate_genomic_signature(sequence, word_length):
    signature = {}

    for i in range(len(sequence) - word_length + 1):
        word = sequence[i:i + word_length]
        if word not in signature:
            signature[word] = 0
        signature[word] += 1
    
    return signature

# Test avec une séquence d'ADN factice et une longueur de mot de 2 lettres
sequence = "ATGCTAAGCTAGCTAGCT"
word_length = 2
genomic_signature = generate_genomic_signature(sequence, word_length)
print(genomic_signature)
