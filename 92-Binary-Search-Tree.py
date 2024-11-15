class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left:
                self._insert(current.left, key)
            else:
                current.left = Node(key)
        elif key > current.key:
            if current.right:
                self._insert(current.right, key)
            else:
                current.right = Node(key)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

bst = BinarySearchTree()
li=[50, 30, 70, 20, 40, 60, 80]
print("unordered list : ",li)
for value in li:
    bst.insert(value)

print("In-order Traversal:", bst.inorder())
