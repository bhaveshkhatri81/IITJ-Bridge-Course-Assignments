from collections import deque


class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, data):
        size = len(self.queue)
        self.queue.append(data)
        for _ in range(size):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Stack is empty. Cannot pop.")

    def top(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Stack is empty. No top element.")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    stack = StackUsingQueue()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack size:", stack.size())
    print("Top element:", stack.top())

    print("Pop:", stack.pop())
    print("Pop:", stack.pop())
    print("Is Stack empty?", stack.is_empty())

    stack.push(4)
    print("Stack size:", stack.size())
    print("Top element:", stack.top())

    print("Pop:", stack.pop())
    print("Is Stack empty?", stack.is_empty())

    print("Pop:", stack.pop())
    print("Is Stack empty?", stack.is_empty())
