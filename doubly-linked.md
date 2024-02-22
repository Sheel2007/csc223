# Doubly Linked Lists

A doubly linked list or a two-way linked list is a more complex type of linked list which contains a pointer to the next as well as the previous node in the sequence. Therefore, it consists of three parts—data, a pointer to the next node, and a pointer to the previous node as shown in Fig. 6.37.

In C, the structure of a doubly linked list can be given as,

```c
struct node
{
    struct node *prev;
    int data;
    struct node *next;
};
```

## 6.4.1 Inserting a New Node in a Doubly Linked List

In this section, we will discuss how a new node is added into an already existing doubly linked list. We will take four cases and then see how insertion is done in each case.

### Case 1: Insertion at the Beginning
To insert a new node at the beginning of a doubly linked list, the following steps are taken:

1. Allocate memory for the new node and initialize its DATA part to the desired value.
2. Set the PREV field of the new node to NULL.
3. Set the NEXT field of the new node to point to the current first node of the list.
4. Update the PREV field of the current first node to point to the new node.
5. Update the START pointer to point to the new node.

### Case 2: Insertion at the End
To insert a new node at the end of a doubly linked list, similar steps are followed, but the new node is inserted before the NULL pointer.

### Case 3: Insertion After a Given Node
To insert a new node after a given node, the NEXT and PREV pointers of the surrounding nodes are adjusted to include the new node.

### Case 4: Insertion Before a Given Node
To insert a new node before a given node, the NEXT and PREV pointers of the surrounding nodes are adjusted to include the new node.

Each case involves similar steps with adjustments made to the pointers of surrounding nodes to accommodate the new node.


## Inserting a Node at the End of a Doubly Linked List

Consider the doubly linked list shown in Fig. 6.41. Suppose we want to add a new node with data 9 as the last node of the list. Then the following changes will be done in the linked list:

1. Take a pointer variable `PTR` and make it point to the first node of the list.
2. Move `PTR` so that it points to the last node of the list.
3. Add the new node after the node pointed to by `PTR`.

Allocate memory for the new node and initialize its DATA part to 9 and its NEXT field to NULL.

### Algorithm:

1. IF `AVAIL` is NULL:
   - Write "OVERFLOW".
   - Exit.
2. Set `NEW_NODE` as `AVAIL`.
3. Set `AVAIL` as `AVAIL NEXT`.
4. Set `DATA` as the desired value.
5. Set `PREV` as NULL.
6. Set `PTR` as `START`.
7. While `PTR` is not NULL, do:
   - Move `PTR` to the next node.
8. Set `NEXT` of the last node pointed by `PTR` as `NEW_NODE`.
9. Set `PREV` of `NEW_NODE` to point to the node pointed by `PTR` (now the second last node of the list).


## Inserting a Node After a Given Node in a Doubly Linked List

Consider the doubly linked list shown in Fig. 6.44. Suppose we want to add a new node with value 9 after the node containing 3. 

### Algorithm:

1. Take a pointer variable `PTR` and make it point to the first node of the list.
2. Move `PTR` further until the data part of `PTR` is equal to the value after which the new node has to be inserted.
3. Insert the new node between `PTR` and the node succeeding it.

Allocate memory for the new node and initialize its DATA part to 9.

Figure 6.43 shows the algorithm to insert a new node after a given node in a doubly linked list. In Step 5, we take a pointer `PTR` and initialize it with `START`. That is, `PTR` now points to the first node of the linked list. In the while loop, we traverse through the linked list to reach the node that has its value equal to the specified value. Once we reach this node, we change the `NEXT` and `PREV` fields to insert the new node after it.


## 6.4.2 Deleting a Node from a Doubly Linked List

In this section, we will see how a node is deleted from an already existing doubly linked list. We will take four cases and then see how deletion is done in each case.

### Case 1: Deleting the First Node
To delete the first node from a doubly linked list:

1. Free the memory occupied by the first node of the list.
2. Make the second node of the list the new START node.

Figure 6.48 shows the algorithm to delete the first node of a doubly linked list. In Step 1 of the algorithm, we check if the linked list exists or not. If `START = NULL`, then it signifies that there are no nodes in the list and the control is transferred to the last statement of the algorithm. However, if there are nodes in the linked list, then we use a temporary pointer variable `PTR` that is set to point to the first node of the list. For this, we initialize `PTR` with `START` that stores the address of the first node of the list. In Step 3, `START` is made to point to the next node in sequence and finally the memory occupied by `PTR` (initially the first node of the list) is freed and returned to the free pool.


## Deleting the Last Node from a Doubly Linked List

Consider the doubly linked list shown in Fig. 6.49. Suppose we want to delete the last node from the linked list, then the following changes will be done in the linked list:

1. Take a pointer variable `PTR` that points to the first node of the list.
2. Move `PTR` so that it now points to the last node of the list.
3. Free the space occupied by the node pointed by `PTR` and store NULL in the `NEXT` field of its preceding node.

Figure 6.50 shows the algorithm to delete the last node of a doubly linked list. In Step 2, we take a pointer variable `PTR` and initialize it with `START`. That is, `PTR` now points to the first node of the linked list. The while loop traverses through the list to reach the last node. Once we reach the last node, we can also access the second last node by taking its address from the `PREV` field of the last node. To delete the last node, we simply have to set the `NEXT` field of the second last node to NULL, so that it now becomes the (new) last node of the linked list. The memory of the previous last node is freed and returned to the free pool.

## Deleting the Node After a Given Node in a Doubly Linked List

Consider the doubly linked list shown in Fig. 6.51. Suppose we want to delete the node that succeeds the node which contains data value 4. Then the following changes will be done in the linked list:

1. Take a pointer variable `PTR` and make it point to the first node of the list.
2. Move `PTR` further so that its data part is equal to the value after which the node has to be deleted.
3. Delete the node succeeding `PTR`.

Figure 6.52 shows the algorithm to delete a node after a given node of a doubly linked list. In Step 2, we take a pointer variable `PTR` and initialize it with `START`. That is, `PTR` now points to the first node of the doubly linked list. The while loop traverses through the linked list to reach the given node. Once we reach the node containing `VAL`, the node succeeding it can be easily accessed by using the address stored in its `NEXT` field. The `NEXT` field of the given node is set to contain the contents in the `NEXT` field of the succeeding node. Finally, the memory of the node succeeding the given node is freed and returned to the free pool.

## Deleting the Node Before a Given Node in a Doubly Linked List

Consider the doubly linked list shown in Fig. 6.53. Suppose we want to delete the node preceding the node with value 4. Then the following changes will be done in the linked list:

1. Take a pointer variable `PTR` that points to the first node of the list.
2. Move `PTR` further till its data part is equal to the value before which the node has to be deleted.
3. Delete the node preceding `PTR`.

Figure 6.54 shows the algorithm to delete a node before a given node of a doubly linked list. In Step 2, we take a pointer variable `PTR` and initialize it with `START`. That is, `PTR` now points to the first node of the linked list. The while loop traverses through the linked list to reach the desired node. Once we reach the node containing `VAL`, the `PREV` field of `PTR` is set to contain the address of the node preceding the node which comes before `PTR`. The memory of the node preceding `PTR` is freed and returned to the free pool.

Hence, we see that we can insert or delete a node in a constant number of operations given only that node’s address. Note that this is not possible in the case of a singly linked list which requires the previous node’s address also to perform the same operation.


