class Node:
    def __init__(self, book_title):
        self.data = book_title
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, book_title):
        if self.root is None:
            self.root = Node(book_title)
            print("Root node created.")
        else:
            self._insert_recursive(self.root, book_title)

    def _insert_recursive(self, current_node, book_title):
        if book_title < current_node.data:
            if current_node.left is None:
                current_node.left = Node(book_title)
                print("Inserted on the left.")
            else:
                self._insert_recursive(current_node.left, book_title)
        else:
            if current_node.right is None:
                current_node.right = Node(book_title)
                print("Inserted on the right.")
            else:
                self._insert_recursive(current_node.right, book_title)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):
        if current_node:
            self._inorder_recursive(current_node.left)
            print(current_node.data)
            self._inorder_recursive(current_node.right)

if __name__ == "__main__":
    tree = BinaryTree()
    while True:
        print("\n1. Insert Book Title\n2. View All Books (Inorder)\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            tree.insert(title)
        elif choice == "2":
            print("\nStored Book Titles:")
            tree.inorder_traversal()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
