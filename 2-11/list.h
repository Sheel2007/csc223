typedef struct node {
    int val;
    struct node* next;
} Node;

Node* make_node(int);
Node* find_in_list(Node*, int);
void insert_in_front(Node**, Node**);
void insert_at_end(Node**, Node**);