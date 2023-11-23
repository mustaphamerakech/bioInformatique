class Node:
    def __init__(self, sequence1, sequence2, score, alignment):
        self.sequence1 = sequence1
        self.sequence2 = sequence2
        self.score = score
        self.alignment = alignment

def simple_scoring(a, b):
    # Simple scoring function: +1 for a match, -1 for a mismatch
    return 1 if a == b else -1

def heuristic(sequence1, sequence2):
    # Heuristic function: count the number of matching positions
    return sum(1 for a, b in zip(sequence1, sequence2) if a == b)

def a_star_sequence_alignment(sequence1, sequence2):
    initial_node = Node(sequence1, sequence2, 0, '')

    # Priority queue to store nodes based on the total cost (score + heuristic)
    open_set = [(0 + heuristic(sequence1, sequence2), initial_node)]

    # Set to store explored nodes
    closed_set = set()

    while open_set:
        # Pop the node with the minimum total cost
        current_node = min(open_set, key=lambda x: x[0])[1]
        open_set.remove((current_node.score + heuristic(sequence1, sequence2), current_node))

        # Check if the sequences are aligned
        if not any('-' in alignment for alignment in [current_node.alignment, current_node.sequence2]):
            print("Alignment Found!")
            print(current_node.alignment)
            return current_node.alignment

        # Explore neighbors
        for i in range(len(sequence1) + 1):
            for j in range(len(sequence2) + 1):
                if i < len(sequence1) and j < len(sequence2):
                    match = simple_scoring(sequence1[i], sequence2[j])
                else:
                    match = 0  # Gap penalty

                new_score = current_node.score + match
                new_alignment = current_node.alignment + ('|' if match == 1 else ' ')

                neighbor = Node(
                    sequence1=current_node.sequence1[i:],
                    sequence2=current_node.sequence2[j:],
                    score=new_score,
                    alignment=new_alignment
                )

                # Check if the neighbor has not been explored
                if neighbor not in closed_set:
                    open_set.append((new_score + heuristic(neighbor.sequence1, neighbor.sequence2), neighbor))

        # Mark the current node as explored
        closed_set.add(current_node)

    print("No alignment found.")
    return None

# Get user input for sequences
sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

# Run the A* sequence alignment
result = a_star_sequence_alignment(sequence1, sequence2)
if result is None:
    print("No alignment found.")
