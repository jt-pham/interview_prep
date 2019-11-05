class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def make_new_list(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_end(value)

        self.traverse()

    def traverse(self):
        current = self.head
        out_string = ""
        if current is None:
            return
        else:
            while current is not None:
                out_string += "{}->".format(current.data)
                current = current.next
            print(out_string)

    def insert_start(self, data):
        """
        Set next of the new_node, to the current head
        assign head as the new node
        :param data: data to insert at beginning of LinkedList
        :return: void
        """
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        """
        Traverse to the end of the list (where next is None)
        Assign tail.next to new_node
        :param data: data to insert at end of LinkedList
        :return: void
        """
        new_node = Node(data)
        current = self.head
        if current is None:
            self.head = new_node
            return
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_after(self, key, data):

        current = self.head
        print(current.next)
        while current is not None:
            if current.data == key:
                break
            current = current.next
        if current is None:
            print("data not in the list")
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    def insert_before(self, key, data):
        if self.head is None:
            print("List has no element")
            return

        if key == self.head.data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        print(current.next)
        while current.next is not None:
            if current.next.data == key:
                break
            current = current.next
        if current.next is None:
            print("data not in the list")
        else:
            new_node = Node(data)
            new_node.next = current.next

    def insert_position(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        current = self.head

        while i < index - 1 and current is not None:
            current = current.next
            i = i + 1
        if current is None:
            print("out of bounds!")
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node


a = LinkedList()
a.insert_end(10)
a.insert_end(12)
a.insert_end(40)
a.insert_end(120)
a.insert_end(10222)
a.insert_end(102222222)
a.insert_position(3, 420)
a.traverse()