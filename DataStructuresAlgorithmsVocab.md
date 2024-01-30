## Vocab

**Primitive vs. Non-primitive Data Structures:** Primitive data structures store single values directly, while non-primitive data structures organize multiple values.

**Linear vs. Non-linear Data Structures:** Linear data structures store elements sequentially, while non-linear structures allow branching or multiple paths.

**Linked Lists:** A linear data structure where elements, called nodes, are linked by pointers, allowing dynamic memory allocation.

**Stacks:** A linear data structure with Last-In-First-Out (LIFO) access, supporting operations like push and pop.

**Queues:** A linear data structure with First-In-First-Out (FIFO) access, supporting operations like enqueue and dequeue.

**Trees:** A non-linear data structure composed of nodes connected by edges, with one designated as the root, allowing hierarchical representation.

**Graphs:** A non-linear data structure comprising vertices connected by edges, representing relationships between objects.

**Traversing:** Process of accessing and visiting all elements of a data structure in a specific order.

**Searching:** Process of finding a target element within a data structure.

```python
names = ["Sheel", "Nate", "Joseph", "Cyrus", "Edward", "Julissa"]

for name in names:
    if name == "Joseph":
        break
```

**Inserting / Deleting:** Operations to add or remove elements from a data structure.

```python
names = ["Sheel", "Nate", "Joseph", "Cyrus", "Edward", "Julissa"]

names.insert(3, "Jeff") # Insertion
names.remove("Sheel") # Deletion
```

**Sorting:** Process of arranging elements in a specific order such as ascending or descending.

```python
scores = [5, 2, 19, 37, 3]

scores.sort()
```

**Merging:** Combining two or more data structures into a single structure while maintaining its properties.

```python
names = ["Sheel", "Nate", "Joseph"]

more_names = ["Cyrus", "Edward", "Julissa"]

all_names = names + more_names
```


## References: 

[W3 Schools](https://www.w3schools.com/python/gloss_python_join_lists.asp)

[FreeCodeCamp](https://www.freecodecamp.org/news/how-linked-lists-work/)