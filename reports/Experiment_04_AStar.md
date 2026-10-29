# AI LAB 1

## EXPERIMENT 4 - A* Search for Intelligent Route Planning

### APPLICATION:
To route planning for an autonomous delivery robot.

### QUESTION

Develop an intelligent route-planning system for an autonomous delivery robot navigating a network of locations connected by paths with different travel costs. Implement the A* search algorithm in Python to find a minimum-cost route from a specified starting location to a delivery destination.

The program must:

1. Represent the environment as a weighted graph.
2. Assign a heuristic estimate h(n) to each node and calculate the accumulated path cost g(n).
3. Use f(n) = g(n) + h(n) to determine which node to explore next.
4. Display the selected route, total path cost and node expansion order.
5. Explain how heuristic quality affects search efficiency and why an admissible heuristic matters for optimality.

### CODE:

```python
import heapq

# Weighted graph from the experiment image
graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 3), ('B', 2), ('D', 6), ('E', 4)],
    'D': [('B', 5), ('C', 6), ('E', 1), ('F', 2)],
    'E': [('C', 4), ('D', 1), ('F', 3)],
    'F': [('D', 2), ('E', 3)]
}

# Estimated cost from each node to goal F
h = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 0
}

def astar(start, goal):
    # Priority queue entries: (f, node, g, path)
    open_list = [(h[start], start, 0, [start])]
    best_g = {start: 0}
    expanded = []

    print("A* Search: Intelligent Route Planning")
    print(f"Start: {start} | Goal: {goal}\n")

    while open_list:
        f, node, g, path = heapq.heappop(open_list)

        # Ignore outdated entries
        if g != best_g.get(node):
            continue

        expanded.append(node)
        print(f"Step {len(expanded)}: Expand {node}")
        print(f" g(n)={g}, h(n)={h[node]}, f(n)={f}")

        if node == goal:
            print(" Goal reached!")
            break

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[neighbor]

            if new_g < best_g.get(neighbor, float('inf')):
                best_g[neighbor] = new_g
                new_path = path + [neighbor]

                heapq.heappush(
                    open_list,
                    (new_f, neighbor, new_g, new_path)
                )

                print(
                    f" {node}->{neighbor}: "
                    f"g={new_g}, h={h[neighbor]}, f={new_f} "
                    f"| Updated"
                )
            else:
                print(f" {node}->{neighbor}: No better cost")

        pending = sorted(
            (item[1], item[2], item[0])
            for item in open_list
            if item[2] == best_g.get(item[1])
        )

        print(" OPEN (node, g, f):", pending, "\n")

    if node == goal:
        print("--- Final Result ---")
        print("Optimal path     :", " -> ".join(path))
        print("Total path cost :", g)
        print("Nodes expanded :", len(expanded))
        print("Expansion order :", " -> ".join(expanded))
    else:
        print("No route found.")


astar('A', 'F')
```

### OUTPUT:

```text
A* Search: Intelligent Route Planning
Start: A | Goal: F

Step 1: Expand A
 g(n)=0, h(n)=6, f(n)=6
 A->B: g=4, h=4, f=8 | Updated
 A->C: g=3, h=5, f=8 | Updated
 OPEN (node, g, f): [('B', 4, 8), ('C', 3, 8)]

Step 2: Expand B
 g(n)=4, h(n)=4, f(n)=8
 B->A: No better cost
 B->C: No better cost
 B->D: g=9, h=2, f=11 | Updated
 OPEN (node, g, f): [('C', 3, 8), ('D', 9, 11)]

Step 3: Expand C
 g(n)=3, h(n)=5, f(n)=8
 C->A: No better cost
 C->B: No better cost
 C->D: No better cost
 C->E: g=7, h=3, f=10 | Updated
 OPEN (node, g, f): [('D', 9, 11), ('E', 7, 10)]

Step 4: Expand E
 g(n)=7, h(n)=3, f(n)=10
 E->C: No better cost
 E->D: g=8, h=2, f=10 | Updated
 E->F: g=10, h=0, f=10 | Updated
 OPEN (node, g, f): [('D', 8, 10), ('F', 10, 10)]

Step 5: Expand D
 g(n)=8, h(n)=2, f(n)=10
 D->B: No better cost
 D->C: No better cost
 D->E: No better cost
 D->F: No better cost
 OPEN (node, g, f): [('F', 10, 10)]

Step 6: Expand F
 g(n)=10, h(n)=0, f(n)=10
 Goal reached!
--- Final Result ---
Optimal path     : A -> C -> E -> F
Total path cost : 10
Nodes expanded : 6
Expansion order : A -> B -> C -> E -> D -> F
```