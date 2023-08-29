class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def flatten_tree(node, values):
    if node is None:
        return
    values.append(node.value)
    flatten_tree(node.left, values)
    flatten_tree(node.right, values)

def sorted_array_to_bst(values):
    if not values:
        return None
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = sorted_array_to_bst(values[:mid])
    root.right = sorted_array_to_bst(values[mid+1:])
    return root

def binary_tree_to_bst(root):
    values = []
    flatten_tree(root, values)
    values.sort()
    new_root = sorted_array_to_bst(values)
    return new_root

def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)

# Example usage
def create_sample_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    return root

original_tree = create_sample_tree()
bst_root = binary_tree_to_bst(original_tree)
result = inorder_traversal(bst_root)
print(result)
