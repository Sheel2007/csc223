# Chapter 8.1: Introduction to Queues

- **Concept of Queues:**
  - Queues are illustrated through various analogies:
    - People moving on an escalator: First person on is first to step out.
    - People waiting for a bus: First person in line boards first.
    - People at a ticketing window: First person in line gets the ticket first.
    - Luggage on conveyor belts: First bag placed is first to come out.
    - Cars at a toll bridge: First car to reach leaves first.
  - Key principle: First element added is the first to be served (FIFO - First-In, First-Out).

- **Definition:**
  - Queue is a FIFO data structure.
  - Element inserted first is the first to be taken out.
  - Elements added at one end (REAR) and removed from the other end (FRONT).

- **Implementation:**
  - Queues can be implemented using either arrays or linked lists.
  - This section explores implementations using both data structures.


# Chapter 8.2: Array Representation of Queues

- **Representation using Arrays:**
  - Queues can be represented using linear arrays.
  - Each queue has FRONT and REAR variables indicating positions for deletions and insertions respectively.
  - Array representation illustrated in Fig. 8.1.

- **Operations on Queues:**
  - Addition of elements:
    - Increment REAR by 1 and store the new element at the position pointed by REAR.
    - Example: If FRONT = 0 and REAR = 5, adding element 45 would result in FRONT = 0 and REAR = 6 (Fig. 8.2).
  - Deletion of elements:
    - Increment FRONT by 1.
    - Deletions are performed from the FRONT end of the queue.
    - Example: After deletion, FRONT = 1 and REAR = 6 (Fig. 8.3).
  - Overflow and Underflow Conditions:
    - Overflow: Occurs when trying to insert into a full queue (REAR = MAX - 1).
    - Underflow: Occurs when trying to delete from an empty queue (FRONT = -1 and REAR = -1).

- **Algorithms:**
  - Insertion Algorithm (Fig. 8.4):
    1. Check for overflow condition.
    2. Check if queue is empty, if so, set FRONT and REAR to 0. Otherwise, increment REAR.
    3. Store the value in the queue at the location pointed by REAR.
  - Deletion Algorithm (Fig. 8.5):
    1. Check for underflow condition.
    2. If queue has values, increment FRONT to point to the next value.

# Chapter 8.3: Linked Representation of Queues

- **Array vs Linked Representation:**
  - Arrays: Fixed size, efficient for small or known maximum size queues.
  - Linked Lists: Dynamic size, efficient for cases where size cannot be determined in advance.

- **Storage and Time Requirements:**
  - Linked representation: Storage requirement O(n), Time requirement O(1) for operations.

- **Linked Queue Representation:**
  - Each element in a linked queue has data and pointer to the next element.
  - START pointer of linked list used as FRONT, additional pointer REAR points to last element.
  - All insertions at rear end, deletions at front end. If FRONT = REAR = NULL, queue is empty.
  - Representation shown in Fig. 8.6.

- **Operations on Linked Queues:**
  - **Insert Operation:**
    - Adds an element to the end of the queue.
    - If queue is empty, new node becomes both FRONT and REAR.
    - Otherwise, insert at rear end and update REAR pointer.
    - Algorithm shown in Fig. 8.9.
  - **Delete Operation:**
    - Deletes the first element inserted in the queue (element at FRONT).
    - Check for underflow (empty queue) before deletion.
    - Algorithm shown in Fig. 8.12.
