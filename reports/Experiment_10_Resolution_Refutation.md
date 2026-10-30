# AI LAB – 3

## EXPERIMENT 10 - Resolution Refutation

### AIM:
To verify whether a student qualifies as a happy student using logical statements.

### QUESTION:

A university models student well-being using logical facts and rules. It wants to determine whether a student is happy based on the conditions that the student enjoys learning and has sufficient free time.

Develop a Python program to implement Resolution Refutation to prove whether a student is happy.

The program must:

1. Represent the knowledge base using logical statements.
2. Convert the relevant statements into Conjunctive Normal Form (CNF).
3. Negate the goal to be proved and add it to the knowledge base.
4. Apply the resolution rule to derive new clauses.
5. Identify the empty clause, if obtained, to demonstrate a contradiction and establish the goal.

### CODE:

```python
clauses = [
    {"EnjoysLearning"},              # C1
    {"HasFreeTime"},                 # C2
    {"NotEnjoysLearning", "Happy"},  # C3
    {"NotHasFreeTime", "Happy"}      # C4
]

goal = "Happy"

print("Resolution Refutation\n")

print("--- Knowledge Base (CNF) ---")

for i, clause in enumerate(clauses, start=1):
    print(f"C{i}: {' OR '.join(sorted(clause))}")

# Negate the goal and add it to the knowledge base
negated_goal = "Not" + goal

clauses.append({negated_goal})

print(f"\nNegated goal added: {negated_goal}")

# Resolve complementary literals

derived = set()

empty_clause_found = False

print("\n--- Resolution Steps ---")

changed = True

while changed and not empty_clause_found:
    changed = False

    current_clauses = list(clauses)

    for i in range(len(current_clauses)):
        for j in range(i + 1, len(current_clauses)):
            c1 = current_clauses[i]
            c2 = current_clauses[j]

            for literal in c1:
                if literal.startswith("Not"):
                    complement = literal[3:]
                else:
                    complement = "Not" + literal

                if complement in c2:
                    resolvent = (c1 - {literal}) | (c2 - {complement})

                    print(
                        f"Resolve {sorted(c1)} and {sorted(c2)} "
                        f"on {literal} -> {sorted(resolvent)}"
                    )

                    if not resolvent:
                        empty_clause_found = True
                        break

                    frozen_resolvent = frozenset(resolvent)

                    if (
                        frozen_resolvent not in
                        {frozenset(c) for c in clauses}
                        and frozen_resolvent not in derived
                    ):
                        derived.add(frozen_resolvent)
                        changed = True

                if empty_clause_found:
                    break

            if empty_clause_found:
                break

    for clause in derived:
        new_clause = set(clause)

        if new_clause not in clauses:
            clauses.append(new_clause)

    derived.clear()

print("\n--- Final Result ---")

if empty_clause_found:
    print("Empty clause derived: Yes")
    print("Contradiction found.")
    print("Therefore, the goal 'Happy' is proved.")
else:
    print("Empty clause derived: No")
    print("The goal could not be proved by this resolution run.")
```

### OUTPUT:

```text
Resolution Refutation

--- Knowledge Base (CNF) ---
C1: EnjoysLearning
C2: HasFreeTime
C3: Happy OR NotEnjoysLearning
C4: Happy OR NotHasFreeTime

Negated goal added: NotHappy

--- Resolution Steps ---
Resolve ['EnjoysLearning'] and ['Happy', 'NotEnjoysLearning'] on EnjoysLearning -> ['Happy']
Resolve ['HasFreeTime'] and ['Happy', 'NotHasFreeTime'] on HasFreeTime -> ['Happy']
Resolve ['Happy', 'NotEnjoysLearning'] and ['NotHappy'] on Happy -> ['NotEnjoysLearning']
Resolve ['Happy', 'NotHasFreeTime'] and ['NotHappy'] on Happy -> ['NotHasFreeTime']
Resolve ['EnjoysLearning'] and ['Happy', 'NotEnjoysLearning'] on EnjoysLearning -> ['Happy']
Resolve ['EnjoysLearning'] and ['NotEnjoysLearning'] on EnjoysLearning -> []

--- Final Result ---
Empty clause derived: Yes
Contradiction found.
Therefore, the goal 'Happy' is proved.
```