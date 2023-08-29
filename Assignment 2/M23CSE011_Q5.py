
class QueueUsingStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, data):
        while self.stack_dequeue:
            self.stack_enqueue.append(self.stack_dequeue.pop())

        self.stack_enqueue.append(data)

    def dequeue(self):
        while self.stack_enqueue:
            self.stack_dequeue.append(self.stack_enqueue.pop())

        if self.stack_dequeue:
            return self.stack_dequeue.pop()
        else:
            raise IndexError("Queue is empty. Cannot dequeue.")

    def front_element(self):
        while self.stack_enqueue:
            self.stack_dequeue.append(self.stack_enqueue.pop())

        if self.stack_dequeue:
            return self.stack_dequeue[-1]
        else:
            raise IndexError("Queue is empty. No front element.")

    def is_empty(self):
        return not (self.stack_enqueue or self.stack_dequeue)

    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)


if __name__ == "__main__":
    queue = QueueUsingStacks()

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
