class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def balance(self, node):
        if node is None:
            return node

        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        self.update_height(node)
        return self.balance(node)

    def delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self.find_min(node.right)
            node.key = min_node.key
            node.right = self.delete(node.right, min_node.key)

        self.update_height(node)
        return self.balance(node)

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

# Creating an AVL tree instance
avl_tree = AVLTree()

# Inserting data into the AVL tree
data = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
for key in data:
    avl_tree.root = avl_tree.insert(avl_tree.root, key)

print("AVL Tree after insertions:")
avl_tree.inorder(avl_tree.root)
print()

# Deleting nodes from the AVL tree
nodes_to_delete = [18, 14, 28, 15, 3, 30]
for key in nodes_to_delete:
    avl_tree.root = avl_tree.delete(avl_tree.root, key)

print("AVL Tree after deletions:")
avl_tree.inorder(avl_tree.root)
print()

print("In-order traversal:")
avl_tree.inorder(avl_tree.root)
print()

print("Pre-order traversal:")
avl_tree.preorder(avl_tree.root)
print()

print("Post-order traversal:")
avl_tree.postorder(avl_tree.root)
print()
