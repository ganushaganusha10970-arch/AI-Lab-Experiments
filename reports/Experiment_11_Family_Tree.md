# AI LAB – 3

## EXPERIMENT 11: Family Tree

### AIM:
To represent family relationships in an expert system.

### QUESTION:

Develop a program to represent family relationships using facts and rules. Given a family tree, identify the parents, children, and grandparents of specified individuals.

### CODE:

```python
parents = [
    ("Ravi", "Arun"),
    ("Ravi", "Meena"),
    ("Arun", "Kiran"),
    ("Meena", "Priya"),
    ("Suresh", "Ravi")
]


def is_parent(parent, child):
    return (parent, child) in parents


def get_children(parent):
    return [child for p, child in parents if p == parent]


def get_parents(child):
    return [parent for parent, c in parents if c == child]


def get_grandparents(person):
    grandparents = []

    for parent in get_parents(person):
        grandparents.extend(get_parents(parent))

    return grandparents


# Display family relationships

person = "Kiran"

print("Family Tree Relationships")
print("-------------------------")

print("Parents of", person, ":", get_parents(person))
print("Children of Ravi:", get_children("Ravi"))
print("Grandparents of", person, ":", get_grandparents(person))

print("\nIs Ravi a parent of Arun?", is_parent("Ravi", "Arun"))

print("Is Suresh a grandparent of Kiran?",
      "Suresh" in get_grandparents("Kiran"))
```

### OUTPUT:

```text
Family Tree Relationships

-------------------------

Parents of Kiran : ['Arun']

Children of Ravi: ['Arun', 'Meena']

Grandparents of Kiran : ['Ravi']

Is Ravi a parent of Arun? True

Is Suresh a grandparent of Kiran? False
```