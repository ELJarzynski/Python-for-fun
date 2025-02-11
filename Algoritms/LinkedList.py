class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def remove_from_head(self):
        if not self.head:
            pass
        else:
            destroying_node = self.head
            self.head = self.head.next

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        if not self.head:
            pass
        else:
            current_node = self.head
            while current_node.next:
                previous_node = current_node
                current_node = current_node.next

            previous_node.next = None
            self.tail = previous_node

    def find(self,index):
        if not self.head:
            pass
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next

        return current_node.value

    def insert(self, index, value):
        new_node = Node(value)

        if not self.head:
            pass

        if index == 0:
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
        else:
            current_node = self.head
            for i in range(index):
                previous_node = current_node
                current_node = current_node.next

            current_node = current_node.next
            previous_node.next = new_node
            new_node.next = current_node


    def __len__(self):
        length = 0
        if not self.head:
            return length
        else:
            current_node = self.head
            while current_node:
                current_node = current_node.next
                length += 1

        return length

    def __str__(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.value))
            current_node = current_node.next

        return "->".join(elements)

# if __name__ =="__main__":
#     lista = LinkedList()
#     lista.add_to_tail(200)
#
#     lista.add_to_head(5)
#     lista.add_to_head(4)
#     lista.add_to_head(3)
#     lista.add_to_head(2)
#     lista.add_to_head(1)
#     lista.add_to_head(0)
#     lista.add_to_tail(6)
#
#
#     lista.remove_from_head()
#     lista.remove_from_tail()
#
#     lista.insert(0,10)
