from Algoritms.LinkedList import Node

# add
# remove
# len
# str

class Queue:
    def __init__(self ):
        self.head = None
        self.tail = None

    def join_queue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def leave_queue(self):
        if not self.head:
            pass
        else:
            self.head = self.head.next

    def __len__(self):
        length = 0

        if not self.head:
            return length
        else:
            current_node = self.head
            while current_node:
                length += 1
                current_node = current_node.next

        return length


    def __str__(self):
        elements = []

        if not self.head:
            return elements
        else:
            current_node = self.head
            while current_node:
                elements.append(str(current_node.value))
                current_node = current_node.next

        return "->".join(elements)

lista=Queue()
lista.join_queue(5)
lista.join_queue(5)
lista.join_queue(3)
print(lista)
lista.leave_queue()
print(lista)
print(len(lista))