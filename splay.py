class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to create a new node with a given key
def new_node(key):
    return Node(key)

# Right rotate operation
def right_rotate(x):
    y = x.left
    x.left = y.right
    y.right = x
    return y

# Left rotate operation
def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

# Splay operation to move the accessed node to the root
def splay(root, key):
    if root is None:
        return new_node(key)
    if root.key == key:
        return root

    if root.key > key:
        if root.left is None:
            return root
        if root.left.key > key:
            # Zig-zig (left-left)
            root.left.left = splay(root.left.left, key)
            root = right_rotate(root)
        elif root.left.key < key:
            # Zig-zag (left-right)
            root.left.right = splay(root.left.right, key)
            if root.left.right:
                root.left = left_rotate(root.left)
        return root.left if root.left is None else right_rotate(root)
    else:
        if root.right is None:
            return root
        if root.right.key > key:
            # Zig-zag (right-left)
            root.right.left = splay(root.right.left, key)
            if root.right.left:
                root.right = right_rotate(root.right)
        elif root.right.key < key:
            # Zig-zig (right-right)
            root.right.right = splay(root.right.right, key)
            root = left_rotate(root)
        return root.right if root.right is None else left_rotate(root)

# Insertion operation into the splay tree
def insert(root, key):
    if root is None:
        return new_node(key)

    # Splay the tree to move the accessed node to the root
    root = splay(root, key)

    # If the key is already present, return the root
    if root.key == key:
        return root

    # Create a new node
    node = new_node(key)
    
    # Perform insertion based on the key's value
    if root.key > key:
        node.right = root
        node.left = root.left
        root.left = None
    else:
        node.left = root
        node.right = root.right
        root.right = None
    return node

# Pre-order traversal of the tree
def pre_order(node):
    if node:
        print(node.key, end=" ")
        pre_order(node.left)
        pre_order(node.right)

# Example usage
root = None
root = insert(root, 100)
root = insert(root, 50)
root = insert(root, 200)
root = insert(root, 40)
root = insert(root, 60)
print("Preorder traversal of the modified Splay tree:")
pre_order(root)
