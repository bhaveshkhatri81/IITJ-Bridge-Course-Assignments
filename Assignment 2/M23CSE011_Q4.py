class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.front = new_node
            self.rear = new_node
            new_node.next = new_node
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty. Cannot dequeue.")
        data = self.front.data
        if self.size == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.size -= 1
        return data

    def front_element(self):
        if self.size == 0:
            raise IndexError("Queue is empty. No front element.")
        return self.front.data

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size


if __name__ == "__main__":
    queue = CircularQueue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue size:", queue.size())
    print("Front element:", queue.front_element())

    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Is Queue empty?", queue.is_empty())

    queue.enqueue(4)
    print("Queue size:", queue.size())
    print("Front element:", queue.front_element())

    print("Dequeue:", queue.dequeue())
    print("Is Queue empty?", queue.is_empty())

    print("Dequeue:", queue.dequeue())
    print("Is Queue empty?", queue.is_empty())
