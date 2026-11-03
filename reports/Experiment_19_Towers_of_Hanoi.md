# AI LAB – 5

## EXPERIMENT 19: Towers of Hanoi Using Recursion in Python

### AIM:
To implement automated disk transfer and robotic manipulation using Python.

### QUESTION:

A robotic system needs to transfer a stack of objects from one platform to another while following specific placement constraints. The Towers of Hanoi problem demonstrates how a system can break a complex task into smaller subproblems using recursion.

Three rods are provided: Source (A), Auxiliary (B) and Destination (C). A stack of disks of different sizes is placed on the source rod.

Develop a Python program to transfer all disks from the source rod to the destination rod while following these rules:

1. Only one disk can be moved at a time.
2. Only the top disk of a rod can be moved.
3. A larger disk cannot be placed on a smaller disk.

### CODE:

```python
move_count = 0


def tower_of_hanoi(n, source, auxiliary, destination):

    global move_count

    if n == 1:

        move_count += 1

        print(
            "Move disk 1 from",
            source,
            "to",
            destination
        )

        return

    tower_of_hanoi(
        n - 1,
        source,
        destination,
        auxiliary
    )

    move_count += 1

    print(
        "Move disk", n,
        "from", source,
        "to", destination
    )

    tower_of_hanoi(
        n - 1,
        auxiliary,
        source,
        destination
    )


n = 3

print("Towers of Hanoi")

print("----------------")

print("Number of disks:", n)

print("\nSequence of moves:")

tower_of_hanoi(n, 'A', 'B', 'C')

print("\nTotal Moves:", move_count)

print("Minimum Moves Required:", 2**n - 1)
```

### OUTPUT:

```text
Towers of Hanoi

----------------

Number of disks: 3

Sequence of moves:

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C

Total Moves: 7

Minimum Moves Required: 7
```