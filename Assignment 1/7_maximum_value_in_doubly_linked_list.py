class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def find_max_value(self):
        if not self.head:
            return None

        max_value = self.head.data
        current = self.head.next
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value


if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(5)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(15)

    max_value = linked_list.find_max_value()
    if max_value is not None:
        print("Maximum value in the doubly linked list:", max_value)
    else:
        print("The doubly linked list is empty.")
