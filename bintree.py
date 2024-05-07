class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert_recursively(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursively(node.right, key)
        
        return node

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)

    def inorder_traversal(self):
        def _inorder_traversal(node):
            if node:
                _inorder_traversal(node.left)
                print(node.key, end=" ")
                _inorder_traversal(node.right)
        
        _inorder_traversal(self.root)

# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:")
bst.inorder_traversal()  # Output: 20 30 40 50 60 70 80

print("\nSearch for 40:")
result = bst.search(40)
if result:
    print("Found")
else:
    print("Not Found")

print("Search for 90:")
result = bst.search(90)
if result:
    print("Found")
else:
    print("Not Found")
