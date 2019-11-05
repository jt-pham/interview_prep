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
        """
        Helper function to generate lists
        :return: A linked list with your own values
        """
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            value = int(input("Enter the value for the node:"))
            self.insert_end(value)

        self.traverse()
        return self

    def traverse(self):
        """
        Print the current LinkedList
        :return:
        """
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
        """
        Insert a node after a specified value
        :param key: Node value to search, and insert after
        :param data: Data to insert after specified key
        :return: None
        """
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
        """
        Insert a node before a specified value
        :param key: Node value to search, and insert before
        :param data: Data to insert before specified key
        :return: None
        """
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
        """
        Insert node at a specified index
        :param index: position to insert data
        :param data: data to insert
        :return: None
        """
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

    def search(self, key):
        """
        :param data: Value to search for in LinkedList
        :return: True or False, if value is found or not
        """
        if self.head is None:
            print("List has no element")
            return False
        current = self.head
        while current is not None:
            if current.data == key:
                print("found {}".format(key))
                return True
            current = current.next
        print("could not find {}".format(key))
        return False

    def delete_head(self):
        """
        Delete head element of LinkedList
        Overwrite self.head with self.head.next
        :return: True/False, if successfully deleted or not
        """
        if self.head is None:
            print("so no head?")
            return False
        self.head = self.head.next

    def delete(self, key):
        """
        Delete a Node by Value, if it exists
        :param key: Node to search for and delete
        :return: None
        """
        if self.head is None:
            print("so no head?")
            return False

        if self.head.data == key:
            print("deleted {}".format(key))
            self.head = self.head.next
            return True

        current = self.head
        while current is not None:
            if current.next.data == key:
                break
            current = current.next

        if current.next is None:
            print("List has no element")
            return False
        else:
            current.next = current.next.next
            print("deleted {}".format(key))
            return True

    def reverse(self):
        """
        Reverse a linked list
        :return: a reversed linked list
        """
        previous, next = None, None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
        return self.head




a = LinkedList()
a.insert_end(10)
a.insert_end(12)
a.insert_end(40)
a.insert_end(120)
a.insert_end(10222)
a.insert_end(102222222)
a.insert_position(3, 420)
a.delete(10222)
a.search(1960)
a.reverse()

a.traverse()

