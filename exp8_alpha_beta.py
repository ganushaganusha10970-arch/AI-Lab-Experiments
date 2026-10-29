
# Experiment 8: Implementing Alpha-Beta Pruning

tree = {
    "A": ["B", "C", "D"],
    "B": ["E", "F", "G"],
    "C": ["H", "I", "J"],
    "D": ["K", "L", "M"],
    "E": [3, 5],
    "F": [6, 9],
    "G": [1, 2],
    "H": [4, 6],
    "I": [7, 8],
    "J": [9, 10],
    "K": [1, 3],
    "L": [12, 14],
    "M": [15, 18]
}

nodes_evaluated = 0
terminal_values_evaluated = 0
branches_pruned = 0
root_moves = {}


def alpha_beta(node, maximizing, alpha, beta):
    global nodes_evaluated
    global terminal_values_evaluated
    global branches_pruned

    nodes_evaluated += 1

    # Terminal utility value
    if isinstance(node, int):
        terminal_values_evaluated += 1
        return node

    children = tree[node]

    if maximizing:
        value = float("-inf")

        for i, child in enumerate(children):
            child_value = alpha_beta(child, False, alpha, beta)

            if node == "A":
                root_moves[child] = child_value

            value = max(value, child_value)
            alpha = max(alpha, value)

            if alpha >= beta:
                remaining = children[i + 1:]
                branches_pruned += len(remaining)

                for skipped in remaining:
                    print(f"Pruned branch: {node} -> {skipped}")
                break

        print(f"Node {node} (MAX) = {value}")
        return value

    else:
        value = float("inf")

        for i, child in enumerate(children):
            child_value = alpha_beta(child, True, alpha, beta)

            value = min(value, child_value)
            beta = min(beta, value)

            if alpha >= beta:
                remaining = children[i + 1:]
                branches_pruned += len(remaining)

                for skipped in remaining:
                    print(f"Pruned branch: {node} -> {skipped}")
                break

        print(f"Node {node} (MIN) = {value}")
        return value


print("Alpha-Beta Pruning Algorithm\n")

best_value = alpha_beta(
    "A", True, float("-inf"), float("inf")
)

best_move = max(root_moves, key=root_moves.get)

print("\nRoot Move Values:", root_moves)
print("Best Move:", best_move)
print("Best Utility Value:", best_value)
print("Total Nodes Evaluated:", nodes_evaluated)
print("Terminal Values Evaluated:", terminal_values_evaluated)
print("Branches Pruned:", branches_pruned)
