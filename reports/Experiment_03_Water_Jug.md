# AI LAB 1

## EXPERIMENT 3 - State-Space Search for Water Resource Allocation

### AIM:
To Measure a target quantity using containers with fixed capacities.

### QUESTION:

Design a Python-based state-space search solution for a water allocation problem involving two unmarked containers with capacities of 4 litres and 3 litres. Starting with both containers empty, determine a sequence of valid operations that leaves exactly 2 litres in the 4-litre container.

The program must:

1. Represent each state as the quantities of water in both containers.
2. Define the legal actions: fill, empty and transfer water between containers.
3. Search the state space using BFS and identify a valid solution.
4. Display the sequence of states and actions from the initial state to the goal.
5. Explain how state representation, goal testing and repeated-state detection affect the search.

### CODE:

```python
from collections import deque

def water_jug_bfs():
    start = (0, 0)
    goal = 2
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    action = {start: "Initial state"}
    capacities = (4, 3)

    def get_next_states(a, b):
        states = []

        # Fill either jug
        states.append(((4, b), "Fill 4-litre jug"))
        states.append(((a, 3), "Fill 3-litre jug"))

        # Empty either jug
        states.append(((0, b), "Empty 4-litre jug"))
        states.append(((a, 0), "Empty 3-litre jug"))

        # Pour 4-litre jug into 3-litre jug
        transfer = min(a, capacities[1] - b)
        states.append(((a - transfer, b + transfer),
                       "Pour 4-litre jug into 3-litre jug"))

        # Pour 3-litre jug into 4-litre jug
        transfer = min(b, capacities[0] - a)
        states.append(((a + transfer, b - transfer),
                       "Pour 3-litre jug into 4-litre jug"))

        return states

    step = 0
    goal_state = None

    print("Water Jug Problem: State-Space Search")
    print("Start state:", start)
    print("Goal: Exactly 2 litres in the 4-litre jug\n")

    while queue:
        current = queue.popleft()
        step += 1
        a, b = current

        print(f"Step {step}: State = {current}")
        print(" Queue:", list(queue))

        if a == goal:
            goal_state = current
            print(" Goal reached!")
            break

        for next_state, operation in get_next_states(a, b):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                action[next_state] = operation
                queue.append(next_state)

                print(f" Action: {operation}")
                print(f" New state: {next_state}")
            else:
                print(f" Skipped {next_state}: Already visited")

    print("\n--- Final Result ---")

    if goal_state is None:
        print("No solution found.")
        return

    path = []
    current = goal_state

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    for i, state in enumerate(path):
        print(f"Step {i}: {state} | {action[state]}")

    print("\nSolution path:", " -> ".join(map(str, path)))
    print("Operations required:", len(path) - 1)
    print("States discovered:", len(visited))


water_jug_bfs()
```

### OUTPUT:

```text
Water Jug Problem: State-Space Search
Start state: (0, 0)
Goal: Exactly 2 litres in the 4-litre jug

Step 1: State = (0, 0)
 Queue: []
 Action: Fill 4-litre jug
 New state: (4, 0)
 Action: Fill 3-litre jug
 New state: (0, 3)
 Skipped (0, 0): Already visited
 Skipped (0, 0): Already visited
 Skipped (0, 0): Already visited
 Skipped (0, 0): Already visited
Step 2: State = (4, 0)
 Queue: [(0, 3)]
 Skipped (4, 0): Already visited
 Action: Fill 3-litre jug
 New state: (4, 3)
 Skipped (0, 0): Already visited
 Skipped (4, 0): Already visited
 Action: Pour 4-litre jug into 3-litre jug
 New state: (1, 3)
 Skipped (4, 0): Already visited
Step 3: State = (0, 3)
 Queue: [(4, 3), (1, 3)]
 Skipped (4, 3): Already visited
 Skipped (0, 3): Already visited
 Skipped (0, 3): Already visited
 Skipped (0, 0): Already visited
 Skipped (0, 3): Already visited
 Action: Pour 3-litre jug into 4-litre jug
 New state: (3, 0)
Step 4: State = (4, 3)
 Queue: [(1, 3), (3, 0)]
 Skipped (4, 3): Already visited
 Skipped (4, 3): Already visited
 Skipped (0, 3): Already visited
 Skipped (4, 0): Already visited
 Skipped (4, 3): Already visited
 Skipped (4, 3): Already visited
Step 5: State = (1, 3)
 Queue: [(3, 0)]
 Skipped (4, 3): Already visited
 Skipped (1, 3): Already visited
 Skipped (0, 3): Already visited
 Action: Empty 3-litre jug
 New state: (1, 0)
 Skipped (1, 3): Already visited
 Skipped (4, 0): Already visited
Step 6: State = (3, 0)
 Queue: [(1, 0)]
 Skipped (4, 0): Already visited
 Action: Fill 3-litre jug
 New state: (3, 3)
 Skipped (0, 0): Already visited
 Skipped (3, 0): Already visited
 Skipped (0, 3): Already visited
 Skipped (3, 0): Already visited
Step 7: State = (1, 0)
 Queue: [(3, 3)]
 Skipped (4, 0): Already visited
 Skipped (1, 3): Already visited
 Skipped (0, 0): Already visited
 Skipped (1, 0): Already visited
 Action: Pour 4-litre jug into 3-litre jug
 New state: (0, 1)
 Skipped (1, 0): Already visited
Step 8: State = (3, 3)
 Queue: [(0, 1)]
 Skipped (4, 3): Already visited
 Skipped (3, 3): Already visited
 Skipped (0, 3): Already visited
 Skipped (3, 0): Already visited
 Skipped (3, 3): Already visited
 Action: Pour 3-litre jug into 4-litre jug
 New state: (4, 2)
Step 9: State = (0, 1)
 Queue: [(4, 2)]
 Action: Fill 4-litre jug
 New state: (4, 1)
 Skipped (0, 3): Already visited
 Skipped (0, 1): Already visited
 Skipped (0, 0): Already visited
 Skipped (0, 1): Already visited
 Skipped (1, 0): Already visited
Step 10: State = (4, 2)
 Queue: [(4, 1)]
 Skipped (4, 2): Already visited
 Skipped (4, 3): Already visited
 Action: Empty 4-litre jug
 New state: (0, 2)
 Skipped (4, 0): Already visited
 Skipped (3, 3): Already visited
 Skipped (4, 2): Already visited
Step 11: State = (4, 1)
 Queue: [(0, 2)]
 Skipped (4, 1): Already visited
 Skipped (4, 3): Already visited
 Skipped (0, 1): Already visited
 Skipped (4, 0): Already visited
 Action: Pour 4-litre jug into 3-litre jug
 New state: (2, 3)
 Skipped (4, 1): Already visited
Step 12: State = (0, 2)
 Queue: [(2, 3)]
 Skipped (4, 2): Already visited
 Skipped (0, 3): Already visited
 Skipped (0, 2): Already visited
 Skipped (0, 0): Already visited
 Skipped (0, 2): Already visited
 Action: Pour 3-litre jug into 4-litre jug
 New state: (2, 0)
Step 13: State = (2, 3)
 Queue: [(2, 0)]
 Goal reached!

--- Final Result ---
Step 0: (0, 0) | Initial state
Step 1: (4, 0) | Fill 4-litre jug
Step 2: (1, 3) | Pour 4-litre jug into 3-litre jug
Step 3: (1, 0) | Empty 3-litre jug
Step 4: (0, 1) | Pour 4-litre jug into 3-litre jug
Step 5: (4, 1) | Fill 4-litre jug
Step 6: (2, 3) | Pour 4-litre jug into 3-litre jug

Solution path: (0, 0) -> (4, 0) -> (1, 3) -> (1, 0) -> (0, 1) -> (4, 1) -> (2, 3)
Operations required: 6
States discovered: 14
```