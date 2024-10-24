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
            if head == None
                

        else if pos == 2:
        # add at the end
        else if pos == 3:
            for count, ele in
        else:


    def print_nodes(self):

