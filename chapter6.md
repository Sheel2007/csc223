## Introduction to Linked Lists

- **Introduction to Linked Lists:**
  - Arrays: Linear collections of data elements in consecutive memory locations.
  - Limitations: Fixed size determined during declaration, restricting the number of elements.
  - Need for flexibility: Uncertain number of elements, efficient memory utilization.
- **Linked Lists Features:**
  - Dynamic sizing: Accommodates any number of elements without predefining size.
  - Memory flexibility: Does not store elements in consecutive memory locations.
  - Access method: Sequential access only, unlike arrays supporting random access.
- **Advantages:**
  - Insertions and deletions: Constant time complexity at any point in the list.
  - Versatility: Offers solutions for various programming scenarios without maximum element limits.

## Basic Terminologies of Linked Lists

- **Linked List Overview:**
  - Linear collection of data elements termed as nodes.
  - Acts as a foundational structure for implementing other data structures like stacks, queues, etc.

- **Node Structure:**
  - Each node comprises data fields and a pointer to the next node.
  - Data field can hold simple data types, arrays, or structures.
  - Pointer to the next node indicates the sequence.
  - Last node contains a NULL pointer, signifying the end of the list.

- **Pointer Representation:**
  - NULL pointer, often represented by X or -1, marks the end of the list.
  - Self-referential data type: Every node contains a pointer to another node of the same type.

- **START Pointer:**
  - Pointer variable storing the address of the first node in the list.
  - Enables traversal of the list; subsequent nodes linked via their address.

- **Empty List Check:**
  - If START = NULL, the list is empty with no nodes.


## Linked Lists vs. Arrays

- **Linear Collection:**
  - Both arrays and linked lists are linear collections of data elements.

- **Memory Storage:**
  - Arrays store elements in consecutive memory locations.
  - Linked lists do not store nodes in consecutive memory locations.

- **Access Method:**
  - Arrays support random access of data.
  - Linked lists allow sequential access only.

- **Insertions and Deletions:**
  - Both arrays and linked lists support insertions and deletions at any point in constant time.

- **Dynamic Sizing:**
  - Linked lists allow adding any number of elements without predefining size.
  - Arrays have a fixed size determined during declaration.

- **Advantages of Linked Lists:**
  - No restriction on the number of elements.
  - Efficient for insertion, deletion, and updating operations.

- **Trade-offs:**
  - Linked lists require extra space to store the address of next nodes.

## Memory Allocation and De-allocation for Linked Lists

- **Adding a Node:**
  - Find free space in memory and use it to store information.
  - Example: Adding a new student's record to a linked list.

- **Free Space Management:**
  - Computer maintains a list of all free memory cells, known as the free pool.
  - Operating system manages this list and allocates free memory cells.

- **Pointer Variables:**
  - Linked list: START pointer stores the address of the first node.
  - Free pool: AVAIL pointer stores the address of the first free space.

- **Insertion Process:**
  - AVAIL pointer points to the first free space in memory.
  - Memory address pointed by AVAIL is used to store new information.
  - After insertion, AVAIL is updated to point to the next available free space.

- **Deletion Process:**
  - Operating system manages memory deallocation.
  - Freed memory cells are added back to the free pool.
  - Process known as garbage collection.

- **Operating System's Role:**
  - Manages memory allocation and deallocation tasks.
  - Performs garbage collection when memory is idle or programs need more space.

- **Types of Linked Lists:**
  - Various types of linked lists will be discussed in the next section.


## Singly Linked Lists

- **Definition:**
  - Simplest type of linked list.
  - Each node contains data and a pointer to the next node of the same data type.
  - Allows traversal of data in one direction only.

- **Traversing a Linked List:**
  - Accessing nodes of the list in order to perform processing.
  - START pointer stores the address of the first node.
  - End of list marked by NULL or -1 in the NEXT field of the last node.

- **Traversing Algorithm:**
  1. Initialize PTR with the address of START.
  2. Execute a while loop until PTR encounters NULL.
  3. Apply process (e.g., print) to the current node pointed by PTR.
  4. Move to the next node by updating PTR to point to the node stored in the NEXT field.

- **Counting Nodes Algorithm:**
  - Traverse each node, incrementing a counter.
  - Display the final counter value when NULL is reached, indicating the end of the list.


## Searching for a Value in a Linked List

- **Definition:**
  - Searching a linked list involves finding a particular element in the list.
  - Nodes in a linked list consist of an information part and a next part.

- **Search Algorithm:**
  1. Initialize PTR with START, the address of the first node.
  2. Execute a while loop to compare every node's DATA with the value (VAL) being searched.
     - If VAL is found, store the address of that node in POS and exit loop.
     - If VAL is not found, set POS to NULL.

- **Algorithm Overview:**
  - Initialize PTR with START, the first node's address.
  - Compare each node's data with the value being searched.
  - If found, store node's address in POS; otherwise, POS is set to NULL.


## Inserting a New Node in a Linked List

- **Overview:**
  - Adding a new node into an existing linked list.
  - Four cases of insertion:
    1. At the beginning
    2. At the end
    3. After a given node
    4. Before a given node

- **Overflow Condition:**
  - Occurs when AVAIL = NULL or no free memory cell is available.
  - Program must handle this condition appropriately.

### Case 1: Inserting at the Beginning

- **Description:**
  - Adding a new node as the first node of the list.

- **Steps:**
  1. Create a new node with the desired data.
  2. Set the NEXT field of the new node to point to the current first node.
  3. Update START to point to the new node, making it the first node of the list.


### Case 2: Inserting at the End

- **Description:**
  - Adding a new node as the last node of the list.

- **Steps:**
  1. Create a new node with the desired data.
  2. If the list is empty (START is NULL), set START to point to the new node.
  3. Otherwise, traverse the list to reach the last node.
  4. Set the NEXT field of the last node to point to the new node.
  5. Set the NEXT field of the new node to NULL, signifying the end of the list.


### Case 3: Inserting After a Given Node

- **Description:**
  - Adding a new node after a specified node in the list.

- **Steps:**
  1. Create a new node with the desired data.
  2. Traverse the list to find the specified node after which the new node will be inserted.
  3. Set the NEXT field of the new node to point to the node following the specified node.
  4. Update the NEXT field of the specified node to point to the new node.


### Case 4: Inserting Before a Given Node

- **Description:**
  - Adding a new node before a specified node in the list.

- **Steps:**
  1. Create a new node with the desired data.
  2. Traverse the list to find the specified node before which the new node will be inserted.
  3. Keep track of the previous node (PREPTR) while traversing the list.
  4. Update the NEXT field of the previous node (PREPTR) to point to the new node.
  5. Set the NEXT field of the new node to point to the specified node.


## Deleting a Node from a Linked List

- **Overview:**
  - Removing a node from an existing linked list.
  - Three cases of deletion:
    1. Deleting the first node
    2. Deleting the last node
    3. Deleting the node after a given node

- **Underflow Condition:**
  - Occurs when attempting to delete a node from an empty list (START = NULL).

- **Memory Management:**
  - Memory occupied by the deleted node must be freed and returned to the free pool.

### Case 1: Deleting the First Node

- **Description:**
  - Removing the first node of the list.

- **Steps:**
  1. Set PTR to point to START, the first node.
  2. Set START to point to the next node.
  3. Free the memory occupied by the node pointed by PTR.

### Case 2: Deleting the Last Node

- **Description:**
  - Removing the last node of the list.

- **Steps:**
  1. Set PTR to point to START.
  2. Traverse the list to reach the second last node.
  3. Set the NEXT field of the second last node to NULL.
  4. Free the memory occupied by the last node.

### Case 3: Deleting the Node After a Given Node

- **Description:**
  - Removing the node following a specified node in the list.

- **Steps:**
  1. Set PTR to point to the specified node.
  2. Set TEMP to point to the node following PTR.
  3. Update the NEXT field of PTR to point to the node following TEMP.
  4. Free the memory occupied by TEMP.
