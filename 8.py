class LogNode:
    def __init__(self, visitor_name, entry_time, purpose):
        self.visitor_name = visitor_name
        self.entry_time = entry_time
        self.purpose = purpose
        self.left = None
        self.right = None

    def __str__(self):
        return f"Name: {self.visitor_name} | Time: {self.entry_time} | Purpose: {self.purpose}"


class LogBookBST:
    def __init__(self):
        self.root = None

    def insert(self, visitor_name, entry_time, purpose):
        new_node = LogNode(visitor_name, entry_time, purpose)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.visitor_name < current.visitor_name:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def delete(self, visitor_name):
        self.root, deleted = self._delete_recursive(self.root, visitor_name)
        if deleted:
            print("Successfully removed.")
        else:
            print("Not found.")

    def _delete_recursive(self, current, name):
        if current is None:
            return current, False

        deleted = False
        if name < current.visitor_name:
            current.left, deleted = self._delete_recursive(current.left, name)
        elif name > current.visitor_name:
            current.right, deleted = self._delete_recursive(current.right, name)
        else:
            deleted = True
            if current.left is None:
                return current.right, deleted
            elif current.right is None:
                return current.left, deleted

            successor = self._find_min(current.right)
            current.visitor_name = successor.visitor_name
            current.entry_time = successor.entry_time
            current.purpose = successor.purpose
            current.right, _ = self._delete_recursive(current.right, successor.visitor_name)

        return current, deleted

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, visitor_name):
        return self._search_recursive(self.root, visitor_name)

    def _search_recursive(self, current, name):
        if current is None or current.visitor_name == name:
            return current
        if name < current.visitor_name:
            return self._search_recursive(current.left, name)
        return self._search_recursive(current.right, name)

    def inorder_traverse(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):
        if current:
            self._inorder_recursive(current.left)
            print(current)
            self._inorder_recursive(current.right)

    def postorder_traverse(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, current):
        if current:
            self._postorder_recursive(current.left)
            self._postorder_recursive(current.right)
            print(current)

    def count_total_entries(self):
        return self._count_recursive(self.root)

    def _count_recursive(self, current):
        if current is None:
            return 0
        return 1 + self._count_recursive(current.left) + self._count_recursive(current.right)


log_book = LogBookBST()

while True:
    print("\n1. Insert Log Entry")
    print("2. Delete Log Entry")
    print("3. Search Log Entry")
    print("4. Display Log (Inorder)")
    print("5. Display Log (Postorder)")
    print("6. Total Count")
    print("7. Exit")
    
    choice = input("Option: ").strip()

    if choice == '1':
        name = input("Name: ")
        time = input("Time: ")
        purpose = input("Purpose: ")
        log_book.insert(name, time, purpose)

    elif choice == '2':
        name = input("Name to remove: ")
        log_book.delete(name)

    elif choice == '3':
        name = input("Name to search: ")
        result = log_book.search(name)
        if result:
            print(result)
        else:
            print("Not found.")

    elif choice == '4':
        log_book.inorder_traverse()

    elif choice == '5':
        log_book.postorder_traverse()

    elif choice == '6':
        print(log_book.count_total_entries())

    elif choice == '7':
        break
