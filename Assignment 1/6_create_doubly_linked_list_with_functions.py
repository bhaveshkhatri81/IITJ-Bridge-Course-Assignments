class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_beginning(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_from_end(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def display_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=' <-> ')
            current = current.prev
        print("None")


if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_beginning(0)

    print("Doubly Linked List:")
    linked_list.display_reverse()

    linked_list.delete_from_beginning()
    linked_list.delete_from_end()

    print("\nDoubly Linked List after deleting from beginning and end:")
    linked_list.display_reverse()
