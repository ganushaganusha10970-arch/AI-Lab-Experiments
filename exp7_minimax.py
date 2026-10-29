
# Experiment 7: Implementing the Minimax Algorithm

# Game tree and terminal utility values
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [3, 5],
    "E": [2, 9],
    "F": [12, 5],
    "G": [23, 23]
}


def minimax(node, maximizing):
    children = tree[node]

    # Evaluate terminal utility values
    if all(isinstance(value, int) for value in children):
        if maximizing:
            result = max(children)
            role = "MAX"
        else:
            result = min(children)
            role = "MIN"

        print(f"Node {node} ({role}): {children} -> {result}")
        return result

    # Recursively evaluate child nodes
    values = {}

    for child in children:
        values[child] = minimax(child, not maximizing)

    if maximizing:
        result = max(values.values())
        role = "MAX"
    else:
        result = min(values.values())
        role = "MIN"

    print(f"Node {node} ({role}): {values} -> {result}")
    return result


print("Minimax Algorithm Evaluation\n")

root_values = {}

# A is the MAX root, so B and C are MIN nodes
for move in tree["A"]:
    root_values[move] = minimax(move, False)

best_move = max(root_values, key=root_values.get)
best_value = root_values[best_move]

print("\nRoot A (MAX):", root_values)
print("Best Move:", best_move)
print("Best Utility Value:", best_value)
