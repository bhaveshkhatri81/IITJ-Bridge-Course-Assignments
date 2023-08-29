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

    def remove_duplicates(self):
        if not self.head:
            return

        seen = set()
        current = self.head
        seen.add(current.data)

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(5)

    print("Original Linked List:")
    linked_list.display()

    linked_list.remove_duplicates()

    print("\nLinked List after removing duplicates:")
    linked_list.display()
