class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_nth_node(self, n):
        if n <= 0:
            print("Invalid value of n.")
            return

        if not self.head:
            print("List is empty.")
            return

        if n == 1:
            self.head = self.head.next
            return

        count = 1
        current = self.head
        prev = None

        while current:
            if count == n:
                prev.next = current.next
                return
            prev = current
            current = current.next
            count += 1

        print("Position out of range.")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Test the implementation
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_end(10)
    linked_list.insert_end(20)
    linked_list.insert_end(30)
    linked_list.insert_end(40)
    linked_list.insert_end(50)

    n = 3  # Remove the 3rd node (30 in this case)
    linked_list.remove_nth_node(n)

    linked_list.display()
