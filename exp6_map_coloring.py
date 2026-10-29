
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
