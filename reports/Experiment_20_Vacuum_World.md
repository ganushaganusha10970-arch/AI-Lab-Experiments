# AI LAB – 5

## EXPERIMENT 20: Simple Reflex Agent for Vacuum World

### AIM:
To implement autonomous cleaning robot for smart offices using Python.

### QUESTION:

A smart office uses an autonomous vacuum-cleaning robot to clean different rooms. The robot senses whether its current location is dirty or clean and selects an appropriate action, such as cleaning the floor or moving to another location.

Develop a Python program that simulates a vacuum-cleaning agent operating in a four-room environment.

The agent should:

1. Identify its current location.
2. Detect whether the current room is dirty or clean.
3. Clean the room if it is dirty.
4. Move to the next room if the current room is clean.
5. Stop the simulation when all rooms are clean.

### CODE:

```python
rooms = {

    'A': 'Dirty',

    'B': 'Clean',

    'C': 'Dirty',

    'D': 'Dirty'

}

locations = ['A', 'B', 'C', 'D']

current_position = 0

def simple_reflex_agent(location, status):

    if status == 'Dirty':

        return 'Suck'

    return 'Move'


print("Simple Reflex Agent - Vacuum World")

print("-----------------------------------")

print("Initial Room Conditions:", rooms)

step = 1

while True:

    if all(status == 'Clean' for status in rooms.values()):

        print("\nAll rooms are clean!")

        print("Cleaning task completed.")

        break

    current_room = locations[current_position]

    current_status = rooms[current_room]

    action = simple_reflex_agent(

        current_room,

        current_status

    )

    print(

        "\nStep", step,

        "- Location:", current_room,

        "- Status:", current_status

    )

    # Execute action

    if action == 'Suck':

        rooms[current_room] = 'Clean'

        print("Action: Cleaning room", current_room)

    else:

        print("Action: Moving to next room")

        current_position = (

            current_position + 1

        ) % len(locations)

    step += 1

print("\nFinal Room Conditions:", rooms)

print("Total Actions Performed:", step - 1)
```

### OUTPUT:

```text
Simple Reflex Agent - Vacuum World

-----------------------------------

Initial Room Conditions: {'A': 'Dirty', 'B': 'Clean', 'C': 'Dirty', 'D': 'Dirty'}

Step 1 - Location: A - Status: Dirty
Action: Cleaning room A

Step 2 - Location: A - Status: Clean
Action: Moving to next room

Step 3 - Location: B - Status: Clean
Action: Moving to next room

Step 4 - Location: C - Status: Dirty
Action: Cleaning room C

Step 5 - Location: C - Status: Clean
Action: Moving to next room

Step 6 - Location: D - Status: Dirty
Action: Cleaning room D

All rooms are clean!
Cleaning task completed.

Final Room Conditions: {'A': 'Clean', 'B': 'Clean', 'C': 'Clean', 'D': 'Clean'}

Total Actions Performed: 6
```