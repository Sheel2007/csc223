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
    Node* current = list;

    while (current != NULL) {
        if (current->val == target) {
            return current; // Found the target, return the node
        }
        current = current->next;
    }

    return NULL; // Target not found in the list
}


void insert_in_front(Node** list, Node** newnode)
{
    (*newnode)->next = *list;
    *list = *newnode;
}
