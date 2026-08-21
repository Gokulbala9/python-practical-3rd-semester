class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return
        self.stack.append(item)
        print(f'"{item}" pushed to stack')

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack elements:", self.stack)

size_input = int(input("Enter the maximum size of the stack: "))
s = Stack(size_input)

while True:
    print("\n--- Stack Operations Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Size")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        book = input("Enter the name of the book to push: ")
        s.push(book)
    elif choice == "2":
        print("Popped Book:", s.pop())
        
    elif choice == "3":
        print("Top Book:", s.peek())
    elif choice == "4":
        s.display()
    elif choice == "5":
        print("Stack Size:", s.size())
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please select between 1 and 6.")
