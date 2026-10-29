# AI LAB 1

## EXPERIMENT 1 - BFS for Emergency Facility Navigation

### AIM:
To find a route through a hospital or emergency facility.

### QUESTION:

Develop a Python-based navigation system for an emergency response team operating inside a hospital represented as an unweighted graph. Rooms and junctions are vertices, while accessible corridors are edges. Implement Breadth-First Search (BFS) to identify the route from the emergency entrance to a designated critical-care unit.

The program must:

1. Represent the hospital layout as an adjacency list.
2. Accept the source and destination nodes.
3. Find and display the shortest route in terms of the number of corridors traversed.
4. Report the number of nodes explored and explain how BFS guarantees a shortest path in an unweighted graph.

### CODE:

```python
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'G'],
    'E': ['B', 'C', 'F'],
    'F': ['E', 'H'],
    'G': ['D', 'H'],
    'H': ['F', 'G']
}

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    distance = {start: 0}
    order = []

    print("BFS: Hospital Navigation")
    print(f"Start: {start} | Goal: {goal}\n")

    while queue:
        node = queue.popleft()
        order.append(node)

        print(f"Step {len(order)}: Node = {node}")
        print(f" Queue: {list(queue)}")

        if node == goal:
            print(" Goal reached!")
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
                print(f" {node} -> {neighbor}: Added to queue")
            else:
                print(f" {node} -> {neighbor}: Already visited")

        print(f" Visited: {sorted(visited)}")

    if goal not in parent:
        print("\nNo route found.")
        return

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("\n--- Final Result ---")
    print("Traversal order:", " -> ".join(order))
    print("Shortest path :", " -> ".join(path))
    print("Path cost     :", distance[goal], "corridors")
    print("Nodes explored :", len(order))


bfs(graph, 'A', 'H')
```

### OUTPUT:

```text
BFS: Hospital Navigation
Start: A | Goal: H

Step 1: Node = A
 Queue: []
 A -> B: Added to queue
 A -> C: Added to queue
 Visited: ['A', 'B', 'C']

Step 2: Node = B
 Queue: ['C']
 B -> A: Already visited
 B -> D: Added to queue
 B -> E: Added to queue
 Visited: ['A', 'B', 'C', 'D', 'E']

Step 3: Node = C
 Queue: ['D', 'E']
 C -> A: Already visited
 C -> E: Already visited
 Visited: ['A', 'B', 'C', 'D', 'E']

Step 4: Node = D
 Queue: ['E']
 D -> B: Already visited
 D -> G: Added to queue
 Visited: ['A', 'B', 'C', 'D', 'E', 'G']

Step 5: Node = E
 Queue: ['G']
 E -> B: Already visited
 E -> C: Already visited
 E -> F: Added to queue
 Visited: ['A', 'B', 'C', 'D', 'E', 'F', 'G']

Step 6: Node = G
 Queue: ['F']
 G -> D: Already visited
 G -> H: Added to queue
 Visited: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

Step 7: Node = F
 Queue: ['H']
 F -> E: Already visited
 F -> H: Already visited
 Visited: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

Step 8: Node = H
 Queue: []
 Goal reached!

--- Final Result ---
Traversal order: A -> B -> C -> D -> E -> G -> F -> H
Shortest path : A -> B -> D -> G -> H
Path cost     : 4 corridors
Nodes explored : 8
```