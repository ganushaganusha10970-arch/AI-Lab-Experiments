
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
