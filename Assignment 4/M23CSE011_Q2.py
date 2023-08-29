class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.value)
        inorder_traversal(node.right, result)

def find_third_largest(root):
    result = []
    inorder_traversal(root, result)
    if len(result) < 3:
        return None
    return result[-3]

def main():
    root = None
    n = int(input("Enter the number of nodes in the BST: "))
    for _ in range(n):
        value = int(input("Enter node value: "))
        root = insert(root, value)

    third_largest = find_third_largest(root)
    if third_largest is not None:
        print("The third largest element in the BST is:", third_largest)
    else:
        print("The BST does not have a third largest element.")

if __name__ == "__main__":
    main()
