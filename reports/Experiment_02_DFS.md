# AI LAB 1

## EXPERIMENT 2 - DFS for Dependency and Reachability Analysis

### AIM:
To analyse dependencies in an AI software pipeline.

### QUESTION:

An AI deployment pipeline consists of interconnected processing tasks, where each task depends on one or more downstream tasks. Model the pipeline as a directed graph and implement Depth-First Search (DFS) in Python to determine whether a specified target task is reachable from a given starting task.

The program must:

1. Represent the pipeline using a directed adjacency list.
2. Accept a starting task and a target task.
3. Display the DFS traversal order and determine whether the target is reachable.
4. Reconstruct a valid path to the target, if one exists.
5. Explain how visited-node tracking prevents repeated exploration and how DFS behaves when the graph contains cycles.

### CODE:

```python
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': ['L'],
    'L': []
}

def dfs(graph, start, goal):
    visited = set()
    path = []
    order = []

    def search(node):
        visited.add(node)
        order.append(node)
        path.append(node)

        print(f"Step {len(order)}: Node = {node}")
        print(f" Current path: {' -> '.join(path)}")

        if node == goal:
            print(" Goal reached!")
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                print(f" Exploring edge: {node} -> {neighbor}")

                if search(neighbor):
                    return True
            else:
                print(f" Skipping {neighbor}: Already visited")

        path.pop()
        print(f" Backtracking from {node}")
        return False

    print("DFS: AI Pipeline Reachability")
    print(f"Start: {start} | Goal: {goal}\n")

    found = search(start)

    print("\n--- Final Result ---")
    print("Traversal order:", " -> ".join(order))

    if found:
        print("Path found    :", " -> ".join(path))
        print("Path length   :", len(path) - 1, "edges")
    else:
        print("No path exists.")
        print("Path found    : None")

    print("Nodes explored :", len(order))


dfs(graph, 'A', 'H')
```

### OUTPUT:

```text
DFS: AI Pipeline Reachability
Start: A | Goal: H

Step 1: Node = A
 Current path: A
 Exploring edge: A -> B
Step 2: Node = B
 Current path: A -> B
 Exploring edge: B -> E
Step 3: Node = E
 Current path: A -> B -> E
 Exploring edge: E -> H
Step 4: Node = H
 Current path: A -> B -> E -> H
 Goal reached!

--- Final Result ---
Traversal order: A -> B -> E -> H
Path found    : A -> B -> E -> H
Path length   : 3 edges
Nodes explored : 4
```