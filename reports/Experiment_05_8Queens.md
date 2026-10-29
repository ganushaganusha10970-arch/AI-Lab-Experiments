# AI LAB 1

## EXPERIMENT 5 - 8-Queens Problem Using Backtracking

### AIM:
To solve the 8-Queens problem using the backtracking algorithm by placing eight queens on a chessboard such that no two queens attack each other.

### QUESTION:

Develop a Python program to solve the 8-Queens problem using backtracking. Place eight queens on an 8 × 8 chessboard so that no two queens share the same row, column, or diagonal.

The program must:

1. Represent the chessboard using a list to store queen positions.
2. Check whether a queen can be safely placed in a particular column.
3. Use backtracking to explore possible queen positions.
4. Display the chessboard after finding a valid solution.
5. Display the row and column positions of all eight queens and the total number of placement attempts.

### CODE:

```python
# Experiment 5: 8-Queens Problem Using Backtracking

N = 8
positions = [-1] * N
attempts = 0


def is_safe(row, col):
    for previous_row in range(row):
        previous_col = positions[previous_row]

        if previous_col == col:
            return False

        if abs(previous_col - col) == abs(row - previous_row):
            return False

    return True


def solve(row=0):
    global attempts

    if row == N:
        return True

    for col in range(N):
        attempts += 1

        if is_safe(row, col):
            positions[row] = col

            if solve(row + 1):
                return True

            positions[row] = -1

    return False


if solve():
    print("8-Queens Solution Found!")
    print("\nChessboard:")

    for row in range(N):
        print(" ".join(
            "Q" if positions[row] == col else "."
            for col in range(N)
        ))

    print("\nQueen Positions (Row, Column):")
    for row, col in enumerate(positions):
        print(f"Queen {row + 1}: ({row + 1}, {col + 1})")

    print("\nPlacement attempts:", attempts)
else:
    print("No solution found.")
```

### OUTPUT:

```text
8-Queens Solution Found!

Chessboard:
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .

Queen Positions (Row, Column):
Queen 1: (1, 1)
Queen 2: (2, 5)
Queen 3: (3, 8)
Queen 4: (4, 6)
Queen 5: (5, 3)
Queen 6: (6, 7)
Queen 7: (7, 2)
Queen 8: (8, 4)

Placement attempts: 876
```