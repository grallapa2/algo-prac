class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def has_next(self):
        return self.next != None

class SinglyLinkedList(object):
    def __init__(self, node = None):
        self.length = 0
        self.head = node

    def add_node(self,data):
        pos = input("Enter 1 for beginning, 2 for end, 3 to pick a position")
        val = input("Enter a value you want to insert")
        if pos == 1:
        # add at the beginning
            new_node = Node(val)
            if self.head == None:
                self.head = new_node
            else:
                temp = self.head
                head = new_node
                head.next = temp
        elif pos == 2:
        # add at the end
            current = self.head
            new_node = Node(val)
            while current.next != None
                current = current.next
            current.next = new_node
        elif pos == 3:
            picked_position = input("Enter position number:")
            current_pos = 1
            current = self.head
            while picked_position != current_pos:
                current = current.next
            temp = current.next
            new_node = Node(val)
            current.next = new_node
            new_node.next = temp
        else:
            print("Enter a valid number")

    def print_nodes(self):
        current = self.head
        while current.next != None
            temp = current
            print (temp.data)
            current = current.next