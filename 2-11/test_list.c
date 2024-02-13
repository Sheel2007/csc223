#include <stdio.h>
#include <ctest.h>
#include "list.h"

int main()
{
    BEGIN_TESTING("list.h");

    TEST("Can create a node") {
        Node* n = make_node(3);
        ASSERT_EQ(n->val, 3);
        ASSERT_EQ(n->next, NULL);
    }
    
    TEST("Can create two nodes and link them together") {
        Node* n1 = make_node(3);
        Node* n2 = make_node(2);
        n1->next = n2;
        ASSERT_EQ(n1->val, 3);
        ASSERT_EQ(n1->next->val, 2);
        ASSERT_NOT_EQ(n1->next, NULL);
        ASSERT_EQ(n1->next->next, NULL);
    }
 
    TEST("Can add a node to an empty list") {
        Node* mylist = NULL;
        Node* n = make_node(2);
        insert_in_front(&mylist, &n);
        ASSERT_EQ(mylist->val, 2);
        ASSERT_EQ(mylist->next, NULL);
    }

    TEST("Can find an item in the list") {
        // Create a linked list: 1 -> 2 -> 3 -> NULL
        Node* n1 = make_node(1);
        Node* n2 = make_node(2);
        Node* n3 = make_node(3);
        n1->next = n2;
        n2->next = n3;

        // Test finding an existing item
        Node* result1 = find_in_list(n1, 2);
        ASSERT_EQ(result1->val, 2);
        ASSERT_EQ(result1->next->val, 3);

        // Test finding a non-existent item
        Node* result2 = find_in_list(n1, 5);
        ASSERT_EQ(result2, NULL);
    }

    TEST("Can insert a node at the end of the list") {
        // Create a linked list: 1 -> 2 -> 3 -> NULL
        Node* n1 = make_node(1);
        Node* n2 = make_node(2);
        Node* n3 = make_node(3);
        n1->next = n2;
        n2->next = n3;

        // Create a new node and insert it at the end of the list
        Node* new_node = make_node(4);
        insert_at_end(&n1, &new_node);

        // Traverse the list to verify the insertion
        Node* current = n1;
        while (current->next != NULL) {
            current = current->next;
        }
        
        ASSERT_EQ(current->val, 4); // Check the value of the last node
        ASSERT_EQ(current->next, NULL); // Ensure the last node points to NULL
    }

    END_TESTING();
}
