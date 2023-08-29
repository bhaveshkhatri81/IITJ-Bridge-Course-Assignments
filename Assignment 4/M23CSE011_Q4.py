class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_avl_tree(node):
    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1
    
    def is_balanced(node):
        if node is None:
            return True
        left_height = height(node.left)
        right_height = height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return is_balanced(node.left) and is_balanced(node.right)
    
    if node is None:
        return True
    return is_balanced(node) and is_avl_tree(node.left) and is_avl_tree(node.right)

# Example usage
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(3)
root.left.right = TreeNode(8)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)

if is_avl_tree(root):
    print("The given tree is an AVL tree.")
else:
    print("The given tree is not an AVL tree.")
