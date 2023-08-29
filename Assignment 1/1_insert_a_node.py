
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_middle(self, data, position):
        if not self.head or position == 0:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        current = self.head
        count = 1
        while count < position and current.next:
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(7)

    print("Singly Linked List:")
    linked_list.display()

    linked_list.insert_at_start(0)
    print("Linked List after inserting at start:")
    linked_list.display()

    linked_list.insert_at_middle(2, 2)
    print("Linked List after inserting at middle:")
    linked_list.display()
