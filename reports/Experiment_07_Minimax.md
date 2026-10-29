# AI LAB 1

## EXPERIMENT 7 - Implementing the Minimax Algorithm

### AIM:
To implement the Minimax algorithm to evaluate a game tree and determine the best move using terminal utility values.

### QUESTION:

Develop a Python program to implement the Minimax algorithm for a game tree with terminal utility values. Evaluate the tree recursively by alternating between MAX and MIN nodes to determine the optimal move for the maximizing player.

The program must:

1. Represent the game tree using a dictionary.
2. Assign terminal utility values to the leaf nodes.
3. Implement the Minimax algorithm using recursive evaluation.
4. Evaluate MAX and MIN nodes and display their resulting utility values.
5. Identify and display the best move from the root node and its utility value.

### CODE:

```python
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
```

### OUTPUT:

```text
Minimax Algorithm Evaluation

Node D (MAX): [3, 5] -> 5
Node E (MAX): [2, 9] -> 9
Node B (MIN): {'D': 5, 'E': 9} -> 5
Node F (MAX): [12, 5] -> 12
Node G (MAX): [23, 23] -> 23
Node C (MIN): {'F': 12, 'G': 23} -> 12

Root A (MAX): {'B': 5, 'C': 12}
Best Move: C
Best Utility Value: 12
```