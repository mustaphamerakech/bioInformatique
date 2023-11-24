class DNASequenceSet:
    def __init__(self, sequences):
        self.sequences = sequences

def motif_score(motif, sequence):
    # Scoring function for motif matching
    # Example: +1 for a match, -1 for a mismatch
    return sum(1 if sequence[i:i+len(motif)] == motif else -1 for i in range(len(sequence) - len(motif) + 1))

def conserved_motif_score(motif, sequence_set):
    # Calculate the score of the motif based on the scoring function across all sequences
    return sum(motif_score(motif, sequence) for sequence in sequence_set.sequences)

def hill_climbing_motif_finding(initial_motif, sequence_set):
    current_motif = initial_motif
    current_score = conserved_motif_score(current_motif, sequence_set)

    while True:
        neighbors = generate_neighboring_motifs(current_motif)
        best_neighbor = max(neighbors, key=lambda x: conserved_motif_score(x, sequence_set))

        if conserved_motif_score(best_neighbor, sequence_set) <= current_score:
            break  # If no improvement, terminate the search
        else:
            current_motif = best_neighbor
            current_score = conserved_motif_score(current_motif, sequence_set)

    return current_motif

def generate_neighboring_motifs(motif):
    # Generate neighboring motifs by modifying positions and lengths
    # (This is a simplified example, and a more sophisticated approach is typically used)
    neighbors = []

    # Shift the motif position
    for i in range(len(motif)):
        shifted_motif = motif[i:] + motif[:i]
        neighbors.append(shifted_motif)

    # Extend or shorten the motif length
    for i in range(len(motif) - 1):
        extended_motif = motif[:i + 1] + motif[i + 1] * (len(motif) - i - 1)
        neighbors.append(extended_motif)

    return neighbors

# User input for DNA sequences
num_sequences = int(input("Enter the number of DNA sequences: "))
sequences = [input(f"Enter DNA sequence {i + 1}: ").upper() for i in range(num_sequences)]

# User input for initial motif
initial_motif = input("Enter the initial motif: ").upper()

sequence_set = DNASequenceSet(sequences)

final_motif = hill_climbing_motif_finding(initial_motif, sequence_set)
print("\nFinal Conserved Motif:")
print("Motif:", final_motif)
print("Motif Score:", conserved_motif_score(final_motif, sequence_set))
