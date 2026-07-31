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
            print(f'"{data}" pushed to stack')
        except MemoryError:
            print("Stack Overflow")

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"

        popped_data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped_data

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.top.data

    def size(self):
        return self.count

    def display(self):
        if self.is_empty():
            print("Stack is Empty")
            return

        print("Stack elements:")
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next
stack = Stack()
stack.push("Python Programming")
stack.push("Data Structures")
stack.push("Computer Networks")
stack.display()
print("Top Book:", stack.peek())
print("Popped Book:", stack.pop())
stack.display()
print("Stack Size:", stack.size())
print("Popped Book:", stack.pop())
print("Popped Book:", stack.pop())
print("Popped Book:", stack.pop())
print("Is Empty:", stack.is_empty())
