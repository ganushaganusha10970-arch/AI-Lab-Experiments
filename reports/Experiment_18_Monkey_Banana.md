# AI LAB – 5

## EXPERIMENT 18: Monkey and Banana Problem Using State-Space Planning

### AIM:
To implement Goal-based planning in an autonomous warehouse robot using Python.

### QUESTION:

A monkey is inside a room containing a box and a banana hanging from the ceiling. The monkey cannot reach the banana directly. It must move to the box, push it beneath the banana, climb onto the box and grasp the banana.

Develop a Python program that represents the problem using state-space representation and determines the sequence of actions required to obtain the banana.

### CODE:

```python
from collections import deque

# Locations: 0 = A, 1 = B, 2 = C

# Banana is hanging at location C

initial_state = (0, 1, False, False)

goal_location = 2

# State: (monkey_position, box_position, on_box, has_banana)


def get_actions(state):

    monkey, box, on_box, has_banana = state

    actions = []

    if has_banana:

        return actions

    # Move monkey left or right

    if not on_box:

        for direction in [-1, 1]:

            new_position = monkey + direction

            if 0 <= new_position <= 2 and new_position != box:

                actions.append((

                    (new_position, box, False, False),

                    "Move to location " + str(new_position)

                ))

    # Push the box one step away from the monkey

    if not on_box and abs(monkey - box) == 1:

        direction = 1 if box > monkey else -1

        new_box_position = box + direction

        if 0 <= new_box_position <= 2:

            actions.append((

                (box, new_box_position, False, False),

                "Push the box to location " + str(new_box_position)

            ))

    # Climb onto the box

    if not on_box and abs(monkey - box) == 1 and box == goal_location:

        actions.append((

            (box, box, True, False),

            "Climb onto the box"

        ))

    # Grasp the banana

    if on_box and monkey == goal_location and box == goal_location:

        actions.append((

            (monkey, box, True, True),

            "Grasp the banana"

        ))

    return actions


def solve_monkey_problem():

    queue = deque([(initial_state, [])])

    visited = {initial_state}

    while queue:

        current_state, path = queue.popleft()

        if current_state[3]:

            return path

        for next_state, action in get_actions(current_state):

            if next_state not in visited:

                visited.add(next_state)

                queue.append((next_state, path + [action]))

    return None


# Execute the planning algorithm

solution = solve_monkey_problem()

print("Monkey and Banana Problem")

print("-------------------------")

print("Initial State: Monkey at A, Box at B")

print("Banana Location: C")

print("\nSequence of Actions:")

if solution:

    for step, action in enumerate(solution, 1):

        print("Step", step, ":", action)

    print("\nGoal Achieved: Monkey obtained the banana!")

    print("Total Actions:", len(solution))

else:

    print("No solution found.")
```

### OUTPUT:

```text
Monkey and Banana Problem

-------------------------

Initial State: Monkey at A, Box at B

Banana Location: C

Sequence of Actions:

Step 1 : Push the box to location 2

Step 2 : Climb onto the box

Step 3 : Grasp the banana

Goal Achieved: Monkey obtained the banana!

Total Actions: 3
```