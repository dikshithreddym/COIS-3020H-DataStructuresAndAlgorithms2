import random

class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None
    
    def left_rotate(self, node):
        # Perform left rotation to maintain the heap property
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
    
    def right_rotate(self, node):
        # Perform right rotation to maintain the heap property
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def insert(self, root, key, priority):
        # Insert key in BST manner
        if root is None:
            return TreapNode(key, priority)
        
        if key < root.key:
            root.left = self.insert(root.left, key, priority)
        else:
            root.right = self.insert(root.right, key, priority)

        # Check if the heap property is violated
        if root.left and root.left.priority > root.priority:
            # Right rotation to restore heap property
            root = self.right_rotate(root)
        elif root.right and root.right.priority > root.priority:
            # Left rotation to restore heap property
            root = self.left_rotate(root)
        
        return root
    
    def print_inorder(self, root):
        # In-order traversal to print the tree
        if root is not None:
            self.print_inorder(root.left)
            print(f"({root.key}, {root.priority})", end=" ")
            self.print_inorder(root.right)
    
    def insert_key(self, key, priority):
        # Public insert function that starts from the root
        self.root = self.insert(self.root, key, priority)

# Main Program
if __name__ == "__main__":
    treap = Treap()
    
    # Input number of keys and their priorities
    n = int(input("How many keys you want to enter: "))
    
    for i in range(n):
        key, priority = map(int, input(f"Enter key and priority for key {i+1}: ").split())
        treap.insert_key(key, priority)
    
    print("\nTreap after insertion:")
    treap.print_inorder(treap.root)
    print()  # for a new line
