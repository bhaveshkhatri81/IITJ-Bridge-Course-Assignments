class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if not self.head:  # If the list is empty, make new_node as head and circular.
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next

            new_node.next = current.next
            current.next = new_node


if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()

    circular_linked_list.insert_at_position(10, 0)
    circular_linked_list.insert_at_position(20, 1)
    circular_linked_list.insert_at_position(30, 2)

    circular_linked_list.display()
