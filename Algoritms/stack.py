from Algoritms.LinkedList import Node

class Stack:
    def __init__(self ):
        self.head = None
        self.tail = None

    def join_stack(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def leave_stack(self):
        if not self.head:
            pass
        else:
            currnet_node = self.head
            while currnet_node.next:
                previous_node = currnet_node # przedostatnie
                currnet_node = currnet_node.next    # ostatnie


            self.tail = previous_node
            previous_node.next = None


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

