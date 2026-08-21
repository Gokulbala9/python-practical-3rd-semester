class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        try:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
            self.count += 1
            print(f'"{data}" pushed to stack.')
        except MemoryError:
            print("Error: Stack Overflow.")

    def pop(self):
        if self.is_empty():
            return "Error: Stack Underflow (The stack is already empty)."
        popped_data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped_data

    def peek(self):
        if self.is_empty():
            return "The stack is currently empty."
        return self.top.data

    def size(self):
        return self.count

    def display(self):
        if self.is_empty():
            print("The stack is currently empty.")
            return
        print("Stack elements (Top to Bottom):")
        temp = self.top
        while temp:
            print(f" -> {temp.data}")
            temp = temp.next


stack = Stack()

while True:
    print("\n====================================")
    print(" --- Linked List Stack Menu ---")
    print("====================================")
    print("1. Push (Add item)")
    print("2. Pop (Remove top item)")
    print("3. Peek (View top item)")
    print("4. Display (Show all items)")
    print("5. Size (Count total items)")
    print("6. Check If Empty")
    print("7. Exit")
    print("====================================")
    
    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        item = input("Enter the item you want to push: ").strip()
        if item:
            stack.push(item)
        else:
            print("Input cannot be empty.")
            
    elif choice == "2":
        result = stack.pop()
        if "Error" in str(result):
            print(result)
        else:
            print(f"Successfully popped: {result}")
            
    elif choice == "3":
        top_item = stack.peek()
        if "empty" in str(top_item).lower():
            print(top_item)
        else:
            print(f"The top item is: {top_item}")
            
    elif choice == "4":
        stack.display()
        
    elif choice == "5":
        print(f"Total items in stack: {stack.size()}")
        
    elif choice == "6":
        if stack.is_empty():
            print("Yes, the stack is currently empty.")
        else:
            print("No, the stack has items in it.")
            
    elif choice == "7":
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select a valid number between 1 and 7.")
