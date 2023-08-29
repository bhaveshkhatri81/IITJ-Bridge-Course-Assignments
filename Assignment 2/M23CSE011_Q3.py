class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class StackUsingDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Stack is empty. Cannot pop.")
        data = self.tail.data
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data

    def top(self):
        if self.size == 0:
            raise IndexError("Stack is empty. No top element.")
        return self.tail.data

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size


if __name__ == "__main__":
    stack = StackUsingDoublyLinkedList()

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
