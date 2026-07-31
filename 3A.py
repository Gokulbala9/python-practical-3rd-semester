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

s = Stack(3)
s.push("Python Programming")
s.push("Data Structures")
s.push("Computer Networks")
s.push("Operating Systems")
s.display()
print("Top Book:", s.peek())
print("Popped Book:", s.pop())
s.display()
print("Stack Size:", s.size())
