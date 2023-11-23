class Node:
    def __init__(self, motif, sequences):
        self.motif = motif
        self.sequences = sequences

def motif_score(motif, sequence):
    # Simple scoring function: count the number of matching positions
    return sum(1 for a, b in zip(motif, sequence) if a == b)

def best_first_search_motif_finding(sequences, motif_length):
    initial_node = Node('', sequences)

    # Priority queue to store nodes based on motif score
    open_set = [(0, initial_node)]

    while open_set:
        current_score, current_node = max(open_set, key=lambda x: x[0])
        open_set.remove((current_score, current_node))

        # Check if the motif has the desired length
        if len(current_node.motif) == motif_length:
            print("Motif Found:", current_node.motif)
            return current_node.motif

        # Explore neighbors
        for i in range(len(sequences[0]) - motif_length + 1):
            candidate_motif = sequences[0][i:i + motif_length]
            
            new_sequences = [sequence.replace(candidate_motif, '') for sequence in current_node.sequences]
            new_score = current_score + sum(motif_score(candidate_motif, sequence) for sequence in sequences)

            new_node = Node(candidate_motif, new_sequences)
            priority = new_score

            # Check if the neighbor has not been explored
            if candidate_motif not in current_node.motif:
                open_set.append((priority, new_node))

    print("No motif found.")
    return None

# Get user input for sequences
num_sequences = int(input("Enter the number of sequences: "))
sequences = []
for _ in range(num_sequences):
    sequence = input("Enter a DNA sequence: ")
    sequences.append(sequence)

# Get user input for motif length
motif_length = int(input("Enter the motif length: "))

# Run the Best-First Search for motif finding
result = best_first_search_motif_finding(sequences, motif_length)
if result is None:
    print("No motif found.")
