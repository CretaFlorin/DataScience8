class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left:
                self._insert(current.left, value)
            else:
                current.left = Node(value)
        elif value > current.value:
            if current.right:
                self._insert(current.right, value)
            else:
                current.right = Node(value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if not current:
            return False
        elif value == current.value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    #   TRAVERSĂRI

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if not node:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if not node:
            return []
        return [node.value] + self._preorder(node.left) + self._preorder(node.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if not node:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.value]

    def delete(self,value):
        self.root = self._delete(self.root, value)

    def _delete(self,node,value) :
        if not node:
            return None

            # Caut nodul
        if value < node.value:
            node.left = self._delete(node.left, value)     
        elif value > node.value:
            node.right =  self._delete(node.right,value)
        else:
            # Caz 1 — fără copii
            if not node.left and not node.right:
                return None
             # Caz 2 — un copil
            if not node.left:
                return node.right
            if not node.right:
                return node.left 
            # Caz 3 — doi copii
            succcesor = self._min_val_node(node.right)
            node.value = succcesor.value
            node.right = self._delete(node.right, succcesor.value)

        return node    

    def _min_val_node(self, node):
        while node.left:
            node = node.left
        return node
        
    
tree = BST()  

tree.insert(1)
tree.insert(10)
tree.insert(15)
tree.insert(3)
tree.insert(100)
tree.insert(4)
tree.insert(12)
tree.insert(64)

print(tree.search(3))
print(tree.search(1001))
print(tree.search(14))
print(tree.search(12))

print(tree.inorder())
print(tree.preorder())
print(tree.postorder())
print(tree.inorder())

tree.delete(10)
print(tree.inorder())

tree.delete(100)
print(tree.inorder())