class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def _height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)
    
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        
        return y
    
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        
        return x
    
    def _balance(self, node):
        if node is None:
            return node
        
        balance = self._balance_factor(node)
        
        if balance > 1:
            if self._balance_factor(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        
        if balance < -1:
            if self._balance_factor(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        
        return node
    
    def insert(self, value):
        self.root = self._insert(self.root, value)
    
    def _insert(self, root, value):
        if root is None:
            return TreeNode(value)
        
        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)
        else:
            return root  # No duplicates allowed
        
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        return self._balance(root)
    
    def delete(self, value):
        self.root = self._delete(self.root, value)
    
    def _delete(self, root, value):
        if root is None:
            return root
        
        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self._get_min_value_node(root.right)
            root.value = temp.value
            root.right = self._delete(root.right, temp.value)
        
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        return self._balance(root)
    
    def _get_min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result
    
    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)
    
    def pre_order(self):
        result = []
        self._pre_order(self.root, result)
        return result
    
    def _pre_order(self, node, result):
        if node is not None:
            result.append(node.value)
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)
    
    def post_order(self):
        result = []
        self._post_order(self.root, result)
        return result
    
    def _post_order(self, node, result):
        if node is not None:
            self._post_order(node.left, result)
            self._post_order(node.right, result)
            result.append(node.value)

# Example usage
if __name__ == "__main__":
    avl_tree = AVLTree()
    elements = [10, 20, 30, 40, 50, 25]

    for element in elements:
        avl_tree.insert(element)

    print("In-order traversal:", avl_tree.in_order())
    print("Pre-order traversal:", avl_tree.pre_order())
    print("Post-order traversal:", avl_tree.post_order())

    avl_tree.delete(30)
    print("In-order traversal after deleting 30:", avl_tree.in_order())
