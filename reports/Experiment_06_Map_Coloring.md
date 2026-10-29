# AI LAB 1

## EXPERIMENT 6 - Map Colouring Using CSP

### AIM:
To solve the map colouring problem using a Constraint Satisfaction Problem (CSP) and backtracking, ensuring that no two adjacent regions have the same colour.

### QUESTION:

Develop a Python program to solve a map colouring problem involving six regions, represented by a constraint graph. Assign colours to the regions from the available set of Red, Green and Blue using backtracking.

The program must:

1. Represent the regions and their adjacency relationships.
2. Define the available colours for each region.
3. Check that adjacent regions do not receive the same colour.
4. Use backtracking to find a valid colour assignment.
5. Display the final colour assignment, verify all adjacency constraints, and report the number of assignment attempts.

### CODE:

```python
# Experiment 6: Map Colouring Using CSP

regions = ["A", "B", "C", "D", "E", "F"]
colors = ["Red", "Green", "Blue"]

neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D", "F"],
    "F": ["D", "E"]
}

assignment = {}
attempts = 0


def is_consistent(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def backtrack(index=0):
    global attempts

    if index == len(regions):
        return True

    region = regions[index]

    for color in colors:
        attempts += 1

        if is_consistent(region, color):
            assignment[region] = color

            if backtrack(index + 1):
                return True

            del assignment[region]

    return False


if backtrack():
    print("Map Colouring Solution Found!")
    print("\nFinal Colour Assignment:")

    for region in regions:
        print(f"Region {region}: {assignment[region]}")

    valid = all(
        assignment[region] != assignment[neighbor]
        for region in regions
        for neighbor in neighbors[region]
    )

    print("\nAll adjacency constraints satisfied:", valid)
    print("Assignment attempts:", attempts)
else:
    print("No valid colouring found.")
```

### OUTPUT:

```text
Map Colouring Solution Found!

Final Colour Assignment:
Region A: Red
Region B: Green
Region C: Blue
Region D: Red
Region E: Green
Region F: Blue

All adjacency constraints satisfied: True
Assignment attempts: 12
```