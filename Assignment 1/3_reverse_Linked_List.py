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

    def reverse_from_x_to_y(self, x, y):
        if not self.head:
            return

        # Find the node at position (x-1)
        prev_x = None
        current = self.head
        count = 1

        while current and count < x:
            prev_x = current
            current = current.next
            count += 1

        if not current:
            print(
                "Invalid values of x and y. The linked list does not have position X or Y.")
            return

        # Reverse the linked list from position X to position Y
        prev = None
        end = current
        for _ in range(y - x + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        if prev_x:
            prev_x.next = prev
        else:
            self.head = prev

        end.next = current


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)

    print("Original Singly Linked List:")
    linked_list.display()

    x = 2
    y = 4
    linked_list.reverse_from_x_to_y(x, y)
    print("Linked List after reversing from position {} to position {}:".format(x, y))
    linked_list.display()
