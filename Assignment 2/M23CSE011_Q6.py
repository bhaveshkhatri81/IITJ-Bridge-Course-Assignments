class SpecialStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data):
        self.stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty. Cannot pop.")
        data = self.stack.pop()
        if data == self.min_stack[-1]:
            self.min_stack.pop()
        return data

    def top(self):
        if not self.stack:
            raise IndexError("Stack is empty. No top element.")
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            raise IndexError("Stack is empty. No minimum element.")
        return self.min_stack[-1]

    def is_empty(self):
        return not self.stack

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = SpecialStack()

    stack.push(3)
    stack.push(1)
    stack.push(2)

    print("Stack size:", stack.size())
    print("Top element:", stack.top())
    print("Minimum element:", stack.get_min())

    print("Pop:", stack.pop())
    print("Is Stack empty?", stack.is_empty())

    stack.push(5)
    print("Stack size:", stack.size())
    print("Top element:", stack.top())
    print("Minimum element:", stack.get_min())

    print("Pop:", stack.pop())
    print("Is Stack empty?", stack.is_empty())

    print("Pop:", stack.pop())
    print("Minimum element:", stack.get_min())
    print("Is Stack empty?", stack.is_empty())

    print("Pop:", stack.pop())
    print("Is Stack empty?", stack.is_empty())
