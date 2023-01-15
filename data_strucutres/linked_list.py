class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def length(self):
        curr = self.head
        list_length = 0

        while curr:
            list_length += 1
            curr = curr.next

        return list_length

    def insert_at_start(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return self.head

    def insert_after_value(self, node_value, value):
        if not self.head:
            raise Exception("The list is empty!")
        curr = self.head
        while curr:
            if curr.data == node_value:
                node = Node(value)
                node.next = curr.next
                curr.next = node
                return self.head
            curr = curr.next
        print(f"There is no value {node_value} in current list")

    def insert_after_position(self, pos, value):
        # TODO
        pass
    def delete_at_start(self):
        if not self.head:
            raise Exception("The list is empty, nothing to delete!")
        self.head = self.head.next
        return self.head

    def delete_node(self, value):
        if not self.head:
            raise Exception("The list is empty, nothing to delete!")
        if self.head.data == value:
            return self.delete_at_start()
        curr = self.head
        while curr:
            if curr.next and curr.next.data == value:
                curr.next = curr.next.next
                return self.head
            curr = curr.next
        print(f"There is no value {value} in current list")

    def reverse(self):
        if not self.head:
            raise Exception("Executing reversing operation on an empty list, nothing to reverse!")
        curr = self.head
        prev = None
        next = curr.next

        while curr.next:
            curr.next = prev
            prev = curr
            curr = next
            next = curr.next
        curr.next = prev
        self.head = curr
        return self.head

    def create_from_list(self, arr):
        if not len(arr):
            raise ValueError("Passed an empty array")

        curr = Node(arr[0])
        self.head = curr

        if len(arr) > 1:
            i = 1
            while i < len(arr):
                curr.next = Node(arr[i])
                curr = curr.next
                i += 1

        return self.head

    def print_list(self):
        if self.head:
            curr = self.head
            while curr:
                print(f'{curr.data} -> ', end="")
                curr = curr.next
        print("None")
