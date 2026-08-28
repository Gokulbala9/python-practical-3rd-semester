class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Inserted: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        item = self.queue.pop(0)
        print(f"Deleted: {item}")
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements are:", " ".join(map(str, self.queue)))

    def is_empty(self):
        return len(self.queue) == 0

if __name__ == "__main__":
    q = Queue()
    while True:
        print("\n1. Insert\n2. Delete\n3. Display\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            element = input("Enter the element to insert: ")
            q.enqueue(element)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice")
