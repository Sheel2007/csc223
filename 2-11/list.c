#include <stdio.h>
#include <stdlib.h>
#include "list.h"

Node* make_node(int data)
{
    Node* new = malloc(sizeof(Node));
    if (new == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new->val = data;
    new->next = NULL;

    return new;
}

Node* find_in_list(Node* list, int target)
{
    // Start traversal from the head of the list
    Node* current = list;

    // Traverse the list until the end is reached
    while (current != NULL) {
        // Check if the current node's value matches the target value
        if (current->val == target) {
            return current; // Found the target, return the node
        }
        // Move to the next node in the list
        current = current->next;
    }

    return NULL; // Target not found in the list
}


void insert_in_front(Node** list, Node** newnode)
{
    (*newnode)->next = *list;
    *list = *newnode;
}

void insert_at_end(Node** list, Node** newnode) {
    // If the list is empty, make the new node the head of the list
    if (*list == NULL) {
        *list = *newnode;
    } else {
        // Traverse the list to find the last node
        Node* current = *list;
        while (current->next != NULL) {
            current = current->next;
        }
        // Insert the new node at the end of the list
        current->next = *newnode;
    }
    // Ensure the new node points to NULL as it's the last node
    (*newnode)->next = NULL;
}

