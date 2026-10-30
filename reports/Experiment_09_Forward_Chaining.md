# AI LAB – 3

## EXPERIMENT 9 - Forward Chaining

### AIM:
To implement forward chaining using rule-based medical appointment eligibility.

### QUESTION:

A healthcare appointment system uses facts and logical rules to determine whether a patient is eligible for a priority consultation. The system derives new facts from existing information by repeatedly applying rules until a conclusion is reached or no further facts can be inferred.

Develop a Python program to implement Forward Chaining using facts and rules.

The program must:

1. Represent the initial facts and inference rules.
2. Check whether the conditions of each rule are satisfied.
3. Infer and add new facts when a rule applies.
4. Continue the inference process until no new facts can be derived.
5. Display the initial facts, newly inferred facts, and final set of facts.

### CODE:

```python
facts = {
    "fever",
    "cough",
    "high_temperature",
    "age_over_65"
}

rules = [
    (["fever", "cough"], "respiratory_symptoms"),
    (["respiratory_symptoms", "high_temperature"],
     "suspected_infection"),
    (["suspected_infection", "age_over_65"],
     "priority_consultation")
]

trace = []

print("Forward Chaining Using Facts and Rules\n")

print("Initial Facts:")

for fact in sorted(facts):
    print("-", fact)

changed = True

while changed:
    changed = False

    for conditions, conclusion in rules:
        if all(condition in facts for condition in conditions):
            if conclusion not in facts:
                facts.add(conclusion)
                changed = True
                trace.append(
                    f"IF {conditions} THEN {conclusion}"
                )

                print(f"\nRule applied: {trace[-1]}")
                print(f"New fact inferred: {conclusion}")

print("\n--- Final Facts ---")

for fact in sorted(facts):
    print("-", fact)

print("\n--- Final Conclusion ---")

if "priority_consultation" in facts:
    print("Patient qualifies for a priority consultation.")
else:
    print("Priority consultation criteria not established.")

print("\nTotal new facts inferred:", len(trace))
```

### OUTPUT:

```text
Forward Chaining Using Facts and Rules

Initial Facts:
- age_over_65
- cough
- fever
- high_temperature

Rule applied: IF ['fever', 'cough'] THEN respiratory_symptoms
New fact inferred: respiratory_symptoms

Rule applied: IF ['respiratory_symptoms', 'high_temperature'] THEN suspected_infection
New fact inferred: suspected_infection

Rule applied: IF ['suspected_infection', 'age_over_65'] THEN priority_consultation
New fact inferred: priority_consultation

--- Final Facts ---
- age_over_65
- cough
- fever
- high_temperature
- priority_consultation
- respiratory_symptoms
- suspected_infection

--- Final Conclusion ---
Patient qualifies for a priority consultation.

Total new facts inferred: 3
```