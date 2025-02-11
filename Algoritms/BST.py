class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self,value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        current_node = self.root
        while True:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                else:
                    current_node = current_node.left
            if value >= current_node.value:
                if not current_node.right:
                    current_node.right = new_node
                else:
                    current_node = current_node.right

    def search(self, val):
        if not self.root:
            return

        list = []
        current_node = self.root
        while current_node:
            if val < current_node.value:
                current_node = current_node.left
                list.append("lewo")
            if val > current_node.value:
                current_node = current_node.right
                list.append("prawo")
            if val == current_node.value:
                list.append("bomba")
                return val


drzewo = BST()
drzewo.add(5)
drzewo.add(4)
drzewo.add(2)
drzewo.add(1)
drzewo.add(3)
drzewo.add(5)
drzewo.add(6)
drzewo.add(7)





