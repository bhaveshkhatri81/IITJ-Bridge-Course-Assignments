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


def merge_sorted_lists(l_list, k_list):
    merged_list = SinglyLinkedList()

    l_current = l_list.head
    k_current = k_list.head

    while l_current and k_current:
        if l_current.data < k_current.data:
            merged_list.insert_at_end(l_current.data)
            l_current = l_current.next
        else:
            merged_list.insert_at_end(k_current.data)
            k_current = k_current.next

    while l_current:
        merged_list.insert_at_end(l_current.data)
        l_current = l_current.next

    while k_current:
        merged_list.insert_at_end(k_current.data)
        k_current = k_current.next

    return merged_list


if __name__ == "__main__":
    l_list = SinglyLinkedList()
    l_list.insert_at_end(1)
    l_list.insert_at_end(3)
    l_list.insert_at_end(5)

    k_list = SinglyLinkedList()
    k_list.insert_at_end(2)
    k_list.insert_at_end(4)
    k_list.insert_at_end(6)

    print("Sorted Linked List L:")
    l_list.display()

    print("Sorted Linked List K:")
    k_list.display()

    merged_list = merge_sorted_lists(l_list, k_list)
    print("Merged Sorted Linked List:")
    merged_list.display()
